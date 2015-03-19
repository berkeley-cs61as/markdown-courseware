## What is Logic Programming?

At the beginning of this course, we stressed that computer science deals with
imperative (how to) knowledge, whereas mathematics deals with declarative
(what is) knowledge. Indeed, programming languages require that the programmer
express knowledge in a form that indicates the step-by-step methods for
solving particular problems. On the other hand, high-level languages provide,
as part of the language implementation, a substantial amount of methodological
knowledge that frees the user from concern with numerous details of how a
specified computation will progress.

Most programming languages, including Lisp, are organized around computing the
values of mathematical functions. Expression-oriented languages (such as Lisp,
Fortran, and Algol) capitalize on the "pun'' that an expression that describes
the value of a function may also be interpreted as a means of computing that
value. Because of this, most programming languages are strongly biased toward
unidirectional computations (computations with well-defined inputs and
outputs). There are, however, radically different programming languages that
relax this bias. Logic programming extends this idea by combining a relational
vision of programming with a powerful kind of symbolic pattern matching called
unification.

This approach, when it works, can be a very powerful way to write programs.
Part of the power comes from the fact that a single "what is'' fact can be
used to solve a number of different problems that would have different "how
to" components.

## A Sample Database

Before we get into the specifics of logic programming, we need a database to
play with. You can load this database using:

    
       > (load "~cs61as/lib/query.scm")
       > (initialize-data-base microshaft-data-base)
       > (query-driver-loop)
    

The personnel data base for Microshaft contains assertions about company
personnel. Here is the information about Ben Bitdiddle, the resident computer
wizard:

    
    (address (Bitdiddle Ben) (Slumerville (Ridge Road) 10))
    (job (Bitdiddle Ben) (computer wizard))
    (salary (Bitdiddle Ben) 60000)
    

Each assertion is a list (in this case a triple) whose elements can themselves
be lists.

As resident wizard, Ben is in charge of the company's computer division, and
he supervises two programmers and one technician. Here is the information
about them:

    
    (address (Hacker Alyssa P) (Cambridge (Mass Ave) 78))
    (job (Hacker Alyssa P) (computer programmer))
    (salary (Hacker Alyssa P) 40000)
    (supervisor (Hacker Alyssa P) (Bitdiddle Ben))
    (address (Fect Cy D) (Cambridge (Ames Street) 3))
    (job (Fect Cy D) (computer programmer))
    (salary (Fect Cy D) 35000)
    (supervisor (Fect Cy D) (Bitdiddle Ben))
    (address (Tweakit Lem E) (Boston (Bay State Road) 22))
    (job (Tweakit Lem E) (computer technician))
    (salary (Tweakit Lem E) 25000)
    (supervisor (Tweakit Lem E) (Bitdiddle Ben))
    

There is also a programmer trainee, who is supervised by Alyssa:

    
    (address (Reasoner Louis) (Slumerville (Pine Tree Road) 80))
    (job (Reasoner Louis) (computer programmer trainee))
    (salary (Reasoner Louis) 30000)
    (supervisor (Reasoner Louis) (Hacker Alyssa P))
    

All of these people are in the computer division, as indicated by the word
computer as the first item in their job descriptions.

Ben is a high-level employee. His supervisor is the company's big wheel
himself:

    
    (supervisor (Bitdiddle Ben) (Warbucks Oliver))
    (address (Warbucks Oliver) (Swellesley (Top Heap Road)))
    (job (Warbucks Oliver) (administration big wheel))
    (salary (Warbucks Oliver) 150000)
    

Besides the computer division supervised by Ben, the company has an accounting
division, consisting of a chief accountant and his assistant:

    
    (address (Scrooge Eben) (Weston (Shady Lane) 10))
    (job (Scrooge Eben) (accounting chief accountant))
    (salary (Scrooge Eben) 75000)
    (supervisor (Scrooge Eben) (Warbucks Oliver))
    (address (Cratchet Robert) (Allston (N Harvard Street) 16))
    (job (Cratchet Robert) (accounting scrivener))
    (salary (Cratchet Robert) 18000)
    (supervisor (Cratchet Robert) (Scrooge Eben))
    

There is also a secretary for the big wheel:

    
    (address (Aull DeWitt) (Slumerville (Onion Square) 5))
    (job (Aull DeWitt) (administration secretary))
    (salary (Aull DeWitt) 25000)
    (supervisor (Aull DeWitt) (Warbucks Oliver))
    

The data base also contains assertions about which kinds of jobs can be done
by people holding other kinds of jobs. For instance, a computer wizard can do
the jobs of both a computer programmer and a computer technician:

    
    (can-do-job (computer wizard) (computer programmer))
    (can-do-job (computer wizard) (computer technician))
    

A computer programmer could fill in for a trainee:

    
    (can-do-job (computer programmer)
                (computer programmer trainee))
    

Also, as is well known,

    
    (can-do-job (administration secretary)
                (administration big wheel))
    

## Simple Queries

The query language allows users to retrieve information from the data base by
posing queries in response to the system's prompt. For example, to find all
computer programmers one can say

    
    ;;; Query input:
    (job ?x (computer programmer))
    

The system will respond with the following items:

    
    ;;; Query results:
    (job (Hacker Alyssa P) (computer programmer))
    (job (Fect Cy D) (computer programmer))
    

The input query specifies that we are looking for entries in the data base
that match a certain pattern. In this example, the pattern specifies entries
consisting of three items, of which the first is the literal symbol job, the
second can be anything, and the third is the literal list (computer
programmer). The "anything" that can be the second item in the matching list
is specified by a pattern variable, `?x`. The general form of a pattern
variable is a symbol, taken to be the name of the variable, preceded by a
question mark. We will see below why it is useful to specify names for pattern
variables rather than just putting ? into patterns to represent "anything."
The system responds to a simple query by showing all entries in the data base
that match the specified pattern.

A pattern can have more than one variable. For example, the query

    
    (address ?x ?y)
    

will list all the employees' addresses.

A pattern can have no variables, in which case the query simply determines
whether that pattern is an entry in the data base. If so, there will be one
match; if not, there will be no matches.

The same pattern variable can appear more than once in a query, specifying
that the same "anything'' must appear in each position. This is why variables
have names. For example,

    
    (supervisor ?x ?x)
    

finds all people who supervise themselves (though there are no such assertions
in our sample data base).

The query

    
    (job ?x (computer ?type))
    

matches all job entries whose third item is a two-element list whose first
item is computer:

    
    (job (Bitdiddle Ben) (computer wizard))
    (job (Hacker Alyssa P) (computer programmer))
    (job (Fect Cy D) (computer programmer))
    (job (Tweakit Lem E) (computer technician))
    

This same pattern does not match

    
    (job (Reasoner Louis) (computer programmer trainee))
    

because the third item in the entry is a list of three elements, and the
pattern's third item specifies that there should be two elements. If we wanted
to change the pattern so that the third item could be any list beginning with
computer, we could specify

    
    (job ?x (computer . ?type))
    

For example,

    
    (computer . ?type)
    

matches the data

    
    (computer programmer trainee)
    

with `?type` as the list (programmer trainee). It also matches the data

    
    (computer programmer)
    

with `?type` as the list (programmer), and matches the data

    
    (computer)
    

with `?type` as the empty list` ()`.

We can describe the query language's processing of simple queries as follows:

  * The system finds all assignments to variables in the query pattern that satisfy the pattern -- that is, all sets of values for the variables such that if the pattern variables are instantiated with (replaced by) the values, the result is in the data base.
  * The system responds to the query by listing all instantiations of the query pattern with the variable assignments that satisfy it.

Note that if the pattern has no variables, the query reduces to a
determination of whether that pattern is in the data base. If so, the empty
assignment, which assigns no values to variables, satisfies that pattern for
that data base.

## Compound Queries

Simple queries form the primitive operations of the query language. In order
to form compound operations, the query language provides means of combination.
One thing that makes the query language a logic programming language is that
the means of combination mirror the means of combination used in forming
logical expressions: and, or, and not. (Here and, or, and not are not the Lisp
primitives, but rather operations built into the query language.)

We can use and as follows to find the addresses of all the computer
programmers:

    
    (and (job ?person (computer programmer))
         (address ?person ?where))
    

The resulting output is

    
    (and (job (Hacker Alyssa P) (computer programmer))
         (address (Hacker Alyssa P) (Cambridge (Mass Ave) 78)))
    (and (job (Fect Cy D) (computer programmer))
         (address (Fect Cy D) (Cambridge (Ames Street) 3)))
    

In general,

    
    (and <query1> <query2> ... <queryn>)
    

is satisfied by all sets of values for the pattern variables that
simultaneously satisfy <query1> <query2> ... <queryn>

As for simple queries, the system processes a compound query by finding all
assignments to the pattern variables that satisfy the query, then displaying
instantiations of the query with those values.

Another means of constructing compound queries is through or. For example,

    
    
    (or (supervisor ?x (Bitdiddle Ben))
        (supervisor ?x (Hacker Alyssa P)))
    

will find all employees supervised by Ben Bitdiddle or Alyssa P. Hacker:

    
    
    (or (supervisor (Hacker Alyssa P) (Bitdiddle Ben))
        (supervisor (Hacker Alyssa P) (Hacker Alyssa P)))
    
    (or (supervisor (Fect Cy D) (Bitdiddle Ben)) 
        (supervisor (Fect Cy D) (Hacker Alyssa P)))
    
    (or (supervisor (Tweakit Lem E) (Bitdiddle Ben))     
        (supervisor (Tweakit Lem E) (Hacker Alyssa P))) 
    
    (or (supervisor (Reasoner Louis) (Bitdiddle Ben)) 
        (supervisor (Reasoner Louis) (Hacker Alyssa P)))
    

In general,

    
    
    (or <query1> <query2> ... <queryn> )
    

is satisfied by all sets of values for the pattern variables that satisfy at
least one of <query1> <query2> ... <queryn>.

Compound queries can also be formed with `not`. For example,

    
    
    (and (supervisor ?x (Bitdiddle Ben))
         (not (job ?x (computer programmer))))
    

finds all people supervised by Ben Bitdiddle who are not computer programmers.
In general,

    
    
    (not <query1>)
    

is satisfied by all assignments to the pattern variables that do not satisfy
<query1>.

The final combining form is called `lisp-value`. When `lisp-value` is the
first element of a pattern, it specifies that the next element is a Lisp
predicate to be applied to the rest of the (instantiated) elements as
arguments. In general,

    
    
    (lisp-value <predicate> <arg1> ... <argn>)
    

will be satisfied by assignments to the pattern variables for which the
<predicate> applied to the instantiated <arg1> ... <argn> is true. For
example, to find all people whose salary is greater than $30,000 we could
write

    
    
    (and (salary ?person ?amount)
         (lisp-value > ?amount 30000))
    
    
    
    

## Rules

As long as we just tell the system isolated facts, we can’t get
extraordinarily interesting replies. But we can also tell it _rules_ that
allow it to infer one fact from another. For example, if we have a lot of
facts like:

    
    
    (mother Eve Cain)
    

then we can establish a rule about grandmotherhood:

    
    
    (assert! (rule (grandmother ?elder ?younger)
                   (and (mother ?elder ?mom)
                        (mother ?mom ?younger) ))))
    

The rule says that the ﬁrst part (the conclusion) is true _if_ we can ﬁnd
values for the variables such that the second part (the condition) is true.

Again, resist the temptation to try to do composition of functions!

    
    
    (assert! (rule (grandmother ?elder ?younger) ;; WRONG!!!!
                   (mother ?elder (mother ?younger)) ))
    

`Mother` isn’t a function, and you can’t ask for the mother of someone as this
incorrect example tries to do. Instead, as in the correct version above, you
have to establish a variable (`?mom`) that has a value that satisﬁes the two
motherhood relationships we need.

In this language the words `assert!, rule, and, or`, and `not` have special
meanings. Everything else is just a word that can be part of assertions or
rules.

## More Rules

Here's a slightly more complicated rule:

    
    
    (rule (lives-near ?person-1 ?person-2)
          (and (address ?person-1 (?town . ?rest-1))
               (address ?person-2 (?town . ?rest-2))
               (not (same ?person-1 ?person-2))))
    

It specifies that two people live near each other if they live in the same
town. The final `not` clause prevents the rule from saying that all people
live near themselves. The `same` relation is defined by the very simple rule:

    
    
    (rule (same ?x ?x))
    

## Logic as Programs

We can regard a rule as a kind of logical implication: _If_ an assignment of
values to pattern variables satisfies the body, _then_ it satisfies the
conclusion. Consequently, we can regard the query language as having the
ability to perform _logical deductions_ based upon the rules. As an example,
consider the `append` operation. A`ppend` can be characterized by the
following two rules:

  * For any list` y`, the empty list and` y` append to form` y.`
  * For any `u, v, y, and z`,` (cons u v)` and` y` append to form` (cons u z)` if `v` and `y` append to form `z`.

To express this in our query language, we define two rules for a relation

    
    (append x y z)
    

which we can interpret to mean "x and y append to form z":

    
    (assert! (rule (append () ?y ?y)))
    (assert! (rule (append (?u . ?v) ?y (?u . ?z))
             (append ?v ?y ?z)))
    

The first rule has no body, which means that the conclusion holds for any
value of `?y`. Note how the second rule makes use of dotted-tail notation to
name the car and cdr of a list.

Given these two rules, we can formulate queries that compute the append of two
lists:

    
    ;;; Query input:
    (append (a b) (c d) ?what)
    ;;; Query results:
    (append (a b) (c d) (a b c d))
    

What is more striking, we can use the same rules to ask the question "Which
list, when appended to `(a b)`, yields` (a b c d)`?" This is done as follows:

    
    ;;; Query input:
    (append (a b) ?what (a b c d))
    ;;; Query results:
    (append (a b) (c d) (a b c d))
    

The new thing in logic programming is that we can run a "function" backwards!
We can tell it the answer and get back the question. But the real magic is...

    
    ;;; Query input:
    (append ?this ?that (a b c d))
    ;;; Query results:
    (append () (a b c d) (a b c d))
    (append (a) (b c d) (a b c d))
    (append (a b) (c d) (a b c d))
    (append (a b c) (d) (a b c d))
    (append (a b c d) () (a b c d))
    

we can also ask for all pairs of lists that append to form `(a b c d)`! We can
use logic programming to compute multiple answers to the same question!
Somehow it found all the possible combinations of values that would make our
query true.

How does the append program work? Compare it to the Scheme append:

    
    (define (append a b)
        (if (null? a)
            b
            (cons (car a) (append (cdr a) b)) ))
    

Like the Scheme program, the logic program has two cases: There is a base case
in which the ﬁrst argument is empty. In that case the combined list is the
same as the second appended list. And there is a recursive case in which we
divide the ﬁrst appended list into its car and its cdr. We reduce the given
problem into a problem about appending `(cdr a)` to `b`. The logic program is
diﬀerent in form, but it says the same thing.

(Just as, in the grandmother example, we had to give the mother a name instead
of using a function call, here we have to give` (car a)` a name--we call it
`?u`.)

## Word of Caution

The query system may seem to exhibit quite a bit of intelligence in using the
rules to deduce the answers to the queries above. Actually, as we will see in
the next section, the system is following a well-determined algorithm in
unraveling the rules. Unfortunately, although the system works impressively in
the append case, the general methods may break down in more complex cases.

The "working backward" magic used in the append case doesn't always work.
Let's look at the following example, which reverses a list.

    
    (assert! (rule (reverse (?a . ?x) ?y)
                   (and (reverse ?x ?z)
                        (append ?z (?a) ?y) )))
    
    (assert! (reverse () ()))
    

This works for `(reverse (a b c) ?what)` but not the other way around; it gets
into an inﬁnite loop. We can also write a version that works only backwards:

    
    (assert! (rule (backward (?a . ?x) ?y)
                   (and (append ?z (?a) ?y)
                        (backward ?x ?z) )))
    
    (assert! (backward () ()))
    

But it's much harder to write one that works both ways. Even as we speak,
logic programming fans are trying to push the limits of the idea, but right
now, you still have to understand something about the below-the-line algorithm
to be conﬁdent that your logic program won't loop.

## takeaways

Here are some takeaways from this subsection:

  * In logic programming, we assert facts and ask questions.
  * An assertion is represented by a list.
  * We use the query language to retrieve information from the data base.
  * Rules allow infering one fact from another.
  * We can write programs such as `append` with logic programming!

## what's next?

Go to the next subsection and learn how the query system works!

