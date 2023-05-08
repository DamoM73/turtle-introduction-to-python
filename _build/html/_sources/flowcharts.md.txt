# Flowcharts

A flowchart is a type of diagram that uses different types of boxes and arrows to show the steps in a process or how to solve a problem. In programming we use flowcharts to map out algorithms.

## Symbols

The different boxes have meanings in a flowchart. Each represent different processes in our program.

### Process

![process symbol](./assets/flowchart_symbols_process.png)

Process blocks contain all the internal sequential commands of your code.

For example:

- variable assignments
- calculations
- function calls

They are reprented using a rectangle with with the description inside.

Flows:

- **inflow arrows** - must have at least one, but can have many
- **outflow arrows** - must have one and can only have one

### Terminal

![Terminal symbol](./assets/flowchart_symbols_terminator.png)

Terminal blocks start and end a process. If starting or ending a main program, they contain the words "Start" or "End". If starting or ending a function, they contain the name of the funtions or the return value.

Flows:

- **start terminal inflow arrows** - can only have none
- **start terminal outflow arrows** - must have one and can only have one
- **end terminal inflow arrows** - must have one and can only have one
- **end terminal outflow arrows** - can only have none