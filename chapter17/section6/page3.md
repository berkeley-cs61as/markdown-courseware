## Message and Args

Notice that in the default-method above, we used **message** to find out what
message we passed in to our object. Similarly, we can also use **args** to
find out what other arguments are passed as a list.

Call message args

(ask jack 'do-math 1 2 5 10)

'do-math

(1 2 5 10)

(ask jack 'dance 'salsa)

'dance

'(salsa)

(ask jack 'swim)

'swim

nil

