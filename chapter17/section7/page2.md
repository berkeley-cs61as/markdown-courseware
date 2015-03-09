## Naming Intuition

You may be thinking that `usual` is a funny name for this function. Here's the
idea behind the name: We are thinking of subclasses as specializations. That
is, the parent class represents some broad category of things, and the child
is a specialized version. (Think of the relationship of checking-accounts to
`accounts` in general.) The child object does almost everything the same way
its parent does. The child has some special way to handle a few messages, di
fferent from the usual way (as the parent does it). But the child can
explicitly decide to do something in the usual (parent-like) way, rather than
in its own specialized way.

