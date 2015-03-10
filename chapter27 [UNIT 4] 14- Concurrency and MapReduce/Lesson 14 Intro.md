## Client/Server Intro

Before networks, most programs ran on a single computer. Today it's common for
programs to involve cooperation between computers. The usual reason is that
you want to run a program on your computer that uses data located elsewhere. A
common example is using a browser on your computer to read a web page stored
somewhere else.

To make this cooperation possible, two programs are actually required: the
client program on your personal computer and the server program on the remote
computer. Sometimes the client and the server are written by a single group,
but often someone publishes a standard document that allows any client to work
with any server that follows the same standard. For example, you can use
Mozilla, Netscape, or Internet Explorer to read most web pages, because they
all follow standards set by the World Wide Web Consortium.

For this course we provide a sample client/server system, implementing a
simple Instant Message protocol. The ﬁles are available in

    
        ~cs61as/lib/im-client.scm
        ~cs61as/lib/im-server.scm
    

