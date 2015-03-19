#!/usr/bin/env python

"""
publish.py
Allen Guo <allenguo@berkeley.edu>
Publishes textbook and website using the supplied templates and settings.
See the README file for details.
"""

import codecs, os, re
import markdown2
import config

# E.g. '1, 9-11, 13' -> [1, 9, 10, 11, 13]
def parse_range(s):
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

# E.g. 'section01 Hello - My, Name, is Bob.md' -> 'hello-my-name-is-bob.html'
def to_output_name(s, extension='.html'):
    s = re.sub('section\d* ', '', s)
    s = re.sub('\.md', '', s)
    s = re.sub(',', '', s)
    s = re.sub(' - ', ' ', s)
    s = re.sub('\(', '', s)
    s = re.sub('\)', '', s)
    chunks = s.split(' ')
    chunks = map(lambda x: x.lower(), chunks)
    chunks = filter(lambda x: x, chunks)
    return '-'.join(chunks) + extension

def to_section_title(s):
    return re.sub('section\d*', '', s.rstrip('.md')).strip()

def clear_output_directory():
    os.system('rm -r ' + os.path.join(config.output_directory, 'textbook/'))
    os.system('rm ' + os.path.join(config.output_directory, '*.html'))

def prepare_output_directory():
    os.mkdir(os.path.join(config.output_directory, 'textbook/'))

class Publisher(object):

    def __init__(self):
        self.textbook_template = codecs.open(config.textbook_html_template, encoding='utf-8').read()
        self.page_template = codecs.open(config.page_html_template, encoding='utf-8').read()
        self.full_toc = ''
        self.full_toc_new_row = True

    def generate_chapter_toc(self, sections, chapter_title):
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
        for unit_title, chapter_range in config.units:
            print 'Publishing %s...' % unit_title
            anchor = to_output_name(unit_title, extension='')
            if self.full_toc_new_row:
                if self.full_toc:
                    self.full_toc += '</div>'
                self.full_toc += '<div class="row">'
            self.full_toc_new_row = not self.full_toc_new_row
            self.full_toc += '<div class="col-md-6 full-toc-panel"'
            self.full_toc += '<a class="anchor" id="%s"></a><h2>%s</h2>' % (anchor, unit_title)
            chapters = parse_range(chapter_range)
            for chapter_num in chapters:
                self.publish_chapter(chapter_num)
            self.full_toc += '</div>'  # Close column
        self.full_toc += '</div>'  # Close row

    def publish_chapter(self, chapter_num):
        chapter_str = 'chapter%02d' % chapter_num
        chapter_dir = filter(lambda name: chapter_str in name, os.listdir('textbook'))
        if not chapter_dir:
            raise ValueError('Chapter does not exist: ' + chapter_str)
        elif len(chapter_dir) > 1:
            raise ValueError('Ambiguous chapter: ' + chapter_str)
        else:
            section_files = os.listdir(os.path.join('textbook', chapter_dir[0]))
            chapter_title = re.sub('chapter\d* ', '', chapter_dir[0])
            chapter_toc = self.generate_chapter_toc(section_files, chapter_title)
            for section in section_files:
                input_path = os.path.join('textbook/', chapter_dir[0], section)
                output_name = to_output_name(section)
                output_path = os.path.join(config.output_directory, 'textbook/', output_name)
                title = to_section_title(section)
                self.convert_section(input_path, output_path, title, chapter_toc, chapter_title)

    def convert_section(self, md_path, html_path, title, chapter_toc, chapter_title):
        edit_url = os.path.join(config.github_url, md_path)
        if os.path.exists(html_path):
            print 'Warning: Only one section can be named "%s"' % title
        output = self.textbook_template
        in_file = codecs.open(md_path, encoding='utf-8')
        out_file = codecs.open(html_path, 'w', encoding='utf-8')
        html = markdown2.markdown(in_file.read())
        output = output.replace('{{title}}', title)
        output = output.replace('{{content}}', html)
        output = output.replace('{{chaptertoc}}', chapter_toc)
        output = output.replace('{{chaptertitle}}', chapter_title)
        output = output.replace('{{editurl}}', edit_url)
        out_file.write(output)
        out_file.close()
        in_file.close()

    def publish_pages(self):
        for page_title, path in config.pages:
            print 'Publishing %s...' % page_title
            output_name = to_output_name(os.path.split(path)[1])
            output_path = os.path.join(config.output_directory, output_name)
            self.convert_page(path, output_path, page_title)

    def convert_page(self, md_path, html_path, title):
        output = self.page_template
        in_file = codecs.open(md_path, encoding='utf-8')
        out_file = codecs.open(html_path, 'w', encoding='utf-8')
        html = markdown2.markdown(in_file.read())
        output = output.replace('{{title}}', title)
        output = output.replace('{{content}}', html)
        output = output.replace('{{fulltoc}}', self.full_toc)
        out_file.write(output)
        out_file.close()
        in_file.close()        

def main():
    print 'Clearing output directory of generated files...'
    clear_output_directory()
    print 'Preparing output directory...'
    prepare_output_directory()
    p = Publisher()
    p.publish_units()
    p.publish_pages()

if __name__ == '__main__':
    main()
