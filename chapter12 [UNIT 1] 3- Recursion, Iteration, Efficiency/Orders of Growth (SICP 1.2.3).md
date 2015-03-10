## Recursive Processes

The following `reverse` function generates a recursive process:

    
            
              (define (reverse sent)
                (if (empty? sent)
                    '()
                    (se (last sent) (reverse (bl sent)))))
            
          

The running time for this function is \( 5N + 2 \) since it has five constant-
runtime operations: `if, empty?, se, last`, and `bl`. Thus the order of growth
of its running time is \( \Theta(n) \).

Now assume that we call `reverse` with an argument `'(Today was a fairytale)`.

The function call `(reverse '(Today was a fairytale))` will then generate the
following processes:

    
    
          (se fairytale (reverse '(Today was a)))
          (se a (reverse '(Today was)))
          (se was (reverse '(Today)))
          (se Today (reverse '()))
          (se Today '())
          (se was '(Today))
          (se a '(was Today))
          (se fairytale '(a was Today))
          '(fairytale a was Today)

One problem with this recursive process is that it takes too much memory.
Along the process, scheme has to keep track of the pending computations: In
order to accomplish `(se fairytale (reverse '(Today was a)))`, it has to
reserve some memory for the unfinished task `(reverse '(Today was a)).
`Similarly, memory has to be reserved for` (reverse '(Today was)), (reverse
'(Today)),` and `(reverse '())`. Therefore, this function is \( \Theta(n) \)
in memory.

## Iterative Process

Now let's consider another function that does the same thing in a different
way:

    
          (define (reverse-iter sent)
            (define (reverse-helper result se)
              (if (empty? se)
                  result
                  (reverse-helper (se result (last se)) (bl se))))
            (reverse-helper '() sent))

We can see that its runtime has the same order of growth as the recursive
reverse function.

If we call reverse-iter with `'(Today was a fairytale)`:

    
    
          (reverse-helper '() '(Today was a fairytale))
          (reverse-helper '(fairytale) '(Today was a))
          (reverse-helper '(fairytale a) '(Today was))
          (reverse-helper '(fairytale a was) '(Today))
          (reverse-helper '(fairytale a was Today) '())
          Returns '(fairytale a was Today)

Notice that both `reverse` functions use recursion. The difference is that, in
the first version, when the recursive procedure reaches the base case, it
doesn't finish all the work yet; in the second version, that particular
subproblem is solved when the recursive calls reach the base case. The first
function generates a recursive process, while the second one generates an
iterative process.

Another important point about this recursive process is that: since each
`reverse-helper` call does not have unfinished tasks, it takes constant memory
space.

In fact, iterative process always takes constant memory space because each
recursive call always contains **all the information necessary to complete the
computation**.

