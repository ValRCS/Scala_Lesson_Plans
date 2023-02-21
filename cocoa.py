# import turtle

# # Set up the turtle window and background color
# turtle.setup(500, 500)
# turtle.bgcolor("white")

# # Set the pen color and thickness
# turtle.pensize(5)
# turtle.pencolor("brown")

# # Draw the cup outline
# turtle.penup()
# turtle.goto(-100, 0)
# turtle.pendown()
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(150)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(150)

# # Draw the handle
# turtle.penup()
# turtle.goto(-60, 70)
# turtle.pendown()
# turtle.right(90)
# turtle.circle(50, 180)

# # Draw the steam
# turtle.penup()
# turtle.goto(20, 150)
# turtle.pendown()
# turtle.right(180)
# turtle.circle(20, 180)

# # Hide the turtle
# turtle.hideturtle()

# # Exit on click
# turtle.exitonclick()

import turtle

# Set up the turtle window and background color
turtle.setup(500, 500)
turtle.bgcolor("white")

# Set the pen color and thickness
turtle.pensize(5)
turtle.pencolor("brown")

# Draw the cup outline
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.forward(200)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(150)

# Draw the handle
turtle.penup()
turtle.goto(100, 60)
turtle.pendown()
turtle.right(180)
turtle.circle(-50, -180)

# Hide the turtle
turtle.hideturtle()

# Exit on click
turtle.exitonclick()