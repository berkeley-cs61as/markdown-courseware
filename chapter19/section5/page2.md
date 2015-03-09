## Question B5: Laptop

Now invent the` laptop` class. A laptop has one instantiation variable, its
name.

    
    >(define somelaptop (instantiate laptop 'somelaptop)

A laptop is a thing that has two extra methods: `connect`, with a password as
argument, sends a `connect` message to the place where the laptop is. If the
password is wrong, return an error.

    
    >(ask somelaptop 'connect 1234)

A laptop also has another method, `surf`, with a URL text string as argument,
sends a `surf` message to the place where it is. Thus, whenever a laptop
enters a new hotspot, the user must ask to `connect` to that hotspot's
network; when the laptop leaves the hotspot, it must automatically be
disconnected from the network. (If it's in a place other than a hotspot, the
`surf` message won't be understood; if it's in a hotspot but not connected,
return an error)

    
    >(ask somelaptop 'surf "www.berkeley.edu")

` `

