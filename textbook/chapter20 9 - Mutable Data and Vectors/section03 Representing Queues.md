## What Is a Queue?

Using `set-mcar!` and `set-mcdr!` allows us to create a data structure that we
could not have implemented efficiently before: a queue. A **queue** is a sequence in which items are inserted at one end (called the rear of the queue) and deleted from the other end (the front). Because items are always removed in the order in which they are inserted, a queue is sometimes called a FIFO (first in, first out).

![](http://3.bp.blogspot.com/_w9XO9zBePXE/SKFjlee6K-I/AAAAAAAAAdk/iRjNgU62cmM/
s1600/royston_queue.jpg)

## Queue Operations

We can regard a queue as defined by the
following set of operations:

  * a constructor: `(make-queue)` returns an empty queue (a queue containing no items).
  * two selectors:
    * `(empty-queue? <queue>)` tests if the queue is empty.
    * `(front-queue <queue>)` returns the object at the front of the queue, signaling an error if the queue is empty. **It does not modify the queue.**
  * two mutators:
    * `(insert-queue! <queue> <item>)` inserts the item at the rear of the queue and returns the modified queue as its value.
    * `(delete-queue! <queue>)` removes the item at the front of the queue and returns the modified queue as its value, signaling an error if the queue is empty before the deletion.

We will implement these procedures below.

### Example

The following shows a series of queue operations and their effects.

<table class="table table-bordered table-striped">
<thead><tr>
    <th>Operation</th>
    <th>Resulting Queue</th>
</tr></thead><tbody>
<tr>
    <td><code>(define q (make-queue))</code></td>
    <td><code></code></td>
</tr>
<tr>
    <td><code>(insert-queue! q 'a)</code></td>
    <td><code>a</code></td>
</tr>
<tr>
    <td><code>(insert-queue! q 'b)</code></td>
    <td><code>a b</code></td>
</tr>
<tr>
    <td><code>(delete-queue! q)</code></td>
    <td><code>b</code></td>
</tr>
<tr>
    <td><code>(insert-queue! q 'c)</code></td>
    <td><code>b c</code></td>
</tr>
<tr>
    <td><code>(insert-queue! q 'd)</code></td>
    <td><code>b c d</code></td>
</tr>
<tr>
    <td><code>(delete-queue! q)</code></td>
    <td><code>c d</code></td>
</tr>
</tbody>
</table>

## Queues as Lists

Because a queue is a list of items, we can technically represent it with an ordinary list. The front of the queue will be the `car` of the list, inserting a new element will be equivalent to appending a new pair at the end. Deleting an item will just be the `cdr`.

Why don't we go with this implementation? The problem is the run time. To add an item to the back of a list, we have to go through a series of `cdr`s. If the list is really long, it will take us a really long time to find the last pair. The run time for this is linear in the length of the list.

A list allows us access to the first item in constant time, but when you need to find the last pair, it takes a long time. We can solve this simply by using a mutable list that stores and updates a pointer to the backmost pair.

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-19.gif)

Looking at the queue above, we see that we store two pointers: one that points to the front of the mlist and one to the back. If we try to add a new item, `'d`, to the queue, the structure will be changed into the following:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-20.gif)

When we want to find the last pair of `q`, we can follow the `(mcdr q)` pointer.

## Implementation

To define the queue operations, we use the following procedures, which enable us to select and modify the front and rear pointers of a queue:

    
    (define (front-ptr queue)
        (mcar queue))
    (define (rear-ptr queue)
        (mcdr queue))
    (define (set-front-ptr! queue item)
        (set-mcar! queue item))
    (define (set-rear-ptr! queue item)
        (set-mcdr! queue item))
    

Now we can implement the actual queue operations. We will consider a queue to be empty if its front pointer is the empty list:

    
    (define (empty-queue? queue)
        (null? (front-ptr queue)))
    

The `make-queue` constructor returns, as an initially empty queue, a pair whose `car` and `cdr` are both the empty list:

    
    (define (make-queue)
        (mcons '() '()))
    

To select the item at the front of the queue, we return the `mcar` of the pair indicated by the front pointer:

    
    (define (front-queue queue)
        (if (empty-queue? queue)
            (error "FRONT called with an empty queue" queue)
            (mcar (front-ptr queue))))
    

## Adding to a Queue

We will follow the general algorithm outlined before:

  1. `mcons` a new mpair containing the new item
  2. If the queue is empty, we set its `front-ptr` and `rear-ptr` to this new mpair
  3. If the queue isn't empty, we find the final mpair, change its `mcdr` to the newly made mpair and update the `rear-ptr`.
    
And now for the code:

```
(define (insert-queue! queue item)
  (let ((new-mpair (mcons item '())))
    (cond ((empty-queue? queue)
           (set-front-ptr! queue new-mpair)
           (set-rear-ptr! queue new-mpair)
           queue)
          (else
           (set-mcdr! (rear-ptr queue) new-mpair)
           (set-rear-ptr! queue new-mpair)
           queue)))) 
```

## Deleting from a Queue

To delete from a queue, we can simply change the `front-ptr` to point to the
next pair.

    
    
    (define (delete-queue! queue)
      (cond ((empty-queue? queue)
             (error "DELETE! called with an empty queue" queue))
            (else
             (set-front-ptr! queue (mcdr (front-ptr queue)))
             queue))) 
    

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-20.gif)

If starting from the queue above we decide to delete the first time, the change will only be where the `front-ptr` points to:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-21.gif)

## Takeaways

Using mlists and its operations, `set-mcar!` and `set-mcdr!`, allows us to implement a new data structure (the queue) much more efficiently than what lists and their operations (`cons`, `car`, and `cdr`) alone can build.