## What is Emacs?

GNU Emacs, is in some sense, a text editor. However, it is also a very
powerful program that is primarily used to write and edit code. It can be used
for as varied tasks as [sending email](http://www.chemie.fu-
berlin.de/chemnet/use/info/emacs/emacs_29.html) and[ browsing the
web](http://www.emacswiki.org/emacs/CategoryWebBrowser)!

Emacs has many built-in features specific to Scheme, such as parentheses
highlighting, automatic indentation, and even a Scheme interpreter. You'll
find that, with a little practice, writing and testing code through Emacs will
make your programming life easier.

Our hope is that by the end of this course, you'll be completely comfortable
with using Emacs. Even if you have another preferred text editor, you should
still learn Emacs! And if this is your first editor you're using as a
programmer, you'll always be fond of your first.

The rest of this tutorial borrows heavily from [Prof. Hilfinger's guide](http
://www-inst.eecs.berkeley.edu/~cs61as/reader/gnuemacs.pdf). If you want a more
detailed intro to Emacs,  you should check it out.

## Understanding Keyboard Shortcuts

One of the reasons Emacs is so powerful to edit code is because everything can
be controled through the keyboard. In fact, it is entirely possible to do
_everything_ Emacs has to offer without using your mouse! If you plan on
working remotely and don't want to wait for laggy graphics, I highly recommend
you start learning at least the basics.

There are two keys which are very important in Emacs: Control and the Meta
key. Control is the normal Ctrl key that you should be used to. The Meta key
varies depending on the computer, but it is typically either the Alt key.

<div class="mc">
Given the following class, what color is the dress?<pre><code>(define-class (test-penguin name)
    (parent (emperor-penguin name))
    (method (eat) ( ... )))
</code></pre>
<ans text="Blue and black." explanation="The dress was verified to be blue and black." correct></ans>
<ans text="White and gold." explanation="Well sure, maybe to <i>you</i> it looks like that."></ans>
<ans text="What dress? <code>help()</code> me please." explanation="Hah."></ans>
</div>

## Trying it Out

Let's try it out! You're going to try out your first Emacs command to see if
you have the hang of this.

First, you need to open Emacs. On the lab computers, type the following into a
terminal:

    
        emacs &

Next, open a file. You can use the bar at the top of the screen to help with
this (if you want to see the keyboard shortcut, check out the Useful Shortcuts
section). If you don't have any files yet, try creating a new file.

Next, make a change to your file, any change will do. Finally, let's save that
change. You could go to the top bar and click the save option, but let's try
out our new keys.

To save, type C-x C-s. This notation means hold Control down and then press x.
Then, continue holding Control down and then press s. The _mini-buffer_ at the
very bottom of the screen should confirm that the file saved.

Now, let's try out the Meta key. We're going to try a command that capitalizes
words. Let's start by typing any word into Emacs. Now, make sure your cursor
is on the first letter of that word. Try out the command M-c. You might have
to try both the Alt key and ESC key to figure out which key is Meta.

If you run into any problems, ask for help! There are tons of keyboard
shortcuts. Check out the Useful Shortcuts section or [this guide](http://www-
inst.eecs.berkeley.edu/~cs61as/reader/gnuemacs.pdf) for more.

## Buffers

Buffers are used within Emacs to hold text. This text may be from a file, but
it doesn't have to be. Emacs supports many buffers, which means you can have
multiple files loaded into Emacs at once.

## Windows

Windows are used to display part of a buffer's text. Windows are what you
_see_, while buffers hold all of the text that Emacs has loaded. Even if a
buffer doesn't have a corresponding window, the buffer's text is still
retained. You can open additional windows using C-x 2 (splits the current
window vertically) or C-x 3 (splits the current window horizontally). The
command C-x 2 means hold down Ctrl, press x, release both keys, press 2. I
promise it sounds a lot more complicated than it actually is.

## Practice

Let's practice switching between buffers and windows.

To switch between buffers _within_ a single window, you can use C-x <arrow-
key> to cycle between buffers. Try it out! You might discover a few buffers
that you didn't know exist.

To switch between windows, use C-x o. Try opening additional windows (C-x 2 or
C-x 3) and switching between them.

There are a lot more commands used to deal with buffers and windows in Emacs.
Check out [this guide](http://www-
inst.eecs.berkeley.edu/~cs61as/reader/gnuemacs.pdf#page=13) or the Useful
Shortcuts section if you're interested in more commands.

