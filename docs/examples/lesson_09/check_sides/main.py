import turtle


def draw_poly(length, sides):
    for index in range(sides):
        my_ttl.forward(length)
        my_ttl.right(360 / sides)


# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# get user input
sides = input("How many sides?> ")
if sides.isdigit():
    sides = int(sides)
else:
    print("Invalid input")
    quit()

length = int(input("How long are the sides?> "))

draw_poly(length, sides)
