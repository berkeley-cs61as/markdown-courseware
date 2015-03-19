from publish import *

def assertEquals(expected, actual):
    if expected != actual:
        print 'Test failed: expected %s but got %s' % (str(expected), str(actual))

assertEquals([], parse_range(''))
assertEquals([1], parse_range('1'))
assertEquals([1, 2, 3], parse_range('1, 2-3'))
assertEquals([1, 2, 3, 4], parse_range('1, 2-3, 4'))
assertEquals([1, 2, 3, 5, 6, 7], parse_range('1, 2-3, 5-7'))

assertEquals('hello-my-name-is-bob.html', to_output_name('section01 Hello - My, Name, is Bob.md'))
assertEquals('mason-dixon-line.html', to_output_name('section13 Mason-Dixon (Line).md'))
