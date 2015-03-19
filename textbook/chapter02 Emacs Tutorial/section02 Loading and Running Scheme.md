## The Basics

So you have a Scheme file open in Emacs, now what? Let's walk through how to
load and run the file through Emacs.

Type M-x (i.e. Meta+x) then type "run-scheme". Alternatively, you could also
just type M-s.

This will run the Scheme interpreter inside of Emacs. This is already superior
to the interpreter inside the normal terminal, since this one has history (M-p
= go backwards and M-n = go forwards).

But we want to run a file, not just type commands! So...let's go back to that
file. Recall that you can use M-x <arrow-key> to cycle between buffers or C-x
o to switch windows.

Once you have the scheme interpreter running and you're at your file, you can
press C-c M-l (i.e. Control+c, then Meta+l) to load the file into the
interpreter. Emacs will prompt you with which file you want to load. The
default choice (what you'll get if you just press enter) is  the current file.
You'll need to switch back to the interpreter to see what it outputs.

You should be good to go! All the functions and methods you've defined in your
file should now be available in the interpreter.

## Troubleshooting

**Problem 1:** When doing run-scheme, Emacs coughs up something and nothing happens. No scheme! What's going on?

**Solution 1:** Emacs does not know how you call your scheme.This is set up on lab computers, but not home computers. Add the line:

(setq scheme-program-name "stk-simply")

to your ~/.emacs file (may need to create it if not already there), and
restart emacs again.

If this does not work, try replacing it with the line (and restart emacs
again):

(setq scheme-program-name "/usr/local/bin/stk-simply")

**Problem 2:** When typing C-c C-l, Emacs doesn't actually prompt for file or it doesn't seem C-c C-l works at all...

**Solution 2:** You're probably not in scheme-mode (in different modes, key combos do different stuff)

To resolve this, type M-x, then "scheme-mode".

-- If emacs prompts for file and all, but definitions didn't load properly into interpreter, it may be that you have a syntax error hiding in there.

Check to see if the interpreter wrote something in its buffer (*scheme*) when
you loaded that file.

## Extra

You don't always need/want to load the full file. Sometimes, you might just
have changed one expression!

C-x C-e lets you evaluate a single expression, with the result printed into
the interpreter.

Move the cursor right after the last parenthesis of the expression. Then...
C-x C-e and presto, the result shows up in the interpreter!

