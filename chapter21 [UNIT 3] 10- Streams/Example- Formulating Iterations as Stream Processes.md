In unit 1, you used the following formula to approximate pi:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-41.gif)

Now, let's calculate pi with an infinite stream:

`(define (pi-summands n)`

`(cons-stream (/ 1.0 n)`

`(stream-map - (pi-summands (+ n 2)))))`

`(define pi-stream`

`(scale-stream (partial-sums (pi-summands 1)) 4))`

The first few elements look like this:

4.

2.666666666666667

3.466666666666667

2.8952380952380956

3.3396825396825403

2.9760461760461765

3.2837384837384844

3.017071817071818

As you can tell, the numbers are converging on pi--after looking at the first
8 elements, we know pi is somewhere between 3.28 and 3.02.

