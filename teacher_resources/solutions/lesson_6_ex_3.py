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

    ##################################
    ######## Answer goes here ########
    ##################################
    """ Part C
    Use 'if', 'elif' and 'else' keywords to set the dot color to
    red when the mouse is clicked in the top right quadrant,
    blue in the top left quadrant, yellow in the bottom left quadrant
    and green in the bottom right quadrant
    """
    
    if x > 0 and y > 0:
        color = "red"
    elif x < 0 and y > 0:
        color = "blue"
    elif x < 0 and y < 0:
        color = "yellow"
    elif x > 0 and y < 0:
        color = "green"

    ##################################
    ##################################
    ##################################

    my_ttl.goto(x, y)
    size = 10
    my_ttl.dot(size, color)


my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()