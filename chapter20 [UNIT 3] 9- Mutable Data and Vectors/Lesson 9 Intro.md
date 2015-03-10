## set-cdr!

As you might expect, scheme also provides us with `set-cdr!` which takes in a
pair and a value, and changes the pointer of the pair's cdr to point to the
value. Going with the previous example, `(define x (cons 1 2))`, calling
`(set-cdr! x 3)` will change the pair as shown below.

![](/static/lab9-3.png)

The general syntax is `(set-cdr! <pair> <value>)`. We are going to see more
examples for cars and cdrs in the next subsection.

