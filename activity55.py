import turtle

# Set up the screen and turtle
screen = turtle.Screen()
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units
    pen.right(90)     # Turn right by 90 degrees

# Close the turtle graphics window when clicked
screen.mainloop()
