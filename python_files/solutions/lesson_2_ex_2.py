import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

################################
## Draw a Triangle in 3 lines ##
################################

for side in range(1,4):
    my_ttl.forward(100)
    my_ttl.left(120)