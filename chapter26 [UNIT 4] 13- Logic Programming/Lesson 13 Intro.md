## Logic Programming

  
Logic programming excels in providing interfaces to data bases for information
retrieval. The query language we shall use in this chapter is designed to be
used in this way.

All we do is assert facts:

    
    > (load "~cs61as/lib/query.scm")
    > (query)
    
    ;;; Query input:
    (assert! (Brian likes potstickers))
    

and ask questions about the facts:

    
    ;;; Query input:
    (?who likes potstickers)
    
    ;;; Query results:
    (BRIAN LIKES POTSTICKERS)
    

Although the assertions and the queries take the form of lists, and so they
look a little like Scheme programs, they're not! There is no application of
function to argument here; an assertion is just data.

This is true even though, for various reasons, it's traditional to put the
verb (the relation) ﬁrst:

    
    (assert! (likes Brian potstickers))
    

We'll use that convention hereafter, but that makes it even easier to fall
into the trap of thinking there is a function called `likes`. Read on to learn
how we program in this peculiar language!

