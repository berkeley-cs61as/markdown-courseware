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

# E.g. 'section01 Hello - My, Name, is Bob.md' -> 'hello-my-name-is-bob'
def to_output_name(s):
    s = re.sub('section\d* ', '', s)
    s = re.sub('\.md', '', s)
    s = re.sub(',', '', s)
    s = re.sub(' - ', ' ', s)
    s = re.sub('\(', '', s)
    s = re.sub('\)', '', s)
    chunks = s.split(' ')
    chunks = map(lambda x: x.lower(), chunks)
    chunks = filter(lambda x: x, chunks)
    return '-'.join(chunks) + '.html'

def to_section_title(s):
    return re.sub('section\d*', '', s.rstrip('.md')).strip()

def to_chapter_toc(sections):
    toc = ''
    for section in sections:
        toc += '<li><a href="%s">%s</a></li>' % (to_output_name(section), to_section_title(section))
    return toc

def clear_output_directory():
    os.system('rm -r ' + os.path.join(config.output_directory, 'textbook/'))
    os.system('rm ' + os.path.join(config.output_directory, '*.md'))

def prepare_output_directory():
    os.mkdir(os.path.join(config.output_directory, 'textbook/'))

class Publisher(object):

    def __init__(self):
        self.textbook_template = codecs.open(config.textbook_html_template, encoding='utf-8').read()
        self.static_page_template = codecs.open(config.page_html_template, encoding='utf-8').read()

    def publish_units(self):
        for unit_title, chapter_range in config.units:
            print 'Publishing %s...' % unit_title
            chapters = parse_range(chapter_range)
            for chapter_num in chapters:
                self.publish_chapter(chapter_num)

    def publish_chapter(self, chapter_num):
        chapter_str = 'chapter%02d' % chapter_num
        chapter_dir = filter(lambda name: chapter_str in name, os.listdir('.'))
        if not chapter_dir:
            print 'Chapter does not exist:', chapter_str
        elif len(chapter_dir) > 1:
            print 'Ambiguous chapter:', chapter_str
        else:
            section_files = os.listdir(chapter_dir[0])
            chapter_title = re.sub('chapter\d* ', '', chapter_dir[0])
            chapter_toc = to_chapter_toc(section_files)
            for section in section_files:
                input_path = os.path.join(chapter_dir[0], section)
                output_name = to_output_name(section)
                output_path = os.path.join(config.output_directory, 'textbook/', output_name)
                title = to_section_title(section)
                self.convert_section(input_path, output_path, title, chapter_toc, chapter_title)

    def convert_section(self, md_path, html_path, title, chapter_toc, chapter_title):
        print title
        output = self.textbook_template
        in_file = codecs.open(md_path, encoding='utf-8')
        out_file = codecs.open(html_path, 'w', encoding='utf-8')
        html = markdown2.markdown(in_file.read())
        output = output.replace('{{title}}', title)
        output = output.replace('{{content}}', html)
        output = output.replace('{{chaptertoc}}', chapter_toc)
        output = output.replace('{{chaptertitle}}', chapter_title)
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

if __name__ == '__main__':
    main()
