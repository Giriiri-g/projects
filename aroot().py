def aroot(a, b, c):
    """3 arguments required. a,b,c as the coefficients of equation.
    Any argument left behind will be considered as Zero as default
    order mismatch will not be considered as an Error (will be considered as human Error)
    output will be given in any order of roots
    only gives algebric roots of quadratic equations"""
    x = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    y = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return (x,y)
