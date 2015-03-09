## Predicate and Style

A predicate is any expression that returns true or false. Some examples
include `(< 3 4)`,` (> 10 -2)`, `(= 'apple 'orange)`. You can form compound
predicates by using ` and, or, not. `

Here is an example of a predicate:

`(define (even? x) (= (remainder x 2) 0))`

The convention in scheme when defining your own predicate is to end the name
with '?'.

Notice that the following code is equivalent:

`(define (even? x) (if (= (remainder x 2) 0)`

` #t`

` #f))`

The second code however, is considered to be a 'bad programming style' because
of its redundancy. We urge you to avoid codes like this because verytime you
do, a penguin will cry.

![](http://farm3.static.flickr.com/2600/3829466121_0e5c9b6cca.jpg)

