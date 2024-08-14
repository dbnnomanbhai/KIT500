"""
2.1PP Turtle Graphics
"""

__author__ = "Najmul Uddin"  # my first and last name will be N U

import turtle    

def main():
    turtle.setup(400, 400)
    turtle.speed(5)  
    turtle.pensize(2)
    #set color 
    turtle.color("Red")

    # Draw the letter for  N
    turtle.penup()
    turtle.setpos(-100, 100)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(200)
    turtle.penup()
    turtle.setpos(-100, 100)
    turtle.pendown()
    turtle.setheading(315)
    turtle.forward(282)
    turtle.penup()
    turtle.setpos(-100 + 200, 100)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(200)

 
    turtle.penup()
    turtle.setpos(50, 100)
    turtle.pendown()

    # Draw the letter U
    turtle.setheading(270)
    turtle.forward(180)
    turtle.circle(90, 180)
    turtle.forward(180)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
