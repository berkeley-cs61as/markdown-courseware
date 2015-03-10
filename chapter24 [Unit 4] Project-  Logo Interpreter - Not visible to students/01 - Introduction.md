## interpreter

It's time to write a fully functional interpreter! You've written several
interpreters up till now, starting with calc.scm, and this project has the
same basic `eval` and `apply` as the other interpreters.

In Chapter 4 we study a Scheme interpreter written in Scheme, the metacircular
evaluator. In this project we modify that evaluator to turn it into an
interpreter for a different programming language.

This project is valuable for several reasons: First, it will make you more
familiar with the structure of the metacircular evaluator because you'll have
to understand which procedure to modify in order to change some aspect of its
operation. Second, working with another language may help overcome some of the
confusion students often have about talking to two different versions of
Scheme at once. In this project, it'll be quite obvious when you're talking to
Scheme and when you're talking to Logo. Third, this project will encourage you
to think about the design of a programming language. Why did Scheme's
designers and Logo's designers make different choices?

This is a two-week project. As in the adventure game project, you'll have a
group of two people, person A and person B. Each week you will do some of the
work separately and then meet together for the final steps. After the first
week you should be able to enter instructions using primitive procedures with
constant arguments. In the second week you will add variables and user-defined
procedures. Just like in project 3, one person will submit the entire project
when you've finished.

**As always, test as you go.** We have provided some test cases for you, and it is important to use those to make sure your code works. Also, **you will need to turn in a transcript** at the end of the project.

## scoring

Each person works on nine problems. Five of these (numbers 3, 4, 6, 7, and 9)
are common to the two partners; the others are separate. You hand in a single
solution to each problem. Both partners get the points awarded to the group
for problems 3, 4, 6, 7, and 9; each person gets the points for his or her own
problems 1, 2, 5, and 8. This means that your score for the project is mostly
based on your individual work but also relies partly on the other member of
your group. The problems that are done with partners require that both
partners have already done their separate work, and meet together to
understand each other's solutions, so probably nobody will get credit for them
unless both have done their jobs.

Please indicate which person is person A and which person is person B
somewhere obvious in your file.

If you can't find a partner and are working alone, you will do both Person A
and B's parts and your grade will be their average.

## Notes on working together

Here are some suggestions to share your work with your partner:

  * [gitHub](https://github.com/). Solid, but long set-up time. [Try here](http://try.github.io/levels/1/challenges/1) for a taste
  * DropBox. Easy to set-up. Be careful with overwriting your partner's file
  * GoogleDocs. Easy to set-up. Less likely to overwrite code
  * E-Mail! Nominate one person. Send all of your code to him/her and he/she will be the one responsible for merging them together

