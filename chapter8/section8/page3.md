_"Wait wait, you just defined a function but it calls other functions that
aren't defined yet! We haven't defined 'good-enough?' or 'improve-guess'! "_

Yup, the definitions of the functions inside  are incomplete but notice that
we (the programmers) can **understand** what the function is doing! We have
broken down the problem of finding 'largest-square' into some small problems
like 'is it close enough?' and 'improve our guess'. We could've broken the
code in a different way, like in every 3 lines, every 5 lines but then each
subproblem will not have an _identifiable_ task. Breaking them to a coherent,
identifiable task is crucial.

This will be a key idea that we will visit again in the end, but first let's
finish the definition.

