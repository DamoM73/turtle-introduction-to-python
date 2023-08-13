import turtle

def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
    my_ttl.pendown()
    
def draw_circle(radius, colour):
    my_ttl.color(colour, colour)
    my_ttl.begin_fill()
    my_ttl.circle(radius)
    my_ttl.end_fill()
    
def draw_rect(width, height, colour):
    my_ttl.color(colour, colour)
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
## Use you knowledge of Python and Turtle ##
## to draw a car. Use functions to ensure ##
## that you Do not Repeat Yourself.       ##
############################################

# draw body
move_pen(-200,0)
draw_rect(400,100,"red")
move_pen(-100,100)
draw_rect(200,100,"red")

# draw glass
move_pen(-90,90)
draw_rect(80,80,"cyan")
move_pen(10,90)
draw_rect(80,80,"cyan")

# draw wheels
move_pen(-100,-150)
draw_circle(50,"black")
move_pen(100,-150)
draw_circle(50,"black")

# draw hubs
move_pen(-100,-125)
draw_circle(25,"silver")
move_pen(100,-125)
draw_circle(25,"silver")

# draw headlights
move_pen(200,-25)
draw_rect(10,25,"yellow")

# draw bumpers
move_pen(175,-75)
draw_rect(40,10,"silver")
move_pen(-215,-75)
draw_rect(40,10,"silver")

my_ttl.hideturtle()