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

