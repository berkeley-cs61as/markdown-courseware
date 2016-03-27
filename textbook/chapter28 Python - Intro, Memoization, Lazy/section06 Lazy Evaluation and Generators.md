## Lazy Evaluation

Sorry for this bit of a jump in topics. You're skipping this from Lesson 12, so we'll do a quick intro here.

Lazy evaluation is the implementation of normal order evaluation as opposed to applicative order evaluation. As a review, in Lesson 1, where we began our discussion of models of evaluation, we noted that Scheme is an applicative-order language, namely, that all the arguments to Scheme procedures are evaluated when the procedure is applied. In contrast, normal-order languages delay evaluation of procedure arguments until the actual argument values are needed. Delaying evaluation of procedure arguments until the last possible moment (e.g., until they are required by a primitive operation) is called lazy evaluation.

Python is similar to Scheme. When you define a procedure and call it with arguments. All arguments are evaluated before the body is evaluated.

Consider the procedure

```python
def try(a, b):
    if a == 0:
       return True
    else:
       return b
```

Evaluating ```try(0, 1/0)``` will trigger a division by zero error because the arguments are both evaluated first. 

In Lazy Evaluation, an error would not occur. Evaluating the expression would return 1, because the argument ```1/0``` would never be evaluated as it is never used in a primitive procedure nor returned.

```if``` is a lazy procedure when used directly. If you were to try:

```python
$ python
>>> if 0 == 0:
...    True
... else:
...    1/0
...
True
```

See that True gets returned since we never need to evaluate 1/0 so we never error! All this is possible because ```if``` is handled as a special form in the evaluation process (think mc-eval from lesson 11). For us to get this behavior in every procedure call, we would have to change how eval and apply work in Python. Instead of immediately evaluating the arguments to a procedure application before passing it to apply, we only do so if it is returned or used primitively. 

If you have an interest in a deeper understanding of lazy evaluation implemented in an interpreter, please read the original lesson 12 [content](http://www.cs61as.org/textbook/an-interpreter-with-lazy-evaluation.html). 

If you want to dabble with an implementation of lazy evaluation wrappers in Python, see the lazy.py module on this [website](http://blitiri.com.ar/p/python/).

## Range and Generators

We've been using ```range()``` in ```for``` loops but we haven't thought much how it works. Range is an immutable sequence that is lazy. Behind the scenes, elements in a sequence created by range aren't created until they are required. Don't believe me? Try ```print(range(4))``` and ```print([0, 1, 2, 3])```.

We can create similar sequences to ```range()``` through the use of generators. In Python, generators are functions than create sequences by computing and ```yield```ing the next value as needed. They are analogous to streams from Scheme and are a lazy sequence as opposed to lists which are eager sequences (eager to enumerate).

Generators are [iterable](https://docs.python.org/3/tutorial/classes.html#iterators) so you can use them in for loops, just like how we use range(). You can also call ```next(generator)``` on any generator procedure to get subsequent elements. Generators, however, cannot be iterated over multiple times. Once you've used up the sequence, it's gone. If you try to call ```next()``` on a used up generator you'll get a ```StopIteration``` error message.

Take a moment to ponder why we'd want generators. [Why not just always use lists?](https://www.google.com/search?q=when+to+use+generators+in+python)

```yield``` is how we create procedures that are generators as opposed to functions. You'll use ```yield``` instead of ```return```. Now for an example:

```python
def gen_to(n):
    for i in range(n+1):
        yield i
```

Now try printing each element using a for loop:

```python
gen_to_7 = gen_to(7)
for i in gen_to(7):
    print(i)
```

Now try calling next:

```python
next(gen_to_7)
```

Aha! The ```StopIteration``` error!

And now an infinite generator! Go ahead and try to ```print``` it and ```next``` through a call.

```python
def gen_forever():
    i = -1
    while true:
        i += 1
        yield i
```

> **Homework Problem 10: Growing Pains (Exponentially)**
>
>Write a generator ```gen_exp()``` that takes a number n and generates (for eternity) the exponential of n to the n to the n starting at n.
>
>For example the first few elements of ```gen_exp(2)``` should be 2, (2^2), ((2^2)^ 2), (((2^2)^ 2) ^ 2)


# TA DAH YOU'RE DONE!

## More cool things! You should look into if you liked learning Python. 

* [Importing Modules](https://docs.python.org/3/tutorial/modules.html) like the [math module... so awesome](https://docs.python.org/3/library/math.html). See [this link](https://docs.python.org/3/library/index.html) for an extensive directory of module libraries that come packaged with Python 3.5.
* [Turtle Graphics](https://docs.python.org/3/library/turtle.html)
* [Science-y math-y stuff](http://www.scipy.org/) which is already installed with an Anaconda distribuition
