### Now We're Chaining

Our function above works, if we pass the pairs with the key as a word, and
value as a number. In real life, we might not have direct access to the word
counts of each word; we have to process that from the original document.

Write the function `real-most-frequent` that accepts a list of key-value pairs
where the key is the name of the file, and the values are lines from that file
(just like our all-songs example) . Our output is again, a list of **single**
key-value pair. You may want to reuse any functions we have defined so far in
the lesson.

    
    
    >(real-most-frequent all-songs)
    ((i . 4))
    

