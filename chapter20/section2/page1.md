## Takeaways

set-car! and set-cdr! change the respective car and cdr pointers. Procedures
like `cons,` `list` and `append` create new pairs. Knowing which pairs are
shared between different lists is crucial to determining whether mutating one
will influence the other. Drawing box-pointer diagrams will be very helpful.

