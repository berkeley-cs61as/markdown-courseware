## Local Tables

The `lookup` and` insert!` operations defined above take the table as an
argument. This enables us to use programs that access more than one table.
Another way to deal with multiple tables is to have separate `lookup` and`
insert!` procedures for each table. We can do this by representing a table
procedurally, as an object that maintains an internal table as part of its
local state. When sent an appropriate message, this "table object'' supplies
the procedure with which to operate on the internal table. Here is a generator
for two-dimensional tables represented in this fashion:

    
    
    (define (make-table)
      (let ((local-table (list '*table*)))
        (define (lookup key-1 key-2)
          (let ((subtable (assoc key-1 (cdr local-table))))
            (if subtable
                (let ((record (assoc key-2 (cdr subtable))))
                  (if record
                      (cdr record)
                      false))
                false)))
        (define (insert! key-1 key-2 value)
          (let ((subtable (assoc key-1 (cdr local-table))))
            (if subtable
                (let ((record (assoc key-2 (cdr subtable))))
                  (if record
                      (set-cdr! record value)
                      (set-cdr! subtable
                                (cons (cons key-2 value)
                                      (cdr subtable)))))
                (set-cdr! local-table
                          (cons (list key-1
                                      (cons key-2 value))
                                (cdr local-table)))))
          'ok)    
        (define (dispatch m)
          (cond ((eq? m 'lookup-proc) lookup)
                ((eq? m 'insert-proc!) insert!)
                (else (error "Unknown operation -- TABLE" m))))
        dispatch))
    

## Get & Put

In Unit 2's "Data Directed" subsection, we used a 2D table to store a value
under 2 keys using the procedures `get` and `put`.

    
    (put <key-1> <key-2> <value>)
    (get <key-1> <key-2>)
    

We can now define these procedures using our tables!

    
    (define operation-table (make-table))
    (define get (operation-table 'lookup-proc))
    (define put (operation-table 'insert-proc!))
    

`Get` takes as arguments two keys, and `put` takes as arguments two keys and a
value. Both operations access the same local table, which is encapsulated
within the object created by the call to `make-table`.

