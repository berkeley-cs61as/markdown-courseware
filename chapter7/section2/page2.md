## Base Case

To solve this problem, we will handle the empty sentence as a separate base
case. The predicate `empty?` is used to check for the empty sentence. Here is
the completed version of `sum-sent`:

    
    (define (sum-sent sent)
      (if (empty? sent)
          0
          (+ (first sent) (sum-sent (bf sent)))))

