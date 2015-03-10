## what is logo?

For Project 4, you are going to write an interpreter for a language called
Logo. In order to do that, you should know its basics.

Logo is a dialect of Lisp, just as Scheme is, but its design has diﬀerent
priorities. The goal was to make it as natural-seeming as possible for kids,
so it's syntax is pretty different from Scheme. For example, there are no
parentheses (do you like it?).

To begin, first ssh into star (`ssh cs61as-xx@star.cs.berkeley.edu`). Then
type `logo` at the terminal -- not in Scheme! You should see something like
this:

    
    Welcome to Berkeley Logo version 5.5
    ?
    

The question mark is the Logo prompt, like the `>` in Scheme. (Later, in some
of the examples below, you'll see a `>` prompt from Logo, while in the middle
of defining a procedure.)

## rules of logo

  * **Commands and operations**: In Scheme, every procedure returns a value, even the ones for which the value is unspeciﬁed and/or useless, like define and print. In Logo, procedures are divided into operations, which return values, and commands, which don't return values but are called for their effect. You have to start each instruction with a command:   
`print sum 2 3`

  * **Syntax**: If parentheses aren't used to delimit function calls, how do you know the difference between a function and an argument? When a symbol is used without punctuation, that means a function call. When you want the value of a variable to use as an argument, you put a colon in front of it: 
    
    make "x 14
    print :x
    print sum :x :x
    

  * **Words**: They are quoted just as in Scheme, except that the double-quote character is used instead of single-quote. But since expressions aren't represented as lists, the same punctuation that delimits a list also quotes it:   
```print [a b c]```

Parentheses can be used, as in Scheme, if you want to give extra arguments to
something, or indicate inﬁx precedence:

    
    print (sum 2 3 4 5)
    print 3*(4+5)
    

  * **No special forms**: Except `to`, the thing that defines a new procedure, all Logo primitives evaluate their arguments. How is this possible? We "proved" back in chapter 1 that `if` has to be a special form. But instead we just quote the arguments to `ifelse`: 
    
    ifelse 2=3 [print "hi] [print "bye] 
    

You don't notice the quoting since you get it for free with the list grouping.

  * **Functions not ﬁrst class**: In Logo every function has a name; there's no `lambda`. Also, the namespace for functions is separate from the one for variables; a variable can't have a function as its value. (This is convenient because we can use things like `list` or `sentence` as formal parameters without losing the functions by those names.) That's another reason why you need colons for variables.
  * **Higher-order functions**: There are two ways to write higher-order functions. First, you can use the name of a function as an argument, and you can use that name to construct an expression and eval it with `run`. Second, Logo has ﬁrst-class expressions; you can `run` a list that you get as an argument: 
    
    print map "first [the rain in spain] 
    print map [? * ?] [3 4 5 6]
    

## try it out!

Type each of the following instruction lines and note the results. (A few of
them will give error messages.) If you can't make sense of a result, ask for
help.

    
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

## takeaways

In this subsection, you learned what Logo is and the differences between Logo
and Scheme. For a more detailed read about the metacircular evaluator,
[here](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html) is the
SICP.

## what's next?

Go do your homework! You should also start on Project 4.

