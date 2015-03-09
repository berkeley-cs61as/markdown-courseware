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

