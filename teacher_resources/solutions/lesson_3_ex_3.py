import turtle

###################################################
## Change the variable values to draw a pentagon ##
###################################################

screen = 500
sides = 5
length = 50

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for index in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)