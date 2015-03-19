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
    title = re.sub(':', ' -', title)
    title = re.sub('/', '-', title)
    return title

def convert_chapter(path, output_dir):
    title = read_title(path)
    title = re.sub('\[.*?\]', '', title).strip()
    for i, path in enumerate(read_child_urls(path)):
        make_directory(OUTPUT_ROOT + output_dir + title)
        convert_sequential('sequential/' + path, output_dir + title + '/section%02d ' % (i + 1))

def convert_sequential(path, output_dir):
    title = read_title(path).strip()
    output_file = codecs.open(OUTPUT_ROOT + output_dir + title + '.md', 'w', encoding='utf-8')
    markdown = ''
    for path in read_child_urls(path):
        markdown += convert_vertical('vertical/' + path)
    output_file.write(markdown)
    output_file.close()    

def convert_vertical(path):
    output = ''
    for path in read_child_urls(path):
        try:
            html_file = codecs.open(DUMP_ROOT + 'html/' + path + '.html', encoding='utf-8')
            markdown = html_to_markdown(html_file.read())
            output += markdown
        except Exception as e:
            print e
    return output

def main():
    os.system('rm -rf ./chapter*')
    chapter_paths = read_child_urls(MANIFEST)
    for i, path in enumerate(chapter_paths):
        convert_chapter('chapter/' + path, 'chapter%02d ' % (i + 1))

if __name__ == '__main__':
    main()