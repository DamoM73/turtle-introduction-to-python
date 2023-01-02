---
marp: true
---

# A Turtle Introduction to Python

Lesson 1

---

## Topics

- how to setup your programming environment
- how to run your first program
- how to use comments in Python
- dealing with error messages
- how to import modules
- how to create a simple turtle program


---

## Part 1

*Thonny Introduction*

---

### What is Thonny

Thonny &rarr; the IDE (integrated development environment) we will use.

- a Python IDE for beginners
- packaged with Python &rarr; helps with setup
- download it from **thonny.org**

Important distinction:

- Python &rarr; the programming language we will use
- Thonny &rarr; the program we use to write it  

Similar to:

- English &rarr; the language we use
- Microsoft Word &rarr; the program we use to write it

---

Python programs consists of text files called scripts.

Any text editor can write Python.

IDEs offer extra features, for example

- highlighting syntax
- debugging help

---

### Setting up Thonny

Need to turn on features, so our IDEs looks the same.

**View** menu &rarr; tick beside **Assistant**, **Shell** and **Variable**.

![View Settings](../assets/thonny_view_settings.png)

---

**Tools** &rarr; **Options**

![Options](../assets/thonny_tools_options.png)

---

**Editor** tab &rarr; check-boxes as below.

![Options editor](../assets/thonny_options_editor.png)

---

**Theme and Font** tab &rarr; **Syntax theme** &rarr; **IDLE Classic**

![Options theme](../assets/thonny_options_theme.png)


---

### The User Interface

![UI](../assets/thonny_ui.png)

---

### First Program

For our first program we are going to make a simple program called *hello world.* This is the traditional first program to write.

Type the following code into the Code panel:

``` python
# Our First Program

print("Hello World")
```

---

### PRIMM

We will use the **PRIMM** process:

**PRIMM** stands for:

- Predict
- Run
- Investigate
- Modify
- Make

PRIMM &rarr; reflects effective programming practices
PRIMM &rarr; encourages curiosity in programming

---

Apply **PRIMM** process

- Predict &rarr; what do you think will happen?
- Run &rarr; click the **Play button** (or **F5**).

---

```
Hello World
```

Is this what you predicted?

Let's **investigate** what happened.

---

### Investigate

Looking at code

- only `Hello World` appears in the terminal
- completely misses `# Our First Program`.
- `#` character &rarr; the line is a **comment**

> Computers ignore comments
> Good way to add notes to code.

---

`Line 3` &rarr; `print` is purple

- Syntax highlighting
- Purple &rarr; a Python keyword
- Removing the `n` so the line &rarr; `prit("Hello World")`
- Notice `prnt` &rarr; no longer purple
- **Predict** what will happen and then **Run** the code

---

Error message in your **Shell**:

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'prnt' is not defined
```

- `Line 1`: `Traceback (most recent call last):` &rarr; "this is where I got up to"
- `Line 2`: `File "<string>", line 3, in <module>` &rarr; file and the line of error
- `Line 3`: `NameError: name 'prnt' is not defined` &rarr; type of error.
  - `NameError` &rarr; found a word that it doesn't understand.
  - Word it doesn't understand &rarr; `prnt`.

---

Fix up `line 3` &rarr; `print("Hello World")` 

- Notice that `print` &rarr; purple.

Continue **investigation**:

- Remove the two `"` 
  - `line 3` &rarr; `print(Hello World)`
- **Predict** what will happen and then **Run** the code

---

**Shell** contains a different error:

```
Traceback (most recent call last):
  File "<string>", line 3
    print(Hello World)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

- `Line 3` &rarr; specific line with the error `print(Hello World)`
- `Line 4` &rarr; `^` point to error location
- `Line 5` &rarr; `SyntaxError: invalid syntax. Perhaps you forgot a comma?`:
  - error is a `SyntaxError: invalid syntax.` &rarr; code does not follow the rules
  - suggestion &rarr; `Perhaps you forgot a comma?` (wrong in this case)

---

Change `line 3` &rarr; `print("Hello World")`

- `"Hello World"` turns green 
- **Syntax highlighting** &rarr; `Hello World` is a **string**
- strings are a whole bunch of characters

---

Continue  **Investigation**:

- `line 3` &rarr; remove `(` and `)` characters
- reads &rarr; `print Hello World`
- **Predict** what will happen and then **Run** the code

---

Error in **Shell**:

```
Traceback (most recent call last):
  File "<string>", line 3
    print "Hello World"
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

- different `SyntaxError` &rarr; `Missing parentheses in call to 'print'`.
- parentheses &rarr; curved brackets
- this time hint is correct `Did you mean print(...)?`

---

Continue  **Investigation**:

- replace the opening parenthesis `(`
  - `line 3` &rarr; `print("Hello World"`.
- **Predict** what will happen and then **Run** the code

---

Error in **Shell**:

``` 
Traceback (most recent call last):
  File "<string>", line 3
    print ("Hello World"
          ^
SyntaxError: '(' was never closed
```

- error message &rarr; failed to close parenthesis.
  - every opening parenthesis `(` needs matching closing parenthesis `)`.
- Look at code in Thonny
  - grey highlight from the `(` onwards
  - **syntax highlighting** &rarr; an opening parenthesis was not closed

---

Fix `line 3` &rarr; `print("Hello World")`.

Investigation concluded.

Error messages:

- don't be discouraged
- the most experienced programmers get error messages

**Error messages are your friend, they help you to work out what went wrong**

---

### Modify

Time to **modify** the code.

Making the code print different things to the **Shell**.

---

## Part 2: 

*Introducing turtle*

---

### First turtle program

1. Click the **New** icon
2. Type the below into the new file 
3. Save it using the name **`lesson_1_pt_1.py`**.

``` python
# Our first turtle program
```

---

Python has limited set of commands (**functions**)

Access to extra commands (called **modules**)

- **Turtle** is one of those modules
- to access other modules &rarr; use the `import` command.

``` python
# Our first turtle program

import turtle
```

---

### Create a turtle

Turtle &rarr; little arrow that you can program

Before programming need to make one

``` python
# Our first turtle program

import turtle

my_ttl = turtle.Turtle()
```

---

`my_ttl = turtle.Turtle()`

- `turtle.Turtle()` tells Python:
  - from the **turtle** module you imported (`turtle`)
  - use the command `Turtle()` to create a turtle.
- `my_ttl =` names your created turtle `my_ttl`.

Name turtle anything

- can **only be a one word name**
- replace `my_ttl` with your name

---

### Make your turtle move

``` python
# Our first turtle program

import turtle

my_ttl = turtle.Turtle()

my_ttl.forward(100)
```

**Predict** and **run** the program

---

PRIMM

- **Prediction**
  - probably predicted movement to the right
  - did you predict the line?
- **Investigate** &rarr; changing things and see what happens.
- **Modify** &rarr; make lines of different length

---

### Changing the turtle environment

Change the Turtle environment &rarr; consistent between all our computers.

- make the Turtle window the same size

``` python
# Our first turtle program

import turtle

window = turtle.Screen()
window.setup(500, 500)

my_ttl = turtle.Turtle()

my_ttl.forward(100)
```

---

The window is called a **Screen**

`window = turtle.Screen()`

- `turtle.Screen()` &rarr; use `Screen()` from **turtle** module (`turtle.`) to create window
- `window =` give created window the name `window`

`window.setup(500,500)` 

- set the size of `window`
  - 500 pixels wide
  - 500 pixels high

---

### What are pixels?

Screen &rarr; thousands of little dots &rarr; **pixels**.

Screen measurement of 1920 x 1080 &rarr; 1,920 pixels wide and 1,080 pixels high.

Pixels &rarr; our measurement of movement on the screen

- `forward(100)` &rarr; move forward `100` pixels.

---

Small aesthetic change

``` python
# Our first turtle program

import turtle

window = turtle.Screen()
window.setup(500, 500)

my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

my_ttl.forward(100)
```
 
**Predict** and **run** the program

---

### Change direction

Lets do more drawing

``` python
# Our first turtle program

import turtle

window = turtle.Screen()
window.setup(500, 500)

my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

my_ttl.forward(100)
my_ttl.left(90)
my_ttl.forward(100)
```
---

PRIMM

- **Predict**: What do you think will happen?
  - be specific
  - draw it on paper
- **Run**: 
  - did it follow your prediction?
  - did it look the same as your drawing?
- **Investigate**: 
  - try changing the values within the brackets

---

## Exercises

Exercises are the **make** component of the **PRIMM** model

Complete exercises 1 - 3
