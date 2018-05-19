## Warning

This lesson contains dense reading and needs major revisions. If you find any of this material confusing or hard to understand, please do not hesitate to ask questions.

## Prerequisites and What to Expect

Make sure you understand all the material prior to this lesson, especially [Message Passing](http://berkeley-cs61as.github.io/textbook/message-passing.html).

In this section, we are going to go over the change of the state of the variables and environment. You get to draw cool diagrams that illustrates beautifully the environment in which Scheme stores variables and procedures. Be prepared to be exposed to a fair amount of information and synthesize it!

## Reading

In this section, we will cover the material in the following readings:

  * [Introduction to Unit 3: Modularity, Objects, and State ](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-19.html#%_sec_3)
  * [SICP 3.1: Assignment and Local State ](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-20.html#%_sec_3.1)
  * [SICP 3.2: The Environment Model of Evaluation](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-21.html#%_sec_3.2)
  * [OOP Below the line](http://inst.eecs.berkeley.edu/~cs61as/reader/belowline.pdf)
  * [Environment Diagram Rules](https://docs.google.com/document/d/1GbRF9rB9TtFbf--89MBDEHzygF2E5_E2wpLBh4rb4Z4/edit)

Feel free to read ahead!

Also, here's the webcast of old lecture videos. The only big example of an environment diagram is in the webcast, so we strongly suggest you watch it:

  * [Lecture 21](http://www.youtube.com/watch?v=vh73mm7MqA0&feature=share&list=PL6D76F0C99A731667)
  * [Lecture 22](http://www.youtube.com/watch?v=cmeWXO9Sa5E&feature=share&list=PL6D76F0C99A731667)
  * [Lecture 23](http://www.youtube.com/watch?v=SdwAj_eowzg&feature=share&list=PL6D76F0C99A731667)

## Modularity

We ordinarily view the world as populated by independent objects, each of
which has a state that changes over time. An object is said to "have state" if
its behavior is influenced by its history. A bank account, for example, has
state in that the answer to the question "Can I withdraw $100?" depends upon
the history of deposit and withdrawal transactions. We can characterize an
object's state by one or more state variables, which among them maintain
enough information about history to determine the object's current behavior.
In a simple banking system, we could characterize the state of an account by a
current balance rather than by remembering the entire history of account
transactions.

![](http://test.ical.ly/wp-content/uploads/2010/07/modularity.jpg)

In a system composed of many objects, the objects are rarely completely
independent. Each may influence the states of others through interactions,
which serve to couple the state variables of one object to those of other
objects. Indeed, the view that a system is composed of separate objects is
most useful when the state variables of the system can be grouped into closely
coupled subsystems that are only loosely coupled to other subsystems.

This view of a system can be a powerful framework for organizing computational
models of the system. For such a model to be **modular**, it should be
decomposed into computational objects that model the actual objects in the
system. Each computational object must have its own local state variables
describing the actual object's state. Since the states of objects in the
system being modeled change over time, the state variables of the
corresponding computational objects must also change. If we choose to model
the flow of time in the system by the elapsed time in the computer, then we
must have a way to construct computational objects whose behaviors change as
our programs run. In particular, if we wish to model state variables by
ordinary symbolic names in the programming language, then the language must
provide an assignment operator to enable us to change the value associated
with a name.

In object-oriented programming, one of the seven fundamental principles of the
object model. The **modularity principle** states that a program should be
composed of a collection of internally cohesive units, called objects, that
can communicate and interoperate without needing information about their
internal structure.

## Takeaways

In this subsection, you learned the definition of modularity.

## What's Next?

Go to the next subsection and see how you can use modularity to program!

