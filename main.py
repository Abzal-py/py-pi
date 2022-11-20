from math import pi


def circle_area(radius):
    if radius <0 :
        raise ValueError("Radius can't be negative")
    if type(radius) not in [int,float]:
        raise TypeError("Wrong type of radius")
    return pi*radius**2

