# Interactivity

To add an interactive multiple-choice question, copy and paste the following block of HTML code into your Markdown file:
```html
<div class="mc">
What is your name?

<pre><code>(any code
goes in a block like this)
</code></pre>
<ans text="Answer A" explanation="Explanation A" correct></ans>
<ans text="Answer B" explanation="Explanation B"></ans>
<ans text="Answer C" explanation="Explanation C"></ans>
<!-- and so on -->
</div>
```

In this case, the question is "What is your name?", and the correct answer is A.

Of course, you shouldn't always make Answer A the correct answer.

## Important!

The three important things to remember are:

1. Markdown does **not** work inside these blocks.
2. There can be only **one** correct answer per question.
3. These blocks will **not** render correctly in GitHub's Markdown preview.

## Example

See [this page](https://berkeley-cs61as.github.io/textbook/what-is-emacs.html) for a demo of an interactive MC question.

The source is [here](https://github.com/berkeley-cs61as/markdown-courseware/blob/master/textbook/chapter02%20Emacs%20Tutorial/section01%20What%20is%20Emacs.md) (click "Raw" or "Edit" to view source).

