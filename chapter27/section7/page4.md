### Reducing a List of Buckets

The procedure `reduce-bucket` above reduces one bucket. Our result from the
previous step, `(sort-into-buckets (map mapper data))` is a list of buckets.
To reduce a list of buckets, we can use map again. We are going to define the
function `group-reduce` that does exactly that.

    
    
    (define (groupreduce reducer base-case buckets)
    	(map (lambda (bucket) (reduce-bucket reducer base-case bucket))  
                 buckets))
    

If we use what we have so far, it evaluates into the following:

    
    
    >(groupreduce reducer 0 (sort-into-buckets (map mapper all-songs)))
    ( (i . 4) (saw . 1) (her . 1)
      . . .
      (misery . 1) (please . 2) (me . 1)
      . . .
      (all . 2) (have . 2))
      

Some values are omitted for conciseness. The final result is again, a list of
kv-pairs: the key is the word, the value is how many times those words appear
in our data. We have just used mapreduce to construct word counts for words in
our data!

This is the final (hand-wavy, approximated) definition of our mapreduce:

    
    
    (define (mapreduce mapper reducer base-case data)
    	(groupreduce reducer base-case (sort-into-buckets (map mapper data))))
      

Why is it not the actual mapreduce? The actual one will involve mapping and
reducing our kv-pairs parallely and we have to take into account of
concurrency issues. The definition above captures the major parts that we are
concerned with.

