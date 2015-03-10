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

