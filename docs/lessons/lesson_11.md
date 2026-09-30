# Lesson 11: Boolean Logic

!!! learn "In this lesson we will learn"
    - what Boolean values are
    - how comparison operators give back `True` or `False`
    - how to use the Boolean operators `not`, `and` and `or`
    - how to join comparisons to build more powerful conditions

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/5GrokwhCXXM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Video link](https://youtu.be/5GrokwhCXXM)

## Booleans

In programming, **Boolean** means working with two possible values: `True` and `False`.

- a Boolean variable can only store `True` or `False`
- comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) check something and give back `True` or `False`
- Boolean operators (we'll learn these soon) also give back `True` or `False`

`True` and `False` are special words in Python. When we type them in Thonny, they're coloured differently to show they're special.

## Comparison operators

The conditions in `if` and `while` statements check whether something is `True` or `False`, using **comparison operators**. Let's quickly review them. Create a new file, type in the code below, and save it as `boolean_logic.py`.

```python linenums="1"
--8<-- "examples/lesson_11/comparisons/main.py"
```

!!! primm "PRIMM"
    1. **Predict** the six results. Each one will be either `True` or `False`.
    2. **Run** the code. Were your predictions correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → prints whether `"jeff"` is equal to `"jeff"`.
    - **line 2** → prints whether `1` is not equal to `1`.
    - **line 3** → prints whether `500` is greater than `300`.
    - **line 4** → prints whether `100` is greater than or equal to `250`.
    - **line 5** → prints whether `"a"` is less than `"q"`. For letters, "less than" means "comes earlier in the alphabet".
    - **line 6** → prints whether `-30` is less than or equal to `3`.

!!! primm "PRIMM"
    Time to **modify** the code. Can you change the values so each result switches: every `True` becomes `False`, and every `False` becomes `True`?

Comparisons work the same way whether the values are typed straight into the code or stored in variables. Change our code so it matches the code below.

```python linenums="1"
--8<-- "examples/lesson_11/score/main.py"
```

!!! primm "PRIMM"
    1. **Predict** whether the code will print `True` or `False`.
    2. **Run** the code. Was your prediction correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → stores `10` in `score`.
    - **line 2** → prints whether the value in `score` is greater than `5`.

## Boolean operators

**Boolean operators** work a bit like maths, but instead of numbers they use `True` and `False`, and the result is always `True` or `False`. They're useful when we want to check more than one thing at the same time. There are three: `not`, `and` and `or`.

### The `not` operator

The easiest operator is `not`. It flips the value: `not True` is `False`, and `not False` is `True`. Change our code so it matches the code below.

```python linenums="1"
--8<-- "examples/lesson_11/not/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what the Shell will show.
    2. **Run** the code. Was your prediction correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → prints `not True is:` followed by the result of `not True`, which is `False`.
    - **line 2** → prints `not False is:` followed by the result of `not False`, which is `True`.

### The `and` operator

The `and` operator only gives back `True` if **every** value is `True`. Change our code so it matches the code below.

```python linenums="1"
--8<-- "examples/lesson_11/and/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what the Shell will show.
    2. **Run** the code. Were your predictions correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → prints `True`, because both values are `True`.
    - **line 2** → prints `False`, because one value is `False`.
    - **line 3** → prints `False`, because one value is `False`.
    - **line 4** → prints `False`, because both values are `False`.
    - **line 5** → prints `True`, because all three values are `True`.
    - **line 6** → prints `False`, because one of the three values is `False`.

### The `or` operator

The `or` operator works the opposite way to `and`. It gives back `True` if **at least one** value is `True`. Change our code so it matches the code below.

```python linenums="1"
--8<-- "examples/lesson_11/or/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what the Shell will show.
    2. **Run** the code. Were your predictions correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → prints `True`, because at least one value (in fact both) is `True`.
    - **line 2** → prints `True`, because one value is `True`.
    - **line 3** → prints `True`, because one value is `True`.
    - **line 4** → prints `False`, because no values are `True`.
    - **line 5** → prints `True`, because all three values are `True`.
    - **line 6** → prints `True`, because one of the three values is `True`.

## Joining comparisons

Using `True` and `False` on their own isn't very useful. But remember, comparison operators give back `True` or `False`. So we can use Boolean operators to join comparisons together, and build more powerful conditions for our `if` and `while` statements. Change our code so it matches the code below.

```python linenums="1"
--8<-- "examples/lesson_11/combined/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what the Shell will show.
    2. **Run** the code. Was your prediction correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → works out both comparisons first (`7 < 8` is `True`, and `"a" < "o"` is `True`), then works out `True and True`, and prints the result, `True`.

!!! warning "Comparisons on both sides"
    When we join comparisons, we need a full comparison on **both sides** of the Boolean operator.

    - `score > 5 and score < 13` is correct: both sides are comparisons.
    - `score > 5 and < 13` is a `SyntaxError`, because the second part isn't a full comparison.
    - `score == 5 or score == 13` checks whether `score` is 5 or 13. Writing `score == 5 or 13` runs, but doesn't do what we expect: an `if` statement using it always runs its code, because Python treats `13` on its own as `True`.

## Exercises

In this course, the exercises are the **make** part of PRIMM. Work through them to make your own code.

Starter files are in the `lesson_11` folder of the tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#lesson-11-boolean-logic) page.

### Exercise 1

Starter: `lesson_11/ex1_all_true`

Each line in this program prints `False`. Can you change the values so every line prints `True`? Only change the numbers and the Boolean values.

### Exercise 2

Starter: `lesson_11/ex2_pass_mark`

Can you write a program that asks the user for their test score out of 100, then prints `True` if the score is a pass (from 50 to 100), and `False` if it isn't? Use `and` to join two comparisons.

### Exercise 3

Starter: `lesson_11/ex3_weekend`

Can you write a program that asks the user what day it is, then prints `True` if it's Saturday or Sunday, and `False` if it isn't? Use `or` to join two comparisons.
