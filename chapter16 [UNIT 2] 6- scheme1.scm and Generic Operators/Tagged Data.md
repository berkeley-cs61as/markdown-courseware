## Weaknesses of Tagged Data

As we alluded to in the last section, there are a few weaknesses in the tagged
data design.

One, the generic interface procedures (such as `add-numbers`) must know about
all of the different representations. For instance, suppose we wanted to
incorporate a new type of number into our system. We would need to identify
this new representation with a type, and then add clauses to `add-numbers,
multiply-numbers, divide-numbers`,  etc. to check for the new type and apply
the appropriate procedure for that type of number.

Another weakness of the technique is that even though the individual
representations and corresponding procedures can be designed separately, we
must guarantee that no two procedures in the entire system have the same name.
This is why we created the new procedure `add-numbers,` which calls `add-
rational,` `add-complex`, and `add-rational-complex`.

The issue underlying both of these weaknesses is that the technique for
implementing generic interfaces is not _additive_. The person implementing the
generic procedures must modify those procedures each time a  new
representation or type is added. Additionally, the people who originally wrote
the rational number system and the complex number system must now modify their
code to avoid name conflicts. In each of these cases, the changes that must be
made to the code are straightforward, but they must be made nonetheless, and
this is a source of inconvenience and error.

