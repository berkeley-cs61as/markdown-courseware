## Prefix Notation

You've already been introduced to prefix notation in Unit 0.1, so here's a
quick recap.

In Scheme, we use prefix notation. So, instead of typing in `2 + 3 ` into the
interpreter, we type in `(+ 2 3)` --that is, the [
operator](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/operator/) comes before the operands, or arguments.

This has a few values. The most obvious one right now is that it can take
procedures, such as + or *, that take a variable number of arguments. For
example, in prefix notation, adding 5 numbers would look like `(+ 1 2 3 4 5)`,
while in infix notation, it would look like `1 + 2 + 3 + 4 + 5`.

Another one is that it makes _nesting_ procedures within each other very easy.
For example, `(+ (- 4 3) (/ 4 2))` evaluates to 3. The depth of these
expressions can be arbitrarily extended, so that

`(+ (- (/ 4 2) (+ 3 4 2 (/ 4 3))) (* 4 (- 3 4)))`

is also valid Scheme expression, though one that is very difficult for us
humans to understand.

Another advantage is that it makes _parsing_ Scheme very easy, which comes in
useful when writing an interpreter. If you have no idea what this means yet,
don't worry about it.

Even with the most complicated expressions, the interpreter does the same
thing: it reads the expression, evaluates it, and prints it to the screen.
This is known as the [ read-eval-print loop ](https://edge.edx.org/courses/uc-
berkeley/cs61as-1x/SICP/wiki/cs61as-1x/read-eval-print-loop/).

