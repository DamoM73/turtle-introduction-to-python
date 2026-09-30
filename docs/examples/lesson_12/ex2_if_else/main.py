# Exercise 2
# Can you use if and else so the dot is red when we click in the top-right
# quadrant, and green when we click anywhere else?
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
