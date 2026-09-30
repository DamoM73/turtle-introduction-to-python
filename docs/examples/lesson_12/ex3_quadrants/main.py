# Exercise 3
# Can you use if, elif and else so each quadrant has its own colour? The dot
# should be:
#
# - red in the top-right quadrant
# - blue in the top-left quadrant
# - yellow in the bottom-left quadrant
# - green in the bottom-right quadrant
#

import turtle


def set_scene():
    turtle.setup(800, 600)
    turtle.onscreenclick(draw_dot)
    my_ttl.speed(0)
    for index in range(2):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
        my_ttl.forward(300)
        my_ttl.back(300)
        my_ttl.right(90)
    my_ttl.penup()


def draw_dot(x, y):
    print(x, y)
    color = "orange"
    size = 10
    my_ttl.goto(x, y)
    my_ttl.dot(size, color)


my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()
turtle.done()
