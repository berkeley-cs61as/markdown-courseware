## Programming Considerations

Even with serializers, it's not easy to do a good job of writing programs that
deal successfully with concurrency. In fact, all of the operating systems in
widespread use today have bugs in this area; Unix systems, for example, are
expected to crash every month or two because of concurrency bugs.

To make the discussion concrete, let's think about an airline reservation
system, which serves thousands of simultaneous users around the world. Here
are the things that can go wrong:

  * **Incorrect results.** The worst problem is if the same seat is reserved for two diﬀerent people. Just as in the case of adding 1 to x, the reservation system must ﬁrst ﬁnd a vacant seat, then mark that seat as occupied. That sequence of reading and then modifying the database must be protected.
  * **Ineﬃciency.** One very simple way to ensure correct results is to use a single serializer to protect the entire reservation database, so that only one person could make a request at a time. But this is an unacceptable solution; thousands of people are waiting to reserve seats, mostly not for the same ﬂight.
  * **Deadlock.** Suppose that someone wants to travel to a city for which there is no direct ﬂight. We must make sure that we can reserve a seat on ﬂight A and a seat on connecting ﬂight B on the same day, before we commit to either reservation. This probably means that we need to use two serializers at the same time, one for each ﬂight. Suppose we say something like 
    
    (serializer-A (serializer-B (lambda () ...))))

Meanwhile someone else says

    
    (serializer-B (serializer-A (lambda () ...))))

The timing could work out so that we get serializer A, the other person gets
serializer B, and then we are each stuck waiting for the other one (forever!).

  * **Unfairness.** This isn't an issue in every situation, but sometimes you want to avoid a solution to the deadlock problem that always gives a certain process priority over some other one. If the high-priority process is greedy, the lower-priority process might never get its turn at the shared data.

## Correct Behavior of Concurrent Programs

Depending on the particular program you're writing, the definition of correct
behavior might differ. Typically, a concurrent program is said to display
correct behavior if it produces the same result as if the processes had run
sequentially in some order. There are two important aspects to this
requirement.

First, it does not require the processes to actually run sequentially, but
only to produce results that are the same _as if_ they had run sequentially.

Second, there may be more than one possible "correct" result produced by a
concurrent program, because we require only that the result be the same as for
some sequential order.

