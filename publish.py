#!/usr/bin/env python

#########################################################################
# publish.py
#
# Author: Allen Guo <allenguo@berkeley.edu>
#
# Publishes textbook and static pages using the settings in config.py.
# See the README file for details.
#########################################################################

import codecs, os, re
import markdown2  # should be in this directory 
import config

"""
Substitutions for simplifying filenames.
See to_output_name().
"""
OUTPUT_NAME_SUBS = [('section\d* ', ''),
                    ('\.md', ''),
                    ('\.html', ''),
                    (',', ''),
                    (' - ', ' '),
                    ('\(', ''),
                    ('\)', '')]


def open_unicode(path, mode='r'):
    """Opens a UTF-8 file in the specified mode."""
    return codecs.open(path, mode, encoding='utf-8')


def parse_range(s):
    """Reads a range into a Python list.
    E.g., '1, 9-11, 13' becomes the list [1, 9, 10, 11, 13].
    """
    if not s:
        return []
    ans = []
    chunks = re.split(',\s?', s.strip())
    for chunk in chunks:
        if '-' in chunk:
            lower, upper = map(int, chunk.split('-'))
            ans += list(range(lower, upper + 1))
        else:
            ans.append(int(chunk))
    return ans


def to_output_name(s, extension='.html'):
    """Simplifies a filename into neat hyphenated chunks.
    E.g., 'section01 Hello - My, Name, is Bob.md' becomes 'hello-my-name-is-bob.html'.
    Appends the given extension (defaults to ".html").
    """
    for original, replacement in OUTPUT_NAME_SUBS:
        s = re.sub(original, replacement, s)
    chunks = s.lower().split(' ')
    chunks = filter(lambda x: x, chunks)
    return '-'.join(chunks) + extension


def to_section_title(s):
    """Returns the title of a section based on its filename."""
    if '.' in s:
        s = s[:s.rfind('.')]
    return re.sub('section\d*', '', s).strip()


def clear_output_directory():
    """Removes all generated files from the output directory."""
    os.system('rm -r ' + os.path.join(config.output_directory, 'textbook/'))


def prepare_output_directory():
    """Creates the output directory for textbook pages."""
    os.mkdir(os.path.join(config.output_directory, 'textbook/'))


class Publisher(object):
    """Builds the textbook and website pages as specified in the config."""

    def __init__(self):
        """Loads templates and starts the main (global) TOC."""
        self.templates = {}
        for file in os.listdir('templates'):
            html = open_unicode(os.path.join('templates', file)).read()
            self.templates[file.rstrip('.html')] = html
        self.full_toc = ''
        self.full_toc_new_row = True

    def generate_chapter_toc(self, sections, chapter_title):
        """Creates the TOC for a single chapter.
        Also adds to the main (global) TOC.
        As a result, this function has side effects and is only called once each chapter.
        """
        toc = ''
        self.full_toc += '<div><b>%s</b><ul>' % chapter_title
        for section in sections:
            path = to_output_name(section)
            title = to_section_title(section)
            toc += '<li><a href="%s">%s</a></li>' % (path, title)
            self.full_toc += '<li><a href="textbook/%s">%s</a></li>' % (path, title)
        self.full_toc += '</ul></div>'
        return toc

    def publish_units(self):
        """Builds all units specified in the config.
        Creates an global TOC along the way.
        """
        for unit_title, chapter_range in config.units:
            print 'Publishing %s...' % unit_title
            if self.full_toc_new_row:
                if self.full_toc:
                    self.full_toc += '</div>'
                self.full_toc += '<div class="row">'
            self.full_toc_new_row = not self.full_toc_new_row
            self.full_toc += '<div class="col-md-6 full-toc-panel">'
            self.full_toc += '<h2>%s</h2>' % unit_title
            chapters = parse_range(chapter_range)
            for chapter_num in chapters:
                self.publish_chapter(chapter_num)
            self.full_toc += '</div>'  # Close column
        self.full_toc += '</div>'  # Close row

    def publish_chapter(self, chapter_num):
        """Builds an individual chapter."""
        # Look for chapter directories matching chapter_num
        chapter_str = 'chapter%02d' % chapter_num
        matches = filter(lambda name: chapter_str in name, os.listdir('textbook'))

        # Handle error conditions
        if not matches:
            raise ValueError('Chapter does not exist: ' + chapter_str)
        elif len(matches) > 1:
            raise ValueError('Ambiguous chapter: ' + chapter_str)

        # Gather chapter information (directory name, sections, title, TOC)
        chapter_dir = matches[0]
        section_files = sorted(os.listdir(os.path.join('textbook', chapter_dir)))
        chapter_title = re.sub('chapter\d* ', '', chapter_dir)
        chapter_toc = self.generate_chapter_toc(section_files, chapter_title)

        # Build the sections that comprise this chapter
        for section in section_files:
            input_path = os.path.join('textbook/', chapter_dir, section)
            output_name = to_output_name(section)
            output_path = os.path.join(config.output_directory, 'textbook/', output_name)
            title = to_section_title(section)
            self.convert_section(input_path, output_path, title, chapter_toc, chapter_title)

    def convert_section(self, md_path, html_path, title, chapter_toc, chapter_title):
        """Builds an individual textbook page, or section."""
        # Check for bad titles
        if len(title) > config.section_title_max_length:
            print 'Warning: Section title "%s" is too long' % title
        if os.path.exists(html_path):
            print 'Warning: Only one section can be named "%s"' % title

        # Determine GitHub URL and get template to use
        edit_url = os.path.join(config.github_url, md_path).replace('\\', '/')
        output = self.templates['textbook']

        # Prepare files
        in_file = open_unicode(md_path)
        out_file = open_unicode(html_path, 'w')

        # Convert input to Markdown
        html = markdown2.markdown(in_file.read(), extras=['fenced-code-blocks'])

        # Make templating substitutions
        output = output.replace('{{title}}', title)
        output = output.replace('{{content}}', html)
        output = output.replace('{{chaptertoc}}', chapter_toc)
        output = output.replace('{{chaptertitle}}', chapter_title)
        output = output.replace('{{editurl}}', edit_url)

        # Tell syntax highlighter we're using Scheme
        output = output.replace('<code>', '<code class=scheme>')

        # Write file
        out_file.write(output)
        out_file.close()
        in_file.close()

    def publish_pages(self):
        """Builds all static pages specified in the config."""
        for page_title, path, template in config.pages:
            print 'Publishing %s...' % page_title
            output_name = to_output_name(os.path.split(path)[1])
            output_path = os.path.join(config.output_directory, output_name)
            self.convert_page(path, output_path, template, page_title)

    def convert_page(self, input_path, output_path, template, title):
        """Builds a single static page."""
        # Get template to use
        output = self.templates[template]

        # Prepare files
        input_type = input_path.split('.')[-1]
        in_file = open_unicode(input_path)
        out_file = open_unicode(output_path, 'w')

        # Convert to Markdown if necessary
        if input_type == 'md':
            html = markdown2.markdown(in_file.read())
        else:
            html = in_file.read()

        # Make templating substitutions
        output = output.replace('{{title}}', title)
        output = output.replace('{{content}}', html)
        output = output.replace('{{fulltoc}}', self.full_toc)

        # Write file
        out_file.write(output)
        out_file.close()
        in_file.close()

    def output_toc(self):
        if config.toc_path:
            out = open(config.toc_path, 'w')
            out.write(self.full_toc)
            out.close()


def main():
    """Do all the things."""
    print 'Clearing output directory of generated files...'
    clear_output_directory()
    print 'Preparing output directory...'
    prepare_output_directory()
    p = Publisher()
    p.publish_units()
    p.publish_pages()
    p.output_toc()

if __name__ == '__main__':
    main()
