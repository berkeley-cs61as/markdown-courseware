## Streams Revisited

In section Lesson 11, we showed how to implement streams as delayed lists. We
introduced special forms `delay` and `cons-stream`, which allowed us to
construct a "promise" to compute the `cdr` of a stream, without actually
fulfilling that promise until later. We could use this general technique of
introducing special forms whenever we need more control over the evaluation
process, but this is awkward. For one thing, a special form is not a first-
class object like a procedure, so we cannot use it together with higher-order
procedures. Additionally, we were forced to create streams as a new kind of
data object similar but not identical to lists, and this required us to
reimplement many ordinary list operations (`map`, `append`, and so on) for use
with streams.

