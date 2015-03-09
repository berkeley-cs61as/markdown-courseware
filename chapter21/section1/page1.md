##  ... Let's use streams!

Streams are a clever idea that allows one to use sequence manipulations
without incurring the costs of manipulating sequences as lists. With streams
we can achieve the best of both worlds: We can formulate programs elegantly as
sequence manipulations, while attaining the efficiency of incremental
computation. The basic idea is to construct a stream only partially, and to
pass the partial construction to the program that consumes the stream. If the
consumer attempts to access a part of the stream that has not yet been
constructed, the stream will automatically construct just enough more of
itself to produce the required part, thus preserving the illusion that the
entire stream exists. In other words, although we will write programs as if we
were processing complete sequences, we design our stream implementation to
automatically and transparently interleave the construction of the stream with
its use.

