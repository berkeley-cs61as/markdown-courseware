## Compound Expressions

So how does our calculator program evaluates compound expressions? It calls
`calc-eval` on simpler expressions, and recursively repeats this until the
expressions are simple enough (just numbers). We know that `calc-eval` and
`calc-apply` works for numbers, and expressions with one operators. Everything
else is just a combination. Trust the recursion!

