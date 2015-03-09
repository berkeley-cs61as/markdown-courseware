"""
Converts edX dump to Markdown files.

Author: Allen Guo <allenguo@berkeley.edu>
"""

import os
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

def convert_chapter(path, output_path):
    for i, path in enumerate(read_child_urls(path)):
        convert_sequential('sequential/' + path, output_path + 'section%d/' % (i + 1))

def convert_sequential(path, output_path):
    for path in read_child_urls(path):
        convert_vertical('vertical/' + path, output_path)

def convert_vertical(path, output_path):
    for i, path in enumerate(read_child_urls(path)):
        try:
            make_directory(OUTPUT_ROOT + output_path)
            html_file = open(DUMP_ROOT + 'html/' + path + '.html')
            markdown = html_to_markdown(html_file.read())
            output_file = open(OUTPUT_ROOT + output_path + 'page%d.md' % (i + 1), 'w')
            output_file.write(markdown)
        except:
            pass

def main():
    chapter_paths = read_child_urls(MANIFEST)
    for i, path in enumerate(chapter_paths):
        convert_chapter('chapter/' + path, 'chapter%d/' % (i + 1))

if __name__ == '__main__':
    main()                