# Flowcharts

!!! terms "Terminology"
    - **flow arrow** – an arrow in a flowchart that shows the path the program takes, in one direction only.
    - **process block** – a rectangle in a flowchart that shows a step where the code does something, like setting a variable or doing a calculation.
    - **terminal block** – a rounded rectangle in a flowchart that shows where a program or function starts and ends.
    - **input/output block** – a parallelogram in a flowchart, also called an IO block, that shows information moving between the real world and the program.
    - **decision block** – a diamond in a flowchart that asks a question and splits the path based on the answer.
    - **loop indicator** – a grey dashed box drawn around the steps in a flowchart that repeat in a loop.
    - **function indicator** – a red dashed box drawn around the steps of a function in a flowchart.

A **flowchart** is a diagram that uses different shapes and arrows to show the steps in a process or how to solve a problem.

In programming, we use flowcharts to plan **algorithms**: step-by-step instructions for solving a problem.

## Symbols

Different shapes in a flowchart each have a special meaning.

Each shape shows a different type of step in a program.

### Flow arrows

![Flow arrow symbol](../assets/flowchart_symbols_flow.png)

Flow arrows show the path the program takes through the flowchart.

They only go in one direction, which is shown by the arrowhead.

### Process blocks

![Process symbol](../assets/flowchart_symbols_process.png)

Process blocks show the steps where your code does something in order.

For example:

- setting values for variables
- doing calculations
- running functions

They are shown as a rectangle with a short description inside.

Flows:

- inflow arrows – must have at least one, but can have more than one
- outflow arrows – must have one, and only one

### Terminal blocks

![Terminal symbol](../assets/flowchart_symbols_terminator.png)

Terminal blocks show where a process starts and ends.

They are drawn as rounded rectangles.

- For a main program, they say **“Start”** or **“End”**
- For a function, they show the function name or what value it returns

Flows:

- start terminal inflow arrows – none
- start terminal outflow arrows – must have one, and only one
- end terminal inflow arrows – must have one, and only one
- end terminal outflow arrows – none

### Input/Output (IO) blocks

![Input Output Symbol](../assets/flowchart_symbols_input.png)

Input/Output (IO) blocks show when information moves between the real world and the program.

**Input** is when information goes into the program, such as:

- typing on a keyboard
- using a mouse
- using a gamepad or joystick
- recording with a camera
- recording with a microphone

**Output** is when the computer sends information out, such as:

- showing text or images on a screen
- playing sound
- making vibrations
- printing on paper

IO blocks are drawn as parallelograms, with a short description of the input or output inside.

Flows:

- inflow arrows – must have at least one, but can have more than one
- outflow arrows – must have one, and only one

### Decision blocks

![Decision Symbol](../assets/flowchart_symbols_decision.png)

Decision blocks ask a question and then split the path based on the answer.

They are drawn as a diamond, with the question written inside.

Decision blocks are the only shape that can have more than one path coming out. Each arrow should be labelled with the answer (like “yes” or “no”) that follows that path.

Flows:

- inflow arrows – must have one, and only one
- outflow arrows – must have at least two, one for each answer

## Additional symbols

In this course, we also use two extra symbols to help show how flowcharts work:

- loop indicator
- function indicator

You do not have to use these symbols, but you can use them if they help make your flowcharts easier to understand.

### Loop indicator

![loop symbol](../assets/flowchart_symbols_loop.png)

The loop indicator is a grey box with dashed lines.

It goes around a loop and shows which steps are repeated. It starts or ends at the decision block that checks the loop condition.

### Function indicator

![function symbol](../assets/flowchart_symbols_function.png)

The function indicator is a red box with dashed lines.

It goes around a function. The function’s **start** is at the top, and the **end** is at the bottom.

No flow arrows should go into or out of the function indicator.

## Example

Below is a flowchart for a number guessing game. 

The game requirements are:

- Generate a random number between 1 and 100
- Ask the user to guess the number
- If the number is incorrect, it tells the user if they guessed too high or too low
- If the number is correct, it tells the user how many guesses they had
- Validate user input to ensure incorrect types cannot be entered
- Only accept numbers between 1 and 100
- Ask the user to play again

![flowchart example](../assets/flowchart_example.png)
