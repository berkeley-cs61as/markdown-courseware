# Interactivity

To add an interactive multiple-choice question, copy and paste the following block of HTML code into the Markdown file:
```html
<div class="mc">
The question is here.

<pre><code>(any code
goes in a block like this)
</code></pre>
<ans text="Answer A" explanation="Explanation A" correct></ans>
<ans text="Answer B" explanation="Explanation B"></ans>
<ans text="Answer C" explanation="Explanation C"></ans>
<!-- and so on -->
</div>
```
For this question, the correct answer is Answer A.

The three important things to remember are:

1. Markdown does **not** work inside these blocks.
2. There can be only **one** correct answer per question.
3. These blocks will **not** render correctly in GitHub's Markdown preview

