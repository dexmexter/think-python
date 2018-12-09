def grid(wide, tall):
    a = ("+ " + "- " * 4) 
    b = ("| " + " " * 8)
    
    a_cap = "+"
    b_cap = "|"
    
    a_row = a * wide + a_cap
    b_row = b * wide + b_cap
    
    for i in range(tall):
        print(a_row)
        print(b_row)
        print(b_row)
        print(b_row)
        print(b_row)

    print(a_row)

grid(4, 4)