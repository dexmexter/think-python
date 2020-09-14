def is_power(a, b):
    if a < 1 or b < 1:
        return "Intergers given must be greater than zero."
    if a / b == 1:
        return True
    
    if a % b == 0:
        return is_power(a / b, b)

    return False

print(is_power(2, 256))