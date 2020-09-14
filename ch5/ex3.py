def is_triangle(a, b, c):
    """Takes three positive numbers and checks to see 
    if they can be combined to make a triangle.
    """
    no = "Sorry, these numbers cannot make a triangle"
    yes = "These numbers can successfully make a triangle"
    if a >= b and a >= c:
        if a > b + c:
            return no
        else:
            return yes
    elif b >= a and b >= c:
        if b > a + c:
            return no
        else:
            return yes
    else:
        if c > a + b:
            return no
        else:
            return yes

def user_num():
    """ Creates a variable with a user-defined number
    and checks if the user actually gave a positive number
    """
    while True:
        try:
            x = float(input("Your choice?\n"))
            break
        except ValueError:
            pass
        print("That's not a number, please try again.")
    
    if x <= 0:
        print("Your number must be greater than zero.")
        x = user_num()
    
    
    return x

def three_user_sides():
    """ Uses user_num to create a user defined number
    and uses those integers as arguments for is_triangle
    """
    print("Please choose the first number.")
    a = user_num()
    print("\n")
    
    print("Please choose the second number.")
    b = user_num()
    print("\n")
    
    print("Please choose the third number.")
    c = user_num()

    print("\n")
    return is_triangle(a, b, c)

print(three_user_sides())