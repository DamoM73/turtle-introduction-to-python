# Debugging with Thonny

Everyone makes mistakes, even experienced programmers. In this guide we will learn how to use Thonny's **debugger** to find and fix mistakes in our code.

## Programming mistakes

Python is good at finding some mistakes, like **syntax errors** (when the code breaks Python's rules) and **run-time errors** (when something goes wrong while the program is running).

There is another type of mistake called a **logic error**. This happens when our code runs without crashing, but it doesn't do what we expected.

For example, the program below is in the `guides` folder of the [tutorial files](../index.md#tutorial-files) as `buggy_code.py`.

```python linenums="1"
--8<-- "examples/guides/buggy_code/main.py"
```

The program should show `_h_e_l_l_o_`. When we run it, it actually shows `o_`. This means there is a logic error.

Logic errors cause unexpected results called **bugs**. **Debugging** is the process of finding and fixing bugs. A **debugger** is a tool that helps us track down bugs by showing what our program is doing, step by step.

## Setting up Thonny's debugger

1. Open the **View** menu and make sure there is a tick next to **Stack** and **Variables**.

    These panels show which part of the program is running and what values it has stored.

    ![Thonny View menu with Stack and Variables ticked](../assets/debugging_1.png)

2. To start the debugger, click the **Debug** button.

    ![Thonny's Debug button](../assets/debugging_2.png)

## Controlling the debugger

To learn how the debugger works, let's start with a program that has no bugs. Type the code below into Thonny and save it as `debug_names.py`.

```python linenums="1"
--8<-- "examples/guides/debug_names/main.py"
```

Now click **Debug**. Thonny should look like the image below.

![Thonny paused at the start of the program in the debugger](../assets/debugging_3.png)

- **Code panel**: Thonny has paused the program. The yellow highlight shows the next code that will run.
- **Variables panel**: no variables are shown yet, because nothing has been stored in memory.
- **Shell panel**: `%Debug` is the command Thonny used to start the program.
- **Stack panel**: shows which part of the program is currently running.

New debugging buttons are now available. Let's see how they work.

![Thonny's debugging buttons](../assets/debugging_4.png)

### Step into

1. Click **Step into**.

    Thonny runs the highlighted code. The new highlight shows what Python will run next: the list `["michelle", "nicole", "simone", "emma"]`.

    ![The list highlighted in the debugger](../assets/debugging_5.png)

2. Click **Step into** again.

    `"michelle"` is highlighted. Python is about to read this value.

3. Keep stepping.

    `"michelle"` turns blue, which shows that Python has read that value.

    ![michelle shown in blue after being read](../assets/debugging_6.png)

4. Click **Step into** four more times (or press ++f7++).

    Python has now read all of the strings.

    ![All four strings read](../assets/debugging_7.png)

5. Click **Step into** again.

    Python is ready to store the list in the variable `names`.

    ![The list ready to be stored in names](../assets/debugging_8.png)

6. Click **Step into** again.

    The **Variables** panel now shows that `names` stores `["michelle", "nicole", "simone", "emma"]`. The highlight covers the whole `for` loop, because Thonny is showing all the code that belongs to it.

    ![The Variables panel showing names](../assets/debugging_9.png)

7. Click **Step into**.

    The next part of the code to run is `names`, the first part of the `for` loop statement.

    ![names highlighted in the for statement](../assets/debugging_10.png)

8. Click **Step into** again.

    Thonny replaces `names` with the list stored inside the `names` variable.

    ![names replaced by its list](../assets/debugging_11.png)

9. Click **Step into** again.

    Because this is a `for` loop, Python reads the first item in the list (`"michelle"`).

    ![The first item in the list highlighted](../assets/debugging_12.png)

10. Click **Step into** again.

    Line 4 is highlighted. The value `"michelle"` is now stored in the variable `name`, as the **Variables** panel shows.

    ![michelle stored in name](../assets/debugging_13.png)

    !!! warning "`name` and `names`"
        Don't mix up `name` and `names`. They look similar, but Python treats them as different variables:

        - `name` is the variable used inside the `for` loop
        - `names` is the list that the loop goes through

11. Click **Step into** three more times.

    Thonny highlights `name.capitalize()`, then `name`, then replaces `name` with `"michelle"`.

    ![name replaced with michelle](../assets/debugging_14.png)

12. Click **Step into** three more times.

    The `capitalize()` method changes `"michelle"` to `"Michelle"`, and the variable `name` is updated to store `"Michelle"`. Line 4 is finished, so line 5 is highlighted next.

    ![name now stores Michelle](../assets/debugging_15.png)

13. Click **Step into** five more times.

    These steps show how Python builds the f-string and prints it in the Shell. When `print()` runs, it gives back a value called `None`.

    ![The print function returning None](../assets/debugging_16.png)

14. Click **Step into** once more.

    We're back at line 3. The `for` loop moves to the next item in the list, `"nicole"`.

    ![The loop moving to nicole](../assets/debugging_17.png)

15. Click **Step into** one more time.

    Python stores `"nicole"` in `name`. We'll use this time through the loop to explore **Step over**.

### Step over

**Step over** runs the highlighted code without showing all the small steps.

1. Look at the highlighted line 4. When it runs, it will take the value in `name` (`"nicole"`), change it to `"Nicole"`, and store the new value back in `name`.

    ![Line 4 highlighted before Step over](../assets/debugging_18.png)

2. Click **Step over**.

    The value stored in `name` has been updated in one step.

    ![name updated to Nicole](../assets/debugging_19.png)

3. Click **Step over** again.

    Line 5 runs, and the highlight returns to the `for` statement on line 3.

    !!! tip "When to use Step over"
        Use **Step over** when you're confident the highlighted code works. Skipping the parts that aren't causing problems helps us find the bug faster.

4. Click **Step over** and then **Step into** until the debugger matches the image below.

    ![The debugger inside line 4](../assets/debugging_20.png)

### Step out

**Step out** finishes the rest of the current piece of code.

1. Look at the grey box around line 4. It shows that we're inside that line of code.
2. Click **Step out**.

    Thonny jumps back out and highlights all of line 4 again.

    ![Line 4 highlighted after Step out](../assets/debugging_21.png)

3. Click **Step out** again.

    The debugger moves up one more level, outside the `for` loop, and the program finishes.

### Resume and breakpoints

The **Resume** button works with **breakpoints**. A breakpoint is a place where we tell the program to pause. **Resume** runs the program until it reaches a breakpoint.

1. Click on the line number `4`.

    A red dot appears next to the line number. This is a breakpoint.

    ![A breakpoint on line 4](../assets/debugging_22.png)

2. Click **Debug**.

    The program runs and pauses at the breakpoint. We can check the current values in the **Variables** panel.

    ![The program paused at the breakpoint](../assets/debugging_23.png)

3. Click **Resume**.

    The program keeps running and pauses at the next breakpoint. This is line 4 again, but on the second time through the loop. Notice the changed values in the **Variables** panel.

    ![The program paused at line 4 on the second loop](../assets/debugging_24.png)

Now that we know how to use Thonny's debugger, let's go back and debug `buggy_code.py`.

## Debugging a logic error

### Guess where the bug is

The first step is to find the part of the code that might have the bug. We might not know the exact line, so we make a good guess about which section could be wrong.

`buggy_code.py` has two main parts:

- a function (lines 1–5)
- the main program (lines 7–8)

Line 7 creates a variable called `phrase` with the value `"hello"`, and line 8 prints the result of `add_underscores(phrase)`. These two lines look correct, so the bug is probably in the function.

The first line inside the function (line 2) creates a variable called `new_word` with the value `"_"`. That looks correct too, so the bug is likely inside the `for` loop.

### Set a breakpoint

1. Add a breakpoint on line 3, the start of the `for` loop.

    ![A breakpoint on the for loop](../assets/debugging_25.png)

2. Click **Debug**.

    Thonny runs the program until it reaches the breakpoint.

    ![The debugger paused inside the function](../assets/debugging_26.png)

    There are some new features here:

    - **An extra debugging window**: Thonny opens a new window for the function `add_underscores("hello")`. This happens whenever Python starts running a function. The bottom of this window shows the function's **local variables**: variables that only exist inside that function.
    - **Two stack entries**: the **Stack** panel shows `<module>` (the main program) and `add_underscores` (the function). The program is at line 8 in the main program, and line 3 inside the function.

    !!! tip "Stack timeline"
        1. Line 8 in the main program calls the `add_underscores` function.
        2. Python pauses the main program at line 8 and waits for the function to finish.
        3. When the function finishes, the main program continues from line 8.

    The `add_underscores` window shows two variables: `word` is `"hello"` and `new_word` is `"_"`. These are correct so far.

    ![The function's local variables](../assets/debugging_26a.png)

3. Click **Step into** once, then **Step over** twice.

    `new_word = word[index] + "_"` is now highlighted and ready to run. The local variable `index` stores `0`, which is correct for the first time through the loop.

    ![The problem line highlighted](../assets/debugging_27.png)

    !!! tip "Can't see the index variable?"
        Make the **Local variables** panel bigger.

4. Click **Step over** to run the line.

    `new_word` now stores `"h_"`, but we wanted `"_h_"`. Part of the value was replaced instead of added to. **This is exactly where the bug happens.**

    ![new_word storing h_](../assets/debugging_28.png)

### Investigate the bug

Now we know the bug is in line 4, let's look more closely at what Python is doing there.

1. Click **Stop**, then click **Debug** again.
2. Click **Step into** once, then **Step over** twice, so line 4 is highlighted again.
3. Click **Step into** three times, checking the values each time. Everything still looks correct.

    ![Stepping into line 4, first step](../assets/debugging_29.png)

    ![Stepping into line 4, second step](../assets/debugging_30.png)

    ![Stepping into line 4, third step](../assets/debugging_31.png)

4. Keep clicking **Step into** and watch the **Local variables** panel. Stop when the window looks like the one below.

    ![Python about to store h_ in new_word](../assets/debugging_32.png)

Python is about to store `"h_"` in `new_word`. That's wrong: we want it to store `"_h_"`. Now we know exactly where the bug is, we need to work out why it's happening.

### Fix the bug

The `add_underscores()` function should put a `_` between each letter. It should do this by adding the next letter and a `_` to the value already stored in `new_word`.

But the code replaces `new_word` each time, so it loses all the letters added before. To fix this, we need to add the current value of `new_word` at the front:

```python
new_word = new_word + word[index] + "_"
```

1. Stop debugging and change line 4 to the code above.

    ![The fixed code](../assets/debugging_33.png)

2. Run the program normally.

    The Shell should show `_h_e_l_l_o_`. We have found and fixed a bug.
