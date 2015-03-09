## Scope of Variables

(define (largest-square total guess)

    
    	(define (next-guess guess) (+ guess 1))
    	(define (good-enough? total guess)
    		(< total (square (next-guess guess))))
    	(if (good-enough? guess)
    		guess
    		(largest-square total (next-guess guess))))
    

Previously we mentioned that the functions `good-enough?` and `next-guess` are
defined only inside the function `largest-square. ` Now that those functions
are inside `largest-square`, we can take other redundant parts out of the
function. Notice that `next-guess` and `good-enough?` accepts the same `total`
and `guess` that is passed in to larger-square. Removing the redunant
arguments in the two helper functions results in:

(define (largest-square total guess)

    
    	(define (next-guess) (+ guess 1))
    	(define (good-enough?)
    		(< total (square (next-guess))))
    	(if (good-enough?)
    		guess
    (largest-square total (next-guess))))  
      
    How do you keep track of what is available to a function and what is not? We will spend a lot of time on this in Unit 3. When a function defined inside another function, the one inside has access to variables and parameters of the outer function. Because next-guess is defined inside largest-square, next-guess has access to largest-square's parameters, total and guess.  
      
    

If you find a mnemonic helpful, consider the outer function as a parent and
the inner function as a baby. A parent may lend the baby their stuff (like a
handphone) but the baby won't let the parents to take away his toys

![](http://4.bp.blogspot.com/-yfy4u4_1Wb4/TxbQrWKytMI/AAAAAAAAIxs/Hi9b9LWDPGY/
s400/cute-baby-playing-handphone-448x336.jpg) ![](http://kidsbesttoys.net/wp-
content/images/lamaze-tug-and-play-knot-block-baby-toy-3.jpg)

