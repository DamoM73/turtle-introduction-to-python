import turtle

#################################################
## Change the variable values to draw a square ##
#################################################

screen = 500
sides = 4
length = 100

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for index in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)