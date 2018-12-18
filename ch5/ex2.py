def check_fermat(a, b, c, n):
    """ If n > 2, fermat's theorem should not work
    """
    fermat_theorem = a ** n + b ** n == c ** n

    if n <= 2:
        return("'n' is not high enough to check")
    elif fermat_theorem:
        return("Holy smokes, Fermat was wrong!")
    else:
        return("No, that doesn't work.")