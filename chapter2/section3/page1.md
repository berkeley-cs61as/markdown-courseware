## Basics

**C-x C-f**

"Open". Opens a minibuffer that allows you to specify a file name to open

**C-x C-s **

"Save". Saves the current buffer

**C-x C-w **

"Save as". Saves the current buffer to a specified file.

**C-w **

"Cut". Deletes everything in the marked region

**M-w **

"Copy". Copies everything in the marked region

**C-y **

"Paste". Inserts contents that were previously cut or copied.

**C-x u **

"Undo". Undoes the effects of the last editing command.

**C-g **

Quits the current (Emacs) command. When in doubt, use it.

**C-x C-c **

Exits from Emacs. It prompts the user if there are any buffers that have not
been saved.

## Manipulating Buffers and Windows

**C-x o **

Makes another window on the screen (if any) the current window.

**C-x 0 **

Deletes the current window, expanding another window to take its place. The bu
ffer being displayed in the current window is not a ffected.

**C-x 1 **

Makes the current window the only window on the screen, deleting all others.
The buff ers being displayed in the deleted windows are not aff ected.

**C-x 2 **

Splits the current window into two vertically (one on top of the other), both
displaying the same buff er.

**C-x 3 **

Splits the current window into two horizontally (beside each other), each
displaying the same bu ffer.

**C-x b **

Prompts for a bu ffer name and switches the current window to that buff er.
When trying to move to a bu ffer associated with a file, it is better to use
the file fi nding commands.

**C-x C-b **

Lists the active bu ffers in a window

**C-x k **

Prompts for a bu ffer name and deletes that buff er, displaying some other
buff er in the current window. You will be warned if the contents of the buff
er have been modifi ed and not yet saved.

## Running Scheme

**M-x run-scheme **

When used for the fi rst time, creates a buff er named *scheme* and runs the
Scheme interpreter in it. If the bu ffer already exists, this command simply
moves to that buff er.

**C-c M-e **

sends the de finition after the cursor to Scheme (that is, it copies it the
*scheme* bu ffer and then sends it to the Scheme interpreter that attached to
that buff er). The command also places the cursor at the end of the *scheme*
buff er.

**C-c M-l **

loads an entire le into Scheme. Prompts for a fi le name; the default is the
current bu ffer's file. Puts the cursor at the end of the *scheme* bu ffer.

