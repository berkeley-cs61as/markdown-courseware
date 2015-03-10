"""
Converts edX dump to Markdown files.

Author: Allen Guo <allenguo@berkeley.edu>
"""

import codecs, os, re
import html2text
import xml.etree.ElementTree as ET

DUMP_ROOT = 'C:/Users/Allen/Downloads/course/'
OUTPUT_ROOT = 'C:/Users/Allen/Documents/GitHub/markdown-courseware/'

MANIFEST = 'course/course.xml'

def html_to_markdown(html):
    return html2text.html2text(html)

def make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_xml(path):
    if os.name == 'nt':
        path = path.replace('/', '\\')  # Windows only!
    path = DUMP_ROOT + path
    if '.xml' != path[-4:]:
        path += '.xml'
    return ET.parse(path).getroot()

def read_child_urls(path):
    xml = read_xml(path)
    for child in xml:
        if 'url_name' in child.attrib:
            yield child.attrib['url_name']

def read_title(path):
    xml = read_xml(path)
    title = xml.attrib['display_name'] if 'display_name' in xml.attrib else 'Untitled'
    title = re.sub('\?', '', title)
    title = re.sub('[/:]', '-', title)
    return title

def convert_chapter(path, output_dir):
    title = read_title(path)
    for i, path in enumerate(read_child_urls(path)):
        convert_sequential('sequential/' + path, output_dir + title + '/')

def convert_sequential(path, output_dir):
    title = read_title(path)
    for i, path in enumerate(read_child_urls(path)):
        convert_vertical('vertical/' + path, output_dir + '%s.md' % title, output_dir)

def convert_vertical(path, output_path, output_dir):
    make_directory(OUTPUT_ROOT + output_dir)
    output_file = codecs.open(OUTPUT_ROOT + output_path, 'w', encoding='utf-8')
    for path in read_child_urls(path):
        try:
            html_file = codecs.open(DUMP_ROOT + 'html/' + path + '.html', encoding='utf-8')
            markdown = html_to_markdown(html_file.read())
            output_file.write(markdown)
        except Exception as e:
            print e

def main():
    os.system('rm -rf ./chapter*')
    chapter_paths = read_child_urls(MANIFEST)
    for i, path in enumerate(chapter_paths):
        convert_chapter('chapter/' + path, 'chapter%d ' % (i + 1))

if __name__ == '__main__':
    main()