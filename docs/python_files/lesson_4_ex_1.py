import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

############################################
## Convert the code below using functions ##
############################################

# move pen
my_ttl.penup()
my_ttl.goto(0, -200)
my_ttl.pendown()

# draw head
my_ttl.color("black", "yellow")
my_ttl.begin_fill()
my_ttl.circle(200)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-75, 0)
my_ttl.pendown()

# draw eye
my_ttl.color("black", "black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(75, 0)
my_ttl.pendown()

# draw eye
my_ttl.color("black", "black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-100, -75)
my_ttl.pendown()

# draw mouth
my_ttl.color("black", "black")
my_ttl.begin_fill()
for index in range(2):
    my_ttl.forward(200)
    my_ttl.right(90)
    my_ttl.forward(25)
    my_ttl.right(90)
my_ttl.end_fill()

my_ttl.hideturtle()