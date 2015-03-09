## The 'self' Keyword

What should `write-check` do? It should reduce the account's balance by the
specified amount and additional fee. We already know how to reduce our
balance, it's just the `withdraw` method! To call a method that we already
defined from the body of another method, we use the **self**, hence the `(ask
self 'withdraw (+ amount 0.10))`. Each ob ject has a local state variable
`self` whose value is the object itself.

