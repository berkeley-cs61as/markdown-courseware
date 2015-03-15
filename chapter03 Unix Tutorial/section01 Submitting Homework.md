## Submitting Homework

This section will show you how to submit files for homeworks and projects. We
will walk you through the different commands you can use in the terminal. This
example uses hw0-1 submission as an example, but submitting other homeworks
follows the same process.

**BEFORE SUBMITTING HOMEWORK: Make sure your file loads in Scheme. You can verify this by typing into STk: (load "hw0-1.scm"),** or whatever the name of your homework file is. You will not receive credit for homework that does not load in Scheme.

It is perfectly fine if this part is confusing for you right now; it takes
time until you are comfortable with these commands. If you are not sure what a
command does, you can always refer back to this page.

### The ls Command

    
    
    ls
    

Typing "ls" in the terminal shows you a list of files and directories(think of
them as folders) that you currently have access to. Use this command to
confirm that your file exists. For example, I can confirm that I have access
to my hw0-1.scm file.

![](/static/ls.jpg)

### The mkdir Command

    
    
    mkdir
    

We are going to have a lot of HW and project files, so it's a good idea to
keep them organized by putting each of them in its own directory/folder.
"mkdir" stands for "Make Directory" (or "Make Folder"), typing "mkdir
homework0-1" will make a new directory called "homework0-1".

After typing "mkdir homework0-1", type "ls" again to check that you've created
a new directory successfully.

![](/static/mkdir.png)

### The mv Command

So you have your file (hw0-1.scm) and you want to move it to its respective
folder(homework0-1) to keep everything tidy and sane. You can use the mv
command for this; mv stands for "move".

    
    
    mv hw0-1.scm homework0-1
    

Typing "mv hw0-1.scm homework0-1" will move the hw0-1.scm file into the
homework0-1 directory. You can type "ls" again to confirm that your hw0-1.scm
file is no longer there.

![](/static/mv.png)

### The cd Command

So your hw0-1.scm file SHOULD be inside homework0-1. Let's check if that is
true by going inside the homework0-1 directory. We can do this with the "cd"
command; "cd" stands for "change directory"

    
    
    cd homework0-1
    

Type "cd homework0-1" to go into your "homework0-1" directory. Now that you
are inside, type "ls" again to confirm that the file you moved is there.

![](/static/cd.png)

### The submit Command

    
    
    submit hw0-1
    

You are one step away from finishing! Since the name of the assignment is
"hw0-1", you can submit it by typing "submit hw0-1".

It will go through all the files you have access in your CURRENT directory and
asks for each file if you want to submit it. Type "yes" for each file you want
to submit and type "yes" again to confirm the final submission. If your
submission is successful, it will show the message "Submission Complete" :)

![](/static/submit.png)

**Notes:**

  1. You can submit however many times you want, we will only take the latest one.
  2. The "hw0-1" in "submit hw0-1" refers to the assignment name, not your file name. Say I saved my hw0-1 file name as "fox.scm" (Please don't actually do this, it will be confusing for you and the readers). If you want to submit "fox.scm" as your hw0-1, you will still type "submit hw0-1", NOT "submit fox.scm"

### Optional: glookup -t

Another command you can use is "glookup -t". It shows you a list of all
submissions you've made and when you've submitted it. If you're not sure if
the submission is successful, this is something you will use.

![](/static/glookup-t.png)

**Notes:**

  1. The "lateness" will show the wront result if you haven't submitted your "units" assignment. (We did this in class. If you missed it, please ask either in lab or Piazza). If you did submit it, please give it some time for it to refresh.
  2. If you believe that there is a mistake, please notify us ASAP

### glookup

You can type "glookup" inside the terminal to show a list of assignments and
grades. Note that this lists everything from unit 0 to unit 5, you should only
look at the units you are signed up for.

As the semester progress, you can also type "glookup -s quiz1" to check the
statistics for quiz1. You can replace "quiz1" with any assignment name. In the
beginning of the semester the command doesn't run because no grades have been
assigned.

![](/static/glookup.png)

**Note**: This assumes that you are working on a Mac or Linux machine. If you are working on Windows please follow the [Windows tutorial](http://www-inst.eecs.berkeley.edu/~cs61a/fa13/pdfs/connect-windows.pdf) for instructions. However, the general workflow is the same for all platforms.

**Everything here except for the last step is done on your home computer, not ssh-d in to the school computers.**

The workflow for this is as follows:

1. go to the directory where your homework is

2. transfer the file to your instructional account

3. log in to your instructional account and submit from there

**1. `cd` to the directory where your homework .scm file is located**

`cd` to the directory where your homework is. Mine is located in a folder
called hw1 on my Desktop, so as soon as I open my terminal I'm going to type
`cd` once to get to the home directory. Now, I'm going to type `cd Desktop` to
get to my Desktop.  Next I'm going to type `cd hw1` to get to the hw1
directory. When I type `ls`, I see this:

![ls hw1](/static/ls_hw1.png)

**2. `scp` your file over to your instructional account**

Now, I'm going to type `scp hw1.scm cs61as-ta@torus.cs.berkeley.edu:`

It should ask you for your password. If it didn't it's probably because you
forgot the `:` at the end.

**3. `ssh` into your instructional account and submit**

Now, I'm going to log in to my cs61as account with ssh:

`ssh cs61as-ta@torus.cs.berkeley.edu`

Again, it should ask you for your password.

Once you're logged in you should see something like this:

![ssh](/static/ssh.png)

Notice the hw1.scm file sitting there.

Now, you should make a directory called hw1, move the hw1.scm file to that
directory, and submit from that directory. Instructions on how to do that are
in the previous tab.

## The "units" assignment

  1. Make a new file called "units".
  2. Inside it, write down which units you are taking. For example if you are in the 0-3 track, write "0 1 2 3" and if you are in the 1-4 track, write "1 2 3 4".
  3. submit it under the assignment name "units"

