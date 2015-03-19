
output_directory = '../berkeley-cs61as.github.io/'

# List of tuples. Each tuple represents a unit.
# The first item in the tuple is the name of the unit.
# The second item is a range of numbers indicating the chapters
# in that tuple. The range must be something like this: "1, 2-4, 6, 7."
# Note that ranges indicated with a dash are inclusive-inclusive.
# Also, make sure every comma is followed by a space.
units = [('Setup', '1-3'),
         ('Unit 0', '4, 6-7'),
         ('Unit 1', '8-9, 11-12'),
         ('Unit 2', '13-16'),
         ('Unit 3', '17-21'),
         ('Unit 4', '22-27')]

pages = [('Home','pages/index.md'),
         ('Textbook','pages/textbook.md'),
         ('Syllabus','pages/syllabus.md'),
         ('FAQ','pages/faq.md'),
         ('Staff','pages/staff.md'),
         ('Resources','pages/resources.md')]

textbook_html_template = 'templates/textbook-template.html'

page_html_template = 'templates/page-template.html'
