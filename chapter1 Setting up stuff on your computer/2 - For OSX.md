**Download scheme **  
It's [here.](http://inst.eecs.berkeley.edu/~scheme/precompiled/OSX/STk-
ucb1.3.6.dmg) (Files for other operating systems are
[here](http://inst.eecs.berkeley.edu/~scheme).)

**Install the package**

Open the file you downloaded and install the package inside.

You may have to open it by pressing Control and clicking on the package, then
clicking "open", due to OSX restrictions.

![](/static/Open_package.png)

**Install XQuartz**

Download XQuartz from [http://xquartz.macosforge.org/landing/

](http://xquartz.macosforge.org/landing/)Install the package inside.[

](http://xquartz.macosforge.org/landing/)You again may have to open it by
pressing Control clicking on the package, due to OSX restrictions.

![](/static/open_xquartz.png)

**Try it out!**

Try opening terminal and launch "stk-simply". If the STk interpreter pops up,
you're good.

You may need to restart computer (to finish XQuartz install) if it doesn't
work.

This is what it should look like:

![](/static/terminal.png)

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

