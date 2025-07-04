import turtle


def draw_poly(length, sides, color):
    my_ttl.color("black", color)
    my_ttl.begin_fill()
    for i in range(sides):
        my_ttl.forward(length)
        my_ttl.right(360 / sides)
    my_ttl.end_fill()


############################################
## adjust the get_number code so it loops ##
## until the user provides a valid input  ##
############################################


def get_number(prompt):
    while True:
        num = input(prompt)
        if num.lstrip("-").isdigit():
            return int(num)
        else:
            print("Invalid input")



###########################################
## adjust the get_color code so it loops ##
## until the user provides a valid input ##
###########################################


def get_color():
    while True:
        color = input("Fill colour (red, blue, green)?> ").lower()
        if color == "red":
            return color
        elif color == "blue":
            return color
        elif color == "green":
            return color
        else:
            print("Invalid input")


def move_pen():
    x_val = get_number("x axis position?> ")
    y_val = get_number("y axis position?> ")
    my_ttl.penup()
    my_ttl.goto(x_val, y_val)
    my_ttl.pendown()


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("Length of sides?> ")
fill = get_color()

move_pen()
draw_poly(size, num_sides, fill)