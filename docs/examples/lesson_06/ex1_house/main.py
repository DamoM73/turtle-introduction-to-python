# Exercise 1
# Can you draw a house made up of several shapes, using the turtle commands
# you've learnt? Try to keep your code DRY (Don't Repeat Yourself) by using
# loops where you can.
#

import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")
