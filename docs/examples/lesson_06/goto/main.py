import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

# shape parameters
sides = 6
length = 100
CIRCLE_DEG = 360

my_ttl.goto(0, 125)

# draw shape
# for index in range(sides):
#     my_ttl.forward(length)
#     my_ttl.left(CIRCLE_DEG / sides)
