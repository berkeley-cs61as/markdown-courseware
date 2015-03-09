## Question B5: Hotspot

In the modern era, many places allow you to get connected to the net. Define a
`hotspot` as a kind of place that allows network connectivity. Each hotspot
should have a `name` and a `password` as instantiation variables that you must
know to connect.

    
    >(define library (instantiate hotspot 'library 1234))   
    ;name of hotspot is library, password is 1234  
    

(Note: We're envisioning a per-network password, not a per-person password as
you use with AirBears.) The hotspot has a `connect` method with two arguments,
a `laptop` (a kind of thing, to be invented in a moment) and a password. If
the password is correct, and the laptop is in the hotspot, add it to a list of
connected laptops otherwise, return an error. When the laptop leaves the
hotspot, remove it from the list.

    
    >(ask library 'connect somelaptop 1234)

Hotspots also have a `surf` method with two arguments, a laptop and a text
string, such as

    
        "http://www.cs.berkeley.edu"
    

If the laptop is connected to the network, then the surf method should

    
        (system (string-append "lynx " url))
    

where URL is the text string argument (note the space after x in "lynx ").
Otherwise, return an error.

    
    >(ask library surf somelaptop "http://www.cs.berkeley.edu")

