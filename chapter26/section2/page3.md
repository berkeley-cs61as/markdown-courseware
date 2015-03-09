## More Rules

Here's a slightly more complicated rule:

    
    
    (rule (lives-near ?person-1 ?person-2)
          (and (address ?person-1 (?town . ?rest-1))
               (address ?person-2 (?town . ?rest-2))
               (not (same ?person-1 ?person-2))))
    

It specifies that two people live near each other if they live in the same
town. The final `not` clause prevents the rule from saying that all people
live near themselves. The `same` relation is defined by the very simple rule:

    
    
    (rule (same ?x ?x))
    

