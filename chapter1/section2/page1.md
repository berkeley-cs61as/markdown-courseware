**Install Emacs**

Download Emacs from [http://emacsformacosx.com/

](http://emacsformacosx.com/)Drag the Emacs.app file to Applications.

**Set STk as scheme interpreter in Emacs**

  * Download a .emacs file for Mac from [here](/static/emacs). Download it to your Downloads folder and make sure it is called "emacs".
    * Note: this is not the emacs program. This is a text file that contains code that configures your emacs accurately.
  * Open up your terminal, and type `cp ~/Downloads/emacs ~/.emacs`
    * This copies the emacs file from your Downloads directory to ~/.emacs. The emacs configuration file needs to be in Downloads or it won't work.

**Try it out!**

Try pressing "M-x run-scheme" (that's Alt-x, then typing "run-scheme", then
press Enter)

If STk interpreter opens, you're good. Otherwise, ask a TA during office
hours.

Ctrl-C Meta-L should also work like it does on the lab computers. Note that
you might have to press Esc intead of option/alt for the Meta key.

This is what it should look like:

![](/static/emacs_stk.png)

