## A Clarification on DDP

Don't get the idea that DDP just means a two-dimensional table of operator and
type names! DDP is a very general, great idea. It means putting the details of
a system into data, rather than into programs, so you can write general
programs instead of very speciﬁc ones.

In the old days, every time a company got a computer they had to hire a bunch
of programmers to write things like payroll programs for them. They couldn't
just use someone else's program because the details would be different, e.g.,
how many digits in the employee number. These days you have general business
packages and each company can "tune" the program to their speciﬁc purpose with
a data ﬁle.

Another example showing the generality of DDP is the compiler. It used to be
that if you wanted to invent a new programming language you had to start from
scratch in writing a compiler for it. But now we have formal notations for
expressing the syntax of the language. (See section 7.1, page 38, of the
Scheme Report at the back of the course reader.) A single program can read
these formal descriptions and compile any language.

