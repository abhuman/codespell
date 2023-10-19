import random
import turtle

# Set the screen size and title
turtle.setup(800, 600)
turtle.title("Hacktoberfest 2023")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed
t.speed(0)

# Create a list of star colors
star_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the hacktoberfest logo
t.penup()
t.goto(-100, 0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-75, 0)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()
t.goto(-50, 0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the star animation
for i in range(100):
    # Choose a random star color
    color = random.choice(star_colors)

    # Set the turtle color
    t.color(color)

    # Draw a star
    t.begin_polygon()
    t.forward(5)
    t.right(144)
    t.forward(5)
    t.right(144)
    t.forward(5)
    t.right(144)
    t.forward(5)
    t.right(144)
    t.forward(5)
    t.end_polygon()

    # Move the turtle to a random location
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-200, 200))
    t.pendown()

# Hide the turtle
t.hideturtle()

# Keep the window open until the user clicks
turtle.done()
