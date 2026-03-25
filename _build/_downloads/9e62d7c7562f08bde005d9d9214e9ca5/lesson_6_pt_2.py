import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    my_ttl.speed(0)
    for i in range(4):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
    my_ttl.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    color = "orange"
    size = 10
    my_ttl.goto(x, y)
    my_ttl.dot(size, color)


## Main Program
my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()