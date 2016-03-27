#!/usr/bin/env python

"""
config.py
Allen Guo <allenguo@berkeley.edu>
Specifies configurable settings for publish.py.
"""

github_url = 'https://github.com/berkeley-cs61as/markdown-courseware/tree/master/'

output_directory = '../berkeley-cs61as.github.io/'

# List of tuples. Each tuple represents a unit.
# The first item in the tuple is the name of the unit.
# The second item is a range of numbers indicating the chapters
# in that tuple. The range must be something like this: "1, 2-4, 6, 7."
# Note that ranges indicated with a dash are inclusive-inclusive.
units = [('Unit 0', '4, 6-7'),
         ('Unit 1', '8-9, 11-12'),
         ('Unit 2', '13-16'),
         ('Unit 3', '17-21'),
         ('Unit 4', '22,23,28,26-27')]

# List of tuples. Each tuple represents a (non-textbook) page.
# The first item in the tuple is the name of the page.
# The second item is the file path (relative to publish.py).
# This can either be a Markdown file or HTML file.
# The third item is the template to use with page.
pages = [('Table of Contents', 'pages/textbook.html', 'basic'),
         ('Submitting Assignments', 'pages/submit.md', 'page-toc')]

# publish.py generates a warning if a section title exceeds this.
section_title_max_length = 48

# publish.py generates an HTML table of contents for the entire textbook.
# It is printed to this file.
# Set to None to disable.
# toc_path = 'toc.html'
toc_path = None
