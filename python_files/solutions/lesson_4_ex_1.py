import turtle

def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
    my_ttl.pendown()
    
def draw_circle(radius, colour):
    my_ttl.color("black", colour)
    my_ttl.begin_fill()
    my_ttl.circle(radius)
    my_ttl.end_fill()
    
def draw_rect(width, height, colour):
    my_ttl.color("black", colour)
    my_ttl.begin_fill()
    for index in range(2):
        my_ttl.forward(width)
        my_ttl.right(90)
        my_ttl.forward(height)
        my_ttl.right(90)
    my_ttl.end_fill()

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

move_pen(0, -200)
# draw head
draw_circle(200, "yellow")
move_pen(-75, 0)
# draw eye
draw_circle(50, "black")
move_pen(75, 0)
# draw eye
draw_circle(50, "black")
move_pen(-100, -75)
# draw mouth
draw_rect(200, 25, "black")
my_ttl.hideturtle()