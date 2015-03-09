## takeaways

Here are the takeaways from this subsection:

  * Remember your constructor and selectors (`make-tree`, `datum`, and `children`).
  * To map over Trees, we use mutual recursion, where the two procedures are written in terms of each other. Typically, one of those procedures takes in a Tree, and the other takes in a forest.
  * Breath First Search looks at the nodes in the same level first, whereas Depth First Search goes through each branch until it hits the leaf node.

