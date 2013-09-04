from fractions import Fraction
from math import modf, pi, sqrt

def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

def simplest_fraction_in_interval(x, y):
    """Return the fraction with the lowest denominator in [x,y]."""
    if x == y:
        # The algorithm will not terminate if x and y are equal.
        raise ValueError("Equal arguments.")
    elif x < 0 and y < 0:
        # Handle negative arguments by solving positive case and negating.
        return -simplest_fraction_in_interval(-y, -x)
    elif x <= 0 or y <= 0:
        # One argument is 0, or arguments are on opposite sides of 0, so
        # the simplest fraction in interval is 0 exactly.
        return Fraction(0)
    else:
        # Remainder and Coefficient of continued fractions for x and y.
        xr, xc = modf(1/x);
        yr, yc = modf(1/y);
        if xc < yc:
            return Fraction(1, int(xc) + 1)
        elif yc < xc:
            return Fraction(1, int(yc) + 1)
        else:
            return 1 / (int(xc) + simplest_fraction_in_interval(xr, yr))

def approximate_fraction(x, e):
    """Return the fraction with the lowest denominator that differs
    from x by no more than e."""
    return simplest_fraction_in_interval(x - e, x + e)

assertEqual(approximate_fraction(6.75, 0.01), Fraction(27,4))
assertEqual(approximate_fraction(pi, 0.00001), Fraction(355, 113))
print approximate_fraction((1 + sqrt(5)) / 2, 0.00001) #377/233