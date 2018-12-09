import turtle
import math

def constants(n, r):
    """Creates a dictionary with all
    the sides and angles for the triangle
    inside a polygon with n sides and r (radius)
    """
    variables = {}
    
    inner_angle = 360 / n 
    outer_angle = (180 - inner_angle) / 2
    # The inner and outer sides can be found using a
    # bisected triangle.
    
    inner_side = r * math.sin(math.radians(90)) \
     / math.sin(math.radians(outer_angle))

    outer_side = 2 * \
    (r * math.sin(math.radians(inner_angle / 2)) \
     / math.sin(math.radians(outer_angle)))
    
    variables["inner_angle"] = inner_angle
    variables["outer_angle"] = outer_angle
    variables["inner_side"] = inner_side
    variables["outer_side"] = outer_side

    return variables

def pie(t, n, r):
    """draws (using t: Turtle) a polygon pie with 
    n sides and r radius
    """
    variables = constants(n, r)
    t.rt(variables["inner_angle"] / 2)
    
    for i in range(n):
        t.fd(variables["inner_side"])
        t.rt(180 + variables["outer_angle"])
        t.fd(variables["outer_side"])
        t.rt(180 + variables["outer_angle"])
        t.fd(variables["inner_side"])
        t.rt(180)
    
    t.lt(variables["inner_angle"] / 2)

if __name__ == "__main__":
    bob = turtle.Turtle()
    r = 50

    bob.pu()
    bob.bk(r * 2 + 20)
    bob.pd()
    pie(bob, 5, r)
    
    bob.pu()
    bob.fd(r * 2 + 20)
    bob.pd()
    pie(bob, 6, r)

    bob.pu()
    bob.fd(r * 2 + 20)
    bob.pd()
    pie(bob, 7, r)
    
    turtle.mainloop()