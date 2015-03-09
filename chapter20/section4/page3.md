## Inserting

To insert into a 2D table, you also need 2 keys. The first key is used to try
and find the correct subtable. If a subtable with the first key doesn't exist,
make a new subtable. If the table exists, use the exact same algorithm we have
for the 1 dimensional` insert!` .

    
    
    (define (insert! key-1 key-2 value table)
      (let ((subtable (assoc key-1 (cdr table))))
        (if subtable
            (let ((record (assoc key-2 (cdr subtable))))
              (if record
                  (set-cdr! record value)
                  (set-cdr! subtable
                            (cons (cons key-2 value)
                                  (cdr subtable)))))
            (set-cdr! table
                      (cons (list key-1
                                  (cons key-2 value))
                            (cdr table)))))
      'ok)
    

