## Intro

We have mentioned in Unit 2 that we can store data using a 2 dimensional table and, given 2 keys, can fetch the desired data. We can use mutable lists to represent this data structure by first building a 1 dimensional table and extending the idea.

## Before We Start: `assoc`

Before we dive in to tables, we have to explore another Scheme compound procedure, `assoc`, which will play a huge role. `assoc` accepts a `key` and a list of pairs, and returns the first pair that has `key` as its `car`. If no such pairs exist, it returns `#f`. Look at the series of examples below to understand what `assoc` does.

    
    > (assoc 1 '((1 2) (3 4)))
      (1 2)     ;returns the pair with car 1
    
    > (assoc 'cupcake '((1 2) (3 4) (cupcake donut) (galaxy star)))
      (cupcake donut)    ;anything can be a key.
    
    > (assoc 2 '((1 2) (3 4)))
      #f      ;No pair has 2 as its car, hence returns #f
    
    > (assoc 'froyo '((cupcake donut eclair)
                      (froyo gingerbread honeycomb) 
                      (sandwich jellybean kitkat)))
      (froyo gingerbread honeycomb)    ;Pairs can be of any length

Here is the formal definition for `assoc`:

    (define (assoc key records)
      (cond ((null? records) false)
            ((equal? key (caar records)) (car records))
            (else (assoc key (cdr records)))))
    

## 1-Dimensional Tables

In a **1D table**, values are stored under a single key. A table will be designed
as a list of pairs. Each pairs' `car` hold the key for each value.

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-22.gif)

In the above table, the breakdown between the keys and values can be seen
below.

<table class="table table-bordered table-striped">
<thead><tr>
    <th>Keys</th>
    <th>Values</th>
</tr></thead><tbody>
<tr>
    <td><code>a</code></td>
    <td><code>1</code></td>
</tr>
<tr>
    <td><code>b</code></td>
    <td><code>2</code></td>
</tr>
<tr>
    <td><code>c</code></td>
    <td><code>3</code></td>
</tr>
</tbody>
</table>

Why does our table point to a pair that doesn't contain any key-value pair? We
designed our table so that the first pair holds the symbol `*table*` which
signifies that the current list structure we're looking at is a table.

### `make-table`

Here is the simple constructor for our table:
    
    (define (make-table)
      (list '*table*))

### `lookup`

To extract information from a table, we use the `lookup` selector, which takes
a key as argument and returns the associated value (or `#f` if there is no
value stored under that key). Here's our definition of `lookup`
    
    (define (lookup key table)
      (let ((record (assoc key (cdr table))))
        (if record
            (cdr record)
            false)))  
    
    > (lookup 'b table)  ;table refers to the table made above
    2
    

### `insert!`

To insert a key-value pair in a table, we follow this simple algorithm:

  1. If key is already in the list, just update the value 
  2. Otherwise, make a new key-value pair and attach it to the table
    
    
    (define (insert! key value table)
      (let ((record (assoc key (cdr table))))
        (if record
            (set-cdr! record value)
            (set-cdr! table
                      (cons (cons key value) (cdr table)))))
      'ok)
    

## 2-Dimensional Tables

In a **2D table**, each value is specified by _two_ keys. We can construct
such a table as a 1 dimensional table in which each key identifies a subtable.
Say we have 2 tables: "math" and "letters" with the following key-value pairs.

    
    math:
        + : 43
        - : 45
        * : 42
    
    letters:
        a : 97
        b : 98
    

We can put them into one big table:

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-23.gif)

### `lookup`

To find a value in a 2D table, you will need 2 keys. The first key is used to
find the correct subtable. The second key is used to find the correct value in
that subtable.

    
    
    (define (lookup key-1 key-2 table)
      (let ((subtable (assoc key-1 (cdr table))))
        (if subtable
            (let ((record (assoc key-2 (cdr subtable))))
              (if record
                  (cdr record)
                  #f))
            #f)))
    

### `insert`

To insert into a 2D table, you also need 2 keys. The first key is used to try
and find the correct subtable. If a subtable with the first key doesn't exist,
make a new subtable. If the table exists, use the exact same algorithm we have
for the 1 dimensional `insert!`.

    
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
    

## Local Tables

The `lookup` and` insert!` operations defined above take the table as an argument. This enables us to use programs that access more than one table. Another way to deal with multiple tables is to have separate `lookup` and `insert!` procedures for each table. We can do this by representing a table procedurally, as an object that maintains an internal table as part of its local state. When sent an appropriate message, this "table object'' supplies the procedure with which to operate on the internal table. Here is a generator for two-dimensional tables represented in this fashion:
    
    
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
    

### `get` and `put`

In Unit 2's "Data Directed" subsection, we used a 2D table to store a value
under 2 keys using the procedures `get` and `put`.

    
    (put <key-1> <key-2> <value>)
    (get <key-1> <key-2>)
    

We can now define these procedures using our tables!

    
    (define operation-table (make-table))
    (define get (operation-table 'lookup-proc))
    (define put (operation-table 'insert-proc!))
    

`get` takes as arguments two keys, and `put` takes as arguments two keys and a value. Both operations access the same local table, which is encapsulated within the object created by the call to `make-table`.