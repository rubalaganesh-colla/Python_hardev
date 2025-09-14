import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("lightgreen")
my_wn.title("My Turtle Program")
my_pen = turtle.Turtle()
size = 0
while True:     
    for i in range(12):
        my_pen.forward(size + 1)
        my_pen.left(90)
        size = size - 5
    size = size + 1  




