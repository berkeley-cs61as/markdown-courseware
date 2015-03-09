## BFS Example

Lets walk through how the code above works using the example Tree below. The
arrows in the diagram indicate the parent --> child relationships.

![](http://upload.wikimedia.org/wikipedia/commons/6/67/Sorted_binary_tree.svg)

When `bfs-iter` is first called, the whole Tree is put into the `queue`. To
simplify things, let's say a tree is denoted by its root.

queue: (F)

It prints the value at the node F, and recursively calls `bfs-iter` with the
rest of the queue and the children of F. The rest of the queue is empty, but
the children of F is (B G).

queue: (B G)

`bfs-iter` will print the node of the first tree in the queue, B and
recursively calls `bfs-iter` with the rest of the queue, `(G)` and the
children of B,`(A D)`

queue: (G A D)

And so on until the queue is empty. Once the queue is empty, we will have
printed out each node's datum exactly once.

Note that the siblings are always first in the queue and the children are
entered from the back. This ensures that siblings are checked first before
children.

