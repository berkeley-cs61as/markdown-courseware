## An Overview

## Three-Way Handshake

## Trying it Out

To better understand client/server systems, we're going to jump in and try
things out! Don't worry if you don't understand absolutely everything just
yet.

You'll need three people, each on a separate workstation. If you can't find
two other people to work with, you can also do these exercises by opening up
three separate terminals. However, that is not nearly as fun.

## Being the Server

Out of the three people in your group, one person should choose to be the
server. To run the server, that person should type the following commands into
a Scheme interpreter:

    
         > (load "~cs61as/lib/im-server.scm")
         > (im-server-start)
    
    

These commands will print the IP (Internet Protocol) address of the machine
you're using, along with another number, the port assigned to the server. Make
a note of the IP address and port number that these commands print! Your other
group numbers will need these numbers to connect to your server.

Note: Port numbers are important because there might be more than one server
program running on the same computer, and also they allow the server to keep
track of connections from more than one client.

## Being a Client

The other two people in your group will be clients. In order to connect to the
server, they will need the IP address and port number from the server. They
will type the following commands into a Scheme interpreter:

    
        > (load "~cs61as/lib/im-client.scm")
        > (im-enroll "123.45.67.89" 6543) ; Replace numbers
                                          ; with server's numbers!
    
    

Make sure to use the server's IP address instead of 123.45.67.89 and the
server's port number instead of 6543. (Note: the IP address must be enclosed
in quotation marks)

Once both clients have run the above commands, they can send each other
messages:

    
        > (im 'cs61as-xy "Hi there, how are you?")
    

The messages can't include more than one line. A client can leave the IM
system by running:

    
        > (im-exit)
    

The server can quit (which disconnects all the clients) with:

    
        > (im-server-close)

Play around with the above commands and peek at the source code if you want to
figure out what's going on!



## Our Client/Server Model

This simple implementation uses the Scheme interpreter as its user interface;
you send messages by typing Scheme expressions. Commercial Instant Message
clients have a more ornate user interface, that accept mouse clicks in windows
listing other clients to specify the recipient of a message. But our version
is realistic in the way it uses the network; the IM client on your home
computer connects to a particular port on a particular server in order to use
the facility. (The only difference is that a large commercial IM system will
have more than one server; your client connects to the one nearest you, and
the servers send messages among themselves to give the illusion of one big
server to which everyone is connected.)

In the news these days, client/server protocols are sometimes contrasted with
another approach called peer-to-peer networking, such as ﬁle-sharing systems
like Napster and BitTorrent. The distinction is social rather than strictly
technical. In each individual transaction using a peer-to-peer protocol, one
machine is acting as a server and the other as a client. What makes it peer-
to-peer networking is that any machine using the protocol can play either
role, unlike the more usual commercial networking idea in which rich companies
operate servers and ordinary people operate clients.

Client-server used to be part of this unit, but it isn't anymore. Don't worry
about it; you won't be tested on it and it's not covered in the homework.
Here's a picture of a penguin instead: ![](/static/emperor-penguin.jpg)

