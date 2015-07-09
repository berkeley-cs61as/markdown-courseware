"""
<tr class="calendar-lesson-1">
    <td>1</td>
    <td><a href="textbook/lesson-1-intro.html">Functions and Primitive Data</a></td>
    <td><a href="">Discussion 1<br><small><a href="">Section Times</a> &middot; <a href="">Worksheet</a> &middot; <a href="">Solutions</a></small></a></td>
    <td><a href="textbook/homework-1.html">HW 1</a></td>
    <td><a href="http://cs61as-quizzes.com">Quiz 1<br><small><a href="https://drive.google.com/folderview?id=0B237hjxsXjT2cTc3MHBHU1VpdU0&usp=sharing">Practice Quizzes</a></small></a></td>
    <td></td>
</tr>
"""

from collections import OrderedDict

LESSONS = OrderedDict([('0.1', 'Introduction to Scheme and CS61AS'),
                       ('0.2', 'More Practice with Scheme'),
                       ('0.3', 'Recursion and Scheme'),
                       ('1', 'Functions and Primitive Data'),
                       ('2', 'Lambdas and Higher Odrer Funcitons'),
                       ('3', 'Recursion, Iteration, Efficiency'),
                       ('4', 'Data Abstraction and Sequences'),
                       ('5', 'Hierarchical Data and calc.scm'),
                       ('6', 'racket.rkt and Generic Operators'),
                       ('7', 'Object Oriented Programming'),
                       ('8', 'Assignment, State, and Environment'),
                       ('9', 'Mutable Data and Vectors'),
                       ('10', 'Streams'),
                       ('11', 'Metacircular Evaluator'),
                       ('12', 'Analyzing Evaluator and Lazy Evaluator'),
                       ('13', 'Logic Programming'),
                       ('14', 'Concurrency and MapReduce')])

DISCUSSIONS = ['https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7bWltVFNqZmE3cGc/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7ZnhBQ3k2UUI5dHM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7d05XMlpTZGRBTmM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7bmZMV3VPeXFZenc/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7RzBVNXk1aWhZZDg/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7ZWctaEJaV28wZVk/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7c1I5QU5tQTBWVUE/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7MnB6UklxbUI2TUE/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7cjhqTjhuMFp1eUU/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7NzJuLUZGaF90Wlk/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7T2NWZHN6ZE1vWWc/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7MHc0bThYU2VpanM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7UkZDdDhqU3hnSnM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7QjdfaEJ0eXZIYUk/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7MGNFMkhyYndPT2c/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7RGJ1YnlnUHEyRms/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7NXU4V3lLRFNrcmc/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7X3QzUzcxWmVHTW8/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7TTlmSHE1VXFBVWs/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7aUdKU3lUSkZzX0k/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7X2lCNjlxLVJDN3M/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7WHN2VlRJTlVXRGs/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7MEdNc3BCeEpSVEk/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7ZjczUVpRd0JGbFE/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7bDh6cjZkc3B1aWM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7XzdzTy1ZX1BsV00/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7b2NZcFFzeUZwSEE/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7NU13MVg3a1plQlU/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7Uk5HSE10V2ttWFE/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7ZjZjUzJSVXdsQnM/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7QkRhdDdnWWNBbFU/edit?usp\u003ddrive_web', 
               'https://docs.google.com/a/berkeley.edu/file/d/0B2P6EWZ9AYe7WnJsUTBwVXBzTUU/edit?usp\u003ddrive_web']

DISCUSSIONS_ORDER = ['0_2',
                     '0_2_sol',
                     '0_3',
                     '0_3_sol',
                     '1',
                     '10',
                     '10_sol',
                     '11',
                     '11_sol',
                     '12',
                     '12_sol',
                     '13',
                     '13_sol',
                     '1_sol',
                     '2',
                     '2_sol',
                     '3',
                     '3_sol',
                     '4',
                     '4_sol',
                     '5',
                     '5_sol',
                     '6',
                     '6_sol',
                     '7',
                     '7_sol',
                     '8',
                     '8_sol',
                     '9',
                     '9_sol',
                     '14',
                     '14_sol']

for le in LESSONS:
    discussion_url = None 
    try:
        discussion_index = DISCUSSIONS_ORDER.index(le.replace('.', '_'))
        discussion_url, solution_url = DISCUSSIONS[discussion_index], DISCUSSIONS[discussion_index + 1]
    except:
        pass
    print '<tr class="calendar-lesson calendar-lesson-%s">' % le.replace('.', '')
    print '<td>%s</td>' % le
    print '<td><a href="textbook/lesson-%s-intro.html">%s</a></td>' % (le, LESSONS[le])
    if discussion_url:
        print '<td><a href="%s">Discussion %s<br><small>' % (discussion_url, le)
        print '<a href="" class="section-time">Section Times</a> &middot; <a href="%s">Solutions</a>' % solution_url
        print '</small></a></td>'
    else:
        print '<td></td>'
    print '<td><a href="textbook/homework-%s.html">HW %s</a></td>' % (le, le)
    if le == '0.1':
        print '<td rowspan="%d">' % len(LESSONS)
        print '<a href="http://cs61as-quizzes.com">Quiz System</a> /<br> <a href="https://drive.google.com/folderview?id=0B237hjxsXjT2cTc3MHBHU1VpdU0&usp=sharing">Practice Quizzes</a>'
        print '</td>'
        # print '<td><a href="http://cs61as-quizzes.com">Quiz %s</a><br><small><a href="https://drive.google.com/folderview?id=0B237hjxsXjT2cTc3MHBHU1VpdU0&usp=sharing">Practice Quizzes</a></small></a></td>' % le
    else:
        pass
    print '<td></td>'
