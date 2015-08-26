## Intro

In Unit 2, we briefly mentioned that we can store data using a 2-dimensional table and, given two keys, can fetch the desired data. We can use mutable lists to represent this data structure by first building a 1-dimensional table and then extending the idea.

## Before We Start: `assoc`

Before we dive in to tables, we have to explore another Racket compound procedure, `assoc`, which will play a huge role. `assoc` accepts a `key` and a list of pairs, and returns the first pair that has `key` as its `car`. If no such pairs exist, it returns `#f`. Look at the series of examples below to understand what `assoc` does.

    
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

Since this lesson deals with mutable data, we'll be using `massoc` with
our tables. The procedure `massoc` has the same functionality as `assoc`, 
but it works on mutable lists.
    

## 1-Dimensional Tables

In a **1D table**, values are stored under a single key. A table will be designed
as a list of pairs. Each pairs' `car` hold the key for each value.

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-22.gif)

In the above table, the breakdown between the keys and values can be seen
below.

<table class="table table-bordered">
<thead>
  <tr>
    <th>Key</th>
    <th>Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>a</td>
    <td>1</td>
  </tr>
  <tr>
    <td>b</td>
    <td>2</td>
  </tr>
  <tr>
    <td>c</td>
    <td>3</td>
  </tr>
</tbody>
</table>

Why does our table point to a pair that doesn't contain any key-value pair? We
designed our table so that the first pair holds the symbol `*table*` which
signifies that the current list structure we're looking at is a table. This
is similar to the idea of tagged data from Lesson 6.

### `make-table`

Here is the simple constructor for our table:
    
    (define (make-table)
      (mcons '*table* '()))
    
### `lookup`

To extract information from a table, we use the `lookup` procedure, which takes
a key as argument and returns the associated value (or false if there is no
value stored under that key).

    
    (define (lookup key table)
      (let ((record (massoc key (mcdr table))))
        (if record
            (mcdr record)
            false)))  
    
    > (lookup 'b table)  ;table refers to the table made above
    2
    

### `insert!`

To insert a key-value pair in a table, we follow this simple algorithm:

  1. If key is already in the list, just update the value 
  2. Otherwise, make a new key-value pair and attach it to the table

We define `insert!` as follows:
    
    (define (insert! key value table)
      (let ((record (massoc key (mcdr table))))
        (if record
            (set-mcdr! record value)
            (set-mcdr! table
                      (mcons (mcons key value) (mcdr table)))))
      'okay)
    

## 2-Dimensional Tables

In a **2D table**, each value is specified by _two_ keys. We can construct
such a table as a 1D table in which each key identifies a subtable.
Say we have two tables, "math" and "letters", with the following key-value pairs.

    
    math:
        + : 43
        - : 45
        * : 42
    
    letters:
        a : 97
        b : 98
    

We can put them into one big table:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-23.gif)

Our constructor for 2D tables is the same as our constructor for 1D tables:

      (define (make-table)
        (mcons '*table* '()))

## Lookup

To find a value in a 2D table, you will need 2 keys. The first key is used to
find the correct subtable. The second key is used to find the correct value in
that subtable.

    
    
    (define (lookup key-1 key-2 table)
      (let ((subtable (massoc key-1 (mcdr table))))
        (if subtable
            (let ((record (massoc key-2 (mcdr subtable))))
              (if record
                  (mcdr record)
                  #f))
            #f)))
    

### `insert!`

To insert into a 2D table, you also need 2 keys. The first key is used to try
and find the correct subtable. If a subtable with the first key doesn't exist,
make a new subtable. If the subtable exists, use the exact same algorithm on this
subtable that we used in our 1D table's `insert!`.

    
    (define (insert! key-1 key-2 value table)
      (let ((subtable (massoc key-1 (mcdr table))))
        (if subtable
            (let ((record (massoc key-2 (mcdr subtable))))
              (if record
                  (set-mcdr! record value)
                  (set-mcdr! subtable
                            (mcons (mcons key-2 value)
                                  (mcdr subtable)))))
            (set-mcdr! table
                      (mcons (mlist key-1
                                  (mcons key-2 value))
                            (mcdr table)))))
      'okay)
    

## Local Tables

The `lookup` and` insert!` operations defined above take the table as an
argument. This enables us to use programs that access more than one table.
Another way to deal with multiple tables is to have separate `lookup` and`
insert!` procedures for each table. We can do this by representing a table
procedurally, as an object that maintains an internal table as part of its
local state. When sent an appropriate message, this table "object" supplies
the procedure with which to operate on the internal table. Here is a generator
for two-dimensional tables represented in this fashion:

    
    (define (make-table)
      (let ((local-table (mlist '*table*)))
        (define (lookup key-1 key-2)
          (let ((subtable (massoc key-1 (mcdr local-table))))
            (if subtable
                (let ((record (massoc key-2 (mcdr subtable))))
                  (if record
                      (mcdr record)
                      false))
                false)))
        (define (insert! key-1 key-2 value)
          (let ((subtable (massoc key-1 (mcdr local-table))))
            (if subtable
                (let ((record (massoc key-2 (mcdr subtable))))
                  (if record
                      (set-mcdr! record value)
                      (set-mcdr! subtable
                                (mcons (mcons key-2 value)
                                      (mcdr subtable)))))
                (mset-cdr! local-table
                          (mcons (mlist key-1
                                      (mcons key-2 value))
                                (mcdr local-table)))))
          'okay)    
        (define (dispatch m)
          (cond ((eq? m 'lookup-proc) lookup)
                ((eq? m 'insert-proc!) insert!)
                (else (error "Unknown operation -- TABLE" m))))
        dispatch))

If this is confusing to you, review Lesson 8's sections on local state variables. 
The idea of a dispatch procedure that interprets messages delivered to your table 
is very similar to the [bank account example](http://www.cs61as.org/textbook/local-state-variables.html#sub4).
    

### `get` and `put`

When we discussed data-directed programming in Unit 2, we used a 2D table to store a value
under two keys using the procedures `get` and `put`:

    
    (put <key-1> <key-2> <value>)
    (get <key-1> <key-2>)
    

We can now define these procedures using our "local" tables, as defined right above!

    
    (define operation-table (make-table))
    (define get (operation-table 'lookup-proc))
    (define put (operation-table 'insert-proc!))
    
Remember that `(operation-table 'lookup-proc)` and `(operation-table 'insert-proc!)` both
return procedures!

The procedure `get` takes as arguments two keys, and `put` takes as arguments two keys and a
value. Both operations access the same local table, which is encapsulated
within the object created by the call to `make-table`.
