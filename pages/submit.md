This page explains how to submit files for homeworks and projects.
We'll be submitting Homework 0.1 as an example, but you can follow the same process to submit other assignments.

It is perfectly fine if this part is confusing for you right now.
It will take some time for you to become comfortable with these commands.
If you are not sure what a command does, you can always refer back to this page.

**Note:** For all screenshots below, disregard the `.scm` file extensions and pretend they are `.rkt` files.

## Before We Begin

This guide assumes that the file you are trying to submit is available on the lab computers, and that you're logged into a lab computer (whether in person or over SSH).

If your file is on your own computer (e.g. your laptop), you need to transfer it to a lab computer.
To do this, [download Filezilla](https://filezilla-project.org/download.php?type=client) and follow
[these instructions](https://docs.google.com/document/d/11afVDf885DrPUyLvLihbHMP2amTo8Va1pXEgEsvTA9U/edit?usp=sharing).

If you are not logged into a lab computer, you should either go to lab or connect to the lab computers via SSH.
The instructions for doing the latter can be found [here](https://docs.google.com/document/d/1a-eE4zeEpnL7vT54gbOAn8jLElMxwqPH3GkPnE3bXdU/edit?usp=sharing).

## The `ls` Command

Typing `ls` in the terminal shows you a list of files and directories (or folders) that you currently have access to.
Use this command to confirm that your file exists. For example, I can confirm that I have access to my `hw0-1.rkt` file:

![](/static/ls.jpg)

## The `mkdir` Command
    
We are going to have a lot of files for different assignments, so it's a good idea to
keep them organized by putting each assignment into its own directory (folder).
`mkdir` stands for "make directory", and is used for, well, making directories.

We can make a new directory called `homework0-1` by typing:

    mkdir homework0-1

Now type `ls` again to check that you've created
a new directory successfully.

![](/static/mkdir.png)

## The `mv` Command

So you have your file (`hw0-1.rkt`) and you want to move it to its respective
directory (`homework0-1`) to keep everything tidy and sane. You can use the `mv`
command for this; `mv` stands for "move".

    mv hw0-1.rkt homework0-1
    
Typing `mv hw0-1.rkt homework0-1` will move the `hw0-1.rkt` file into the
`homework0-1` directory. You can type `ls` again to confirm that your `hw0-1.rkt` file is no longer there.

![](/static/mv.png)

## The cd Command

So your `hw0-1.rkt` file *should* be inside `homework0-1`. Let's check if that is
true by going inside the `homework0-1` directory. We can do this with the `cd`
command; `cd` stands for "change directory".

    
    
    cd homework0-1
    

Type `cd homework0-1` to go into your `homework0-1` directory. Now that you
are inside, type `ls` again to confirm that the file you moved is there.

![](/static/cd.png)

## The `submit` Command
    
    
    submit hw0-1
    

You are one step away from finishing! Since the name of the assignment is
`hw0-1`, you can submit it by typing `submit hw0-1`.

For each file in your *current* directory, you will now be asked if you want to submit it.
Type `yes` for each file you want to submit and type `yes` again to confirm the final submission. If your
submission is successful, it will show the message "Submission complete."

![](/static/submit.png)

Note the following:

  1. You can submit an assignment however many times you want. We will only take the latest one.
  2. The `hw0-1` in `submit hw0-1` refers to the assignment name, not your file name. Supposed I saved my Homework 0.1 file as `fox.rkt`. To submit `fox.rkt`, I would still type `submit hw0-1`, *not* `submit fox.rkt`.

## The `glookup -t` Command

Use the `glookup -t` command to view all submissions you've made and when you submitted them.
You can use this to verify that you've successfully submitted an assignment.

![](/static/glookup-t.png)

Note that the "lateness" will show the wrong result if you haven't submitted your `units` assignment.
(We did this on the first day in class. If you missed it, please talk to a TA.)
If you submitted it very recently, your results may take some time to appear correctly.

If you believe that there is a mistake, please notify a TA as soon as possible.

## The `glookup` Command

Use the `glookup` command to view your grades.

![](/static/glookup.png)

You can also type `glookup -s quiz1` to check the
statistics for Quiz 1. You can replace `quiz1` with any assignment name.

<!--
The workflow for this is as follows:

1. go to the directory where your homework is

2. transfer the file to your instructional account

3. log in to your instructional account and submit from there

**1. `cd` to the directory where your homework .rkt file is located**

`cd` to the directory where your homework is. Mine is located in a folder
called hw1 on my Desktop, so as soon as I open my terminal I'm going to type
`cd` once to get to the home directory. Now, I'm going to type `cd Desktop` to
get to my Desktop.  Next I'm going to type `cd hw1` to get to the hw1
directory. When I type `ls`, I see this:

![ls hw1](/static/ls_hw1.png)

**2. `scp` your file over to your instructional account**

Now, I'm going to type `scp hw1.rkt cs61as-ta@torus.cs.berkeley.edu:`

It should ask you for your password. If it didn't it's probably because you
forgot the `:` at the end.

**3. `ssh` into your instructional account and submit**

Now, I'm going to log in to my cs61as account with ssh:

`ssh cs61as-ta@torus.cs.berkeley.edu`

Again, it should ask you for your password.

Once you're logged in you should see something like this:

![ssh](/static/ssh.png)

Notice the hw1.rkt file sitting there.

Now, you should make a directory called hw1, move the hw1.rkt file to that
directory, and submit from that directory. Instructions on how to do that are
in the previous tab.

## The "units" assignment

  1. Make a new file called "units".
  2. Inside it, write down which units you are taking. For example if you are in the 0-3 track, write "0 1 2 3" and if you are in the 1-4 track, write "1 2 3 4".
  3. submit it under the assignment name "units"

-->