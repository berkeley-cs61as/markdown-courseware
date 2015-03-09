## Functional Programming

The big idea for this lesson is deceptively simple. It's that we can take the
value returned by one function and use it as an argument to another function.
By "hooking up" two functions in this way, we invent a new, third function.
For example, let's say we have a function that adds the letter s to the end of
a word (in pseudo-code):

    
    add-s("run") = "runs"

and another function that puts two words together into a sentence:

    
    sentence("day", "tripper") = "day tripper"

We can combine these to create a new function that represents the third person
singular form of a verb:

    
    third-person(verb) = sentence("she", add-s(verb))

That general formula looks like this when applied to a particular verb:

    
    third-person("sing") = "she sings"

The way we say it in Scheme is

    
    (define (third-person verb)
      (sentence 'she (add-s verb)))

This idea might not seem like a big deal to you. Nevertheless, it will turn
out that we can express a wide variety of computational algorithms by linking
functions together in this way. This linking is what we mean by "functional
programming."

