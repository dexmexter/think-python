import turtle
import math

def square(t, length):
    """Takes a turtle object and draws a square"""
    for i in range(4):
        bob.fd(length)
        bob.lt(90)

def polyline(t, sides, length, angle):
        for i in range(sides):
                t.fd(length)
                t.lt(angle)

def polygon(t, length, sides):
    """Takes a turtle object and draws a polygon"""
    angle = 360.0 / sides
    polyline(t, sides, length, angle)

def arc(t, radius, angle_drawn):
    arc_length = 2 * math.pi * radius * angle_drawn / 360
    sides = int(arc_length / 4) + 3    
    step_angle = float(angle_drawn) / sides
    step_length = arc_length / sides

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc

    t.lt(step_angle / 2)
    polyline(t, sides, step_length, step_angle)
    t.rt(step_angle / 2)

def circle(t, radius):
    arc(t, radius, 360)

if __name__ == "__main__":
    bob = turtle.Turtle()
    
    # draw circle centered on origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # wait for user to close window
    turtle.mainloop()