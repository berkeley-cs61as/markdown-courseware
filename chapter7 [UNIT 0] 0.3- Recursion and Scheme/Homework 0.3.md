**You must finish both lab and homework for a lesson before submitting your homework for that lesson.**

**IF YOU HAVE ANY TROUBLE WITH SUBMITTING, ASK A QUESTION ON PIAZZA OR TALK TO A TA.**

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. More on that later.

Now, right click on the background and select xterm. Xterm is a terminal
emulator, a method of interacting directly to the computer via text commands.
It's sort of an "interpreter" for your entire computer. You can do useful
things with xterm like navigate and manipulate the filesystem (think Windows
Explorer), submit homework (what we're doing now), and start the Scheme
interpreter (via stk)!

If you've been saving your assignments in your Desktop folder, you need to go
there. If you were using Windows or MacOS, you'd probably open up a graphical
interface and click the Desktop folder icon. In xterm, we do

`cd ~/Desktop`

This tells the computer to change directories (a directory is what we'd call a
folder in Windows) from wherever you are now, to ~/Desktop, a folder named
Desktop that happens to be in your home directory (that's what the (~/) is
for).

From there, you can type

`ls`

which shows all of the files and folders in ~/Desktop. Make sure that your HW
1 file is in there. If not, using cd and ls, go to the folder which contains
your HW 1 file. Then, you can type:

`submit hw0-3`

to submit Homework 1. If you have more than one file in your Desktop folder,
submit will ask you "Do you want to submit …" for each file. Say (type) 'no'
to every file except for the HW 1 file.

Here is a quick video showing this for hw4: http://youtu.be/N_fmp6p9Ot0

