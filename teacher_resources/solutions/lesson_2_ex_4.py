import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

#################################################
## Draw a circle (hint - you only need 3 lines ##
#################################################

for side in range(1,361):
    my_ttl.forward(1)
    my_ttl.left(1)