## Exercise 1.

  
List all the procedures in the metacircular evaluator that call `mc-eval`.

## Exercise 2.

  
List all the procedures in the metacircular evaluator that call `mc-apply`.

## Exercise 3.

  
Explain why `make-procedure` does not call `mc-eval`.

## A Note on Homework 11

Some students have complained that this week's homework is very time-
consuming.

Accordingly, with some reluctance, we've marked a few exercises as optional;
these are the ones to leave out if you're really pressed for time. But it's
much better if you do all of them!

The optional ones have * next to them.

## Template

You can copy the template for this homework by typing the following in your
terminal:

    
      cp ~cs61as/autograder/templates/hw11.rkt .
    

Or, you can download it
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw11.rkt).

## Exercise 1.

  
Abelson & Sussman, exercises [4.3, 4.6, 4.7*,
4.10*](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.3), [4.11*,
4.13](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.11), [4.14](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-26.html#%_thm_4.14), and
[4.15](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.15).

## Exercise 4.

  
Abelson & Sussman, exercises [4.1](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.1), [4.2, 4.4, and
4.5](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html#%_thm_4.2).

## Exercise 5.

In this lab exercise you will become familiar with the Logo programming
language, for which you'll be writing an interpreter in project 4.

To begin, type

logo

at the Unix shell prompt - **not** from Scheme! You should see something like
this:

    
    Welcome to Berkeley Logo version 5.5
    ?

The question mark is the Logo prompt, like the > in Scheme. (Later, in some of
the examples below, you'll see a > prompt from Logo, while in the middle of
defining a procedure.)

    * Type each of the following instruction lines and note the results. (A few of them will give error messages.) If you can't make sense of a result, ask for help.
    
    
    print 2 + 3
    
    print 2+3
    
    print sum 2 3
    
    print (sum 2 3 4 5)
    
    print sum 2 3 4 5
    
    2+3
    
    print "yesterday
    
    print "julia"
    
    print revolution
    
    print [blue jay way]
    
    show [eight days a week]
    
    show first [golden slumbers]
    
    print first bf [she loves you]
    
    pr first first bf [yellow submarine]
    
    to second :stuff
    output first bf :stuff
    end
    
    second "something
    
    print second "piggies
    
    pr second [another girl]
    
    pr first second [carry that weight]
    pr second second [i dig a pony]
    
    to pr2nd :thing
    print first bf :thing
    end
    
    pr2nd [the 1 after 909]
    
    print first pr2nd [hey jude]
    
    repeat 5 [print [this boy]]
    
    if 3 = 1+1 [print [the fool on the hill]]
    
    print ifelse 2=1+1 ~
    [second [your mother should know]] ~
    [first "help]
    
    print ifelse 3=1+2 ~
    [strawberry fields forever] ~
    [penny lane]
    
    print ifelse 4=1+2 ~
    ["flying] ~
    [[all you need is love]]
    
    to greet :person
    say [how are you,]
    end
    
    to say :saying
    print sentence :saying :person
    end
    
    greet "ringo
    
    show map "first [paperback writer]
    
    show map [word first ? last ?] ~
    [lucy in the sky with diamonds]
    
    to who :sent
    foreach [pete roger john keith] "describe
    end
    
    to describe :person
    print se :person :sent
    end
    
    who [sells out]
    
    print :bass
    
    make "bass "paul
    
    print :bass
    
    print bass
    
    to bass
    output [johnny cymbal]
    end
    
    print bass
    
    print :bass
    
    print "bass
    
    to countdown :num
    if :num=0 [print "blastoff stop]
    print :num
    countdown :num-1
    end
    
    countdown 5
    
    to downup :word
    print :word
    if emptyp bl :word [stop]
    downup bl :word
    print :word
    end
    
    downup "rain
    
    ;;;; The following stuff will work
    ;;;; only on an X workstation:
    
    cs
    
    repeat 4 [forward 100 rt 90]
    
    cs
    
    repeat 10 [repeat 5 [fd 150 rt 144] rt 36]
    
    cs repeat 36 [repeat 4 [fd 100 rt 90]
                 setpc remainder pencolor+1 8
                 rt 10]
    
    to tree :size
    if :size < 3 [stop]
    fd :size/2
    lt 30 tree :size*3/4 rt 30
    fd :size/3
    rt 45 tree :size*2/3 lt 45
    fd :size/6
    bk :size
    end
    
    cs pu bk 100 pd ht tree 100
    

    * Devise an example that demonstrates that Logo uses dynamic scope rather than lexical scope. Your example should involve the use of a variable that would have a different value if Logo used lexical scope. Test your code with Berkeley Logo.

    * Explain the differences and similarities among the Logo operators " (double-quote), [ ] (square brackets), and : (colon).

## Exercise 2*.

  
Modify the metacircular evaluator to allow type-checking of arguments to
procedures. Here is how the feature should work. When a new procedure is
defined, a formal parameter can be either a symbol as usual or else a list of
two elements. In this case, the second element is a symbol, the name of the
formal parameter. The first element is an expression whose value is a
predicate function that the argument must satisfy. That function should return
`#t` if the argument is valid. For example, here is a procedure foo that has
typechecked parameters num and list:

`> (define (foo (integer? num) ((lambda (x) (not (null? x))) lst))`

` (list-ref lst num))`

` > (foo 3 '(a b c d e))`

` d`

` > (foo 3.5 '(a b c d e))`

` Error: wrong argument type -- 3.5`

` > (foo 2 '())`

` Error: wrong argument type -- () `

In this example we define a procedure `foo` with two formal parameters, named
`num` and `list`. When `foo` is invoked, the evaluator will check to see that
the first actual argument is an integer and that the second actual argument is
not empty. The expression whose value is the desired predicate function should
be evaluated with respect to `foo`'s defining environment. (Hint: Think about
extend-environment.)

## Extra for Experts

### Do this if you want to. This is NOT for credit.

## Exercise 3.

  
Abelson & Sussman, exercises [4.16 - 4.21](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.16).

# **DO NOT FORGET TO SUBMIT YOUR HOMEWORK!**

