import turtle

window = turtle.Screen()
window.setup(500, 500)

my_ttl = turtle.Turtle()

for side in range(1, 5):
    my_ttl.forward(100)
    my_ttl.left(90)
