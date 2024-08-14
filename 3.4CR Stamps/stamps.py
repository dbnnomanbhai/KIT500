# stamps.py

from turtle import Turtle, Screen

__author__ = 'Najmul Uddin'


def place_stamp(stamper: Turtle, x: float, y: float, ink: str) -> None:
    """
    Draws the initials letter of name Najmul Uddin so the first letter of the first name and the first letter of the surname of the name 
    'N' and 'U' with the bottom-left corner of the drawing at (x, y)
    and in the specified color.

    """

    # Save the current turtle state
    old_ink = stamper.pencolor()
    old_direction = stamper.heading()
    old_x, old_y = stamper.position()

    # Set new color and location
    stamper.pencolor(ink)
    stamper.penup()
    stamper.goto(x, y)
    stamper.pendown()

    # Draw the letter "N"
    stamper.setheading(90)  
    stamper.forward(100)    # Draw the left side of "N"
    stamper.right(135)
    stamper.forward(141.4)  # Draw the diagonal of "N"
    stamper.left(135)
    stamper.forward(100)    # Draw the right side of "N"
    
    # Move to start position for "U"
    stamper.penup()
    stamper.right(90)
    stamper.forward(70)  # Space between "N" and "U"
    stamper.pendown()

    # Draw the letter "U"
    stamper.setheading(270)  # Face down to start drawing "U"
    stamper.forward(100)    # Draw the left side of "U"
    stamper.right(90)
    stamper.forward(50)     # Draw the bottom of "U"
    stamper.right(90)
    stamper.forward(100)    # Draw the right side of "U"
    
    # Restore the turtle's previous state
    stamper.penup()
    stamper.goto(old_x, old_y)
    stamper.setheading(old_direction)
    stamper.pencolor(old_ink)
    stamper.pendown()


def main():
    screen = Screen()
    screen.bgcolor("white")

    t = Turtle()
    t.speed(1)

    # Draw initials "N" and "U" at three different locations with different colors
    place_stamp(t, -150, 100, "blue")   # Top left
    place_stamp(t, 0, -50, "red")       # Bottom center
    place_stamp(t, 150, 50, "green")    # Top right

    screen.mainloop()


if __name__ == "__main__":
    main()
