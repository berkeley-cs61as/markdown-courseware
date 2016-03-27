## Introduction
At this point, you should be very familiar with programming principles in Scheme and Racket. 
Time to transfer this knowledge into a new language! Enter Python. This is a bit more detailed than the intro to Python in your project 4 spec but still pretty basic. Doing one should make the other a breeze. Enjoy!

## Homework
The homework prompts are scattered throughout the lesson and are intended to be little exercises to do while you learn. Here's the [template](https://drive.google.com/open?id=0Bx-YJoc_dDDGQjhHSnNlRDNkaTg). More details on the homework section of this lesson!

## Installation
We'll be using Python 3 (specifically 3.5) in this lesson. This is not equivalent to Python 2. You can skip the following if you have already installed Python 3. When you launch python in your terminal, the version you have installed is displayed so check there.

### Anaconda (recommended installation method)
Anaconda is a distribution of Python that packages together Python with some other useful libraries such as [NumPy](https://en.wikipedia.org/wiki/NumPy). Anaconda also makes it much easier to install more extensions and automatically adds python to your computer’s path variable.

Please install Python 3.5 from this link: https://www.continuum.io/downloads and optionally read [this](http://conda.pydata.org/docs/py2or3.html) to get more acquainted with conda and its awesomeness.

It’s okay to obtain Python 3.5 via other methods, this is just a recommended method. If you run into any problems, consult Google and StackOverflow!

## Loading and Running Python

If you have Python 3 installed correctly, you should be able to launch it via your terminal with the command ```python```. You should see three carrots ```>>>``` that indicate that the python interpreter is accepting input! If you're having problems, please check that you've set up your path environment variable to point to your installation (if you're not sure what that means, try google!) and make sure that you remove any other paths to older python versions. If you're on a mac, see [this](http://superuser.com/questions/770696/how-to-update-macs-system-python).
```
MyComputer ~ $ python
Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Jan 29 2016, 15:01:46) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit() #exiting python
MyComputer ~ $ 
```

If you have a file you’d like to run in python, you can type into your terminal “python” followed by the file path and the “-i” flag to load the file and run python interactively. If you are missing the -i flag, the python load the file, run it, and exit
```
MyComputer ~ $ python python_hw.py -i
>>>
```

## Resources
Not required reading! Just references for more help and instruction:

  * [Official Python 3 Guide and Documentation](https://docs.python.org/3/tutorial/index.html)
  * [Python Wikibook](https://en.wikibooks.org/wiki/Python_Programming)
  * [Mini Python Examples](https://wiki.python.org/moin/SimplePrograms)
  * [Google](https://google.com)

When you're ready, move on to the next section!
