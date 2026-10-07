# Lesson 2: Introducing Turtle

!!! learn "In this lesson we will learn"
    - how to import a module into our program
    - how to create a turtle and set up its window
    - how to move and turn the turtle to draw lines
    - how to draw simple shapes like squares and triangles

!!! terms "Terminology"
    - **module** – a file of ready-made code that we can import into our program to use its commands.
    - **import** – the command that tells Python to load a module so our program can use its commands.
    - **turtle** – a small arrow on the screen that we can control and move around to draw.
    - **screen** – the window that the turtle draws in.
    - **pixel** – one of the tiny dots of light that make up a screen or display.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CBrm4-ECyMI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Video link](https://youtu.be/CBrm4-ECyMI)

## Our first turtle program

Create a new file, type in the comment below, and save it as `first_turtle.py`.

```python linenums="1"
# Our first turtle program
```

Python starts with a small set of built-in commands called **functions**. It can also use extra groups of commands called **modules**. One of these modules is **turtle**.

To use a module, we need to tell Python with the `import` command. We always put `import` lines at the very top of our program.

Add line 3 so our code looks like this:

```python linenums="1" hl_lines="3"
--8<-- "examples/lesson_02/import_turtle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the code.
    2. **Run** the code. Did anything appear?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module so our program can use its commands.

Nothing appears yet. Importing a module only makes its commands available. We haven't used any of them yet.

## Create a turtle

A **turtle** is a small arrow on the screen that we can control and move around. Before we can use a turtle, we need to create one.

Add line 5 so our code looks like this:

```python linenums="1" hl_lines="5"
--8<-- "examples/lesson_02/create_turtle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the code.
    2. **Run** the code. Did a window appear?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module.
    - **line 5** → uses the `Turtle()` command from the turtle module to create a turtle, and names it `my_ttl`.

We can choose any name we like for our turtle. The name `my_ttl` is just an example. There are two rules:

- the name must be one word, with no spaces
- if we change the name, we must use the same name everywhere in our code

## Make our turtle move

Now let's make the turtle move. Add line 7 so our code looks like this:

```python linenums="1" hl_lines="7"
--8<-- "examples/lesson_02/forward/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what the turtle will do. Be specific.
    2. **Run** the code. You might have guessed the turtle would move to the right, but did you expect it to leave a line behind it?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module.
    - **line 5** → creates a turtle called `my_ttl`.
    - **line 7** → tells `my_ttl` to move forward 100 steps, drawing a line as it goes.

!!! primm "PRIMM"
    Time to **modify** the code. Can you make the turtle draw lines of different lengths?

## Changing the turtle window

Let's set up the turtle window so it looks the same on every computer. Change our code so it matches the code below. Lines 5 and 6 are new.

```python linenums="1" hl_lines="5-6"
--8<-- "examples/lesson_02/screen_setup/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what will change when we run the code.
    2. **Run** the code. Did the window change?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module.
    - **line 5** → uses the `Screen()` command from the turtle module to create the window, and names it `window`.
    - **line 6** → sets the window to 500 pixels wide and 500 pixels high.
    - **line 8** → creates a turtle called `my_ttl`.
    - **line 10** → moves `my_ttl` forward 100 steps.

In the turtle module, the window is called a **screen**. We create a screen the same way we created a turtle.

!!! tip "What are pixels?"
    Our screen is made up of lots of tiny dots. If you look very closely, you might be able to see them. These dots are called **pixels**.

    You might see screen sizes written like 1920 × 1080. This means the screen is 1,920 pixels wide and 1,080 pixels high.

Pixels are also how the turtle measures movement. When we write `forward(100)`, the turtle moves forward **100 pixels**.

## Changing the turtle's shape

Now let's change how the turtle looks. Add line 9 to our program.

```python linenums="1" hl_lines="9"
--8<-- "examples/lesson_02/shape/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what this change will do.
    2. **Run** the code. Was your guess correct?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module.
    - **lines 5–6** → create a 500 × 500 pixel window.
    - **line 8** → creates a turtle called `my_ttl`.
    - **line 9** → changes `my_ttl` from an arrow into a turtle shape.
    - **line 11** → moves `my_ttl` forward 100 steps.

## Change direction

Now that our window and turtle are ready, let's do more drawing. Add lines 12 and 13 to the bottom of our code.

```python linenums="1" hl_lines="12-13"
--8<-- "examples/lesson_02/left/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what this code will do. Be as specific as you can, and draw what you think will happen on a piece of paper.
    2. **Run** the code. Did the turtle draw the same thing as your picture?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the turtle module.
    - **lines 5–6** → create a 500 × 500 pixel window.
    - **lines 8–9** → create a turtle called `my_ttl` with a turtle shape.
    - **line 11** → moves `my_ttl` forward 100 steps.
    - **line 12** → turns `my_ttl` 90 degrees to the left.
    - **line 13** → moves `my_ttl` forward another 100 steps.

!!! primm "PRIMM"
    Time to **modify** the code. What happens when we change the numbers inside the brackets? Can you make the turtle turn right using `right()`?

## Exercises

In this course, the exercises are the **make** part of PRIMM. Work through them to make your own code.

Starter files are in the `lesson_02` folder of the tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#lesson-2-introducing-turtle) page.

### Exercise 1

Starter: `lesson_02/ex1_square`

Can you add code to the end of the starter so the turtle draws a square?

### Exercise 2

Starter: `lesson_02/ex2_triangle`

Can you add code to the end of the starter so the turtle draws an equilateral triangle (a triangle with three equal sides)?

### Exercise 3

Starter: `lesson_02/ex3_hexagon`

Can you add code to the end of the starter so the turtle draws a hexagon (a shape with six equal sides)?
