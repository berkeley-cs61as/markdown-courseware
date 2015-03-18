# markdown-courseware

Welcome! This repository contains the Markdown files that make up the CS 61AS course website and textbook.

If you need a refresher on Markdown, see [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Quickstart
----------
To contribute to this project you will need a GitHub account. Create one [here](https://github.com/join).

To edit the course website/textbook from your browser:

1. **Navigate** to the Markdown file you want to edit.
2. Click the "edit" button, then **make your changes**.
3. When you are done editing, briefly **describe** your edits in the commit message box at the bottom.
3. **Submit** your edits by clicking "Propose file change" and follow any further instructions.

<!--
1. **Fork this repository** by clicking "Fork" above. This will make an editable copy of the course website for you. To understand this better, see GitHub's [help page](https://help.github.com/articles/fork-a-repo/).
2. In your forked copy, navigate to the Markdown file you want to edit then **make your changes** by clicking the "edit" button. Remember that you can click "Preview changes" to see what changes you've made.
3. **Save your changes**, making sure to describe your changes in the commit message.
4. **Create a pull request** by going [https://github.com/berkeley-cs61as/markdown-courseware/compare](here) and clicking "compare across forks". Then select your fork and click "Create pull request". This is you telling us, "I have made changes and I would like you to merge them." See GitHub's [https://help.github.com/articles/creating-a-pull-request/](help page) for more information.
-->
That's all! If you get stuck, contact Allen at allenguo@berkeley.edu. Comments and suggestions are also welcome!

Updating the Live Site
----------------------

These instructions are for staff members with write access to both this repository and the [berkeley-cs61as.github.io](https://github.com/berkeley-cs61as/berkeley-cs61as.github.io) repository.

### Before You Begin

1. Make sure you have Python 2.7 installed. As of right now, Python 3 is not supported.
2. Install the [markdown2](https://github.com/trentm/python-markdown2) module. (If you use pip: `pip install markdown2`.)
3. Clone this repository.
4. Clone [berkeley-cs61as.github.io](https://github.com/berkeley-cs61as/berkeley-cs61as.github.io).

### Deployment

0. Navigate to this repository.
0. Do a `git pull`.
2. Run `publish.py` by doing `python publish.py`. This will convert all of the Markdown files to HTML. By default, the resulting HTML files will be placed in `../berkeley-cs61as.github.io`.
3. Navigate to `../berkeley-cs61as.github.io`.
4. Commit and push.
4. Your changes will be instantly visible at http://berkeley-cs61as.github.io.

If you're interested in what `publish.py` does, or you want to make more complicated changes to the textbook, keep reading.

More Complicated Changes
------------------------
### Deleting/Adding Sections
To delete/add sections, simply delete/add Markdown files as needed. Keep in mind:

* Section file names are of the form `section## Title Goes Here.md`, where the `#`s are numerical digits.
* Sections are ordered by number. Feel free to change the numbers of existing sections as needed to get everything in the right order.

### Deleting/Adding Chapters
Deleting/adding chapters is kind of like deleting/adding sections: simply delete/add directories as needed. Keep in mind:

* Chapter directory names are of the form `chapter## Title Goes Here/`, where the `#`s are numerical digits.
* Chapters are ordered by number.

Additionally, you must update the `units` variable in `config.py`, which tells `publish.py` what chapters belong in each unit. `units` should be fairly easy to understand.

### Deleting/Adding Units
Remove/add the appropriate mapping from the `units` variable in `config.py`.

What Does `publish.py` Do?
--------------------------
`publish.py` has several roles:

* Generates a table of contents that includes every chapter and section.
* Converts Markdown files to HTML.
* Inserts the converted content in the appropriate places, as defined by the templates files (see below).
* Writes the final HTML files to the output directory (usually `../berkeley-cs61as.github.io`).

### Templating

Our publishing system includes a very simple templating system similar to what you might see in Templar or Django.

Take a look at `textbook-template.html`. Every page in the textbook uses this template. This template allows the following variables:
* `{{title}}` is the title of the page (i.e., the section title).
* `{{content}}` is the content of the page (converted from Markdown).
* `{{chaptertitle}}` is the title of the parent chapter.
* `{{chaptertoc}}` is the table of contents for the parent chapter.

A similar templating system exists for (non-textbook) pages. The template file is called `page-template.html`.

### Generating Tables of Contents

As stated above, the table of contents for each chapter is generated by `publish.py` and inserted using the templating language. In contrast, the table of contents for each *section* is generated from the front-end using jQuery.

