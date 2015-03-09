## Starting the Project

Okay, time for the actual project. You will need these files:

`~cs61as/lib/obj.scm ` object-oriented tools

`~cs61as/lib/logo.scm ` various stuff Logo needs

`~cs61as/lib/logo-meta.scm ` modified metacircular evaluator

You will only be modifying `logo.scm` and `logo-meta.scm`

These files (or your modified versions of the last two) must be loaded into
Scheme in this order; each one depends on the one before it. Much of the work
has already been done for you. (The names logo-eval and logo-apply are used so
as not to conflict with Scheme's built-in eval and apply functions.)

For reference, `~cs61as/lib/mceval.scm `is the metacircular evaluator without
the modifications for Logo.

Start by examining logo-eval. It has two parts: `eval-prefix`, which is
comparable to the version of `eval` in the text, handles expressions with
prefix operations similar to Scheme's syntax. The result of evaluating such an
expression is then given as an argument to `handle-infix`, which checks for a
possible infix operator following the expression. For now, we'll ignore
`handle-infix`, which you'll write later in the project, and concentrate on
`eval-prefix`. Compare it with the version of eval in the text. The Scheme
version has a COND clause for each of several special forms. (And the real
Scheme has even more special forms than the version in the book.) Logo has
only one special form, used for procedure definition, but to make up for it,
eval-prefix has a lot of complexity concerning parentheses. An ordinary
application (handled by the else clause) is somewhat more complicated than in
Scheme because we must figure out the number of arguments required before we
can collect the arguments. Finally, an important subtle point is that the Logo
version uses LET in several places to enforce a left-to-right order of
evaluation. In Scheme the order of evaluation is unspecified, but in Logo we
don't know where the second argument expression starts, for example, until
we've finished collecting and evaluating the first argument expression.

