import turtle

window = turtle.Screen()
window.setup(500, 500)

my_ttl = turtle.Turtle()

for number in range(1, 201):
    my_ttl.forward(number)
    my_ttl.left(91)
