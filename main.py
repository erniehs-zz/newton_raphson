import math


def fun(x):
    """ the function we want to find the minimum of 
        https://www.desmos.com/calculator/uo76pxlnmx
    """
    return 2 - 10 * math.pow(x, 2) + 5 * math.pow(x, 4)


def dfundx(x):
    """ the first derivative of the function """
    return -20 * x + 20 * math.pow(x, 3)

_precision = 1e-05

def newton_raphson(x, r, maxr):
    """ for a value x with recursion leve r having max r recursions """
    y = fun(x)
    x2 = x - y / dfundx(x)
    y2 = fun(x2)
    print("\titer = {} x = {:.9f} y = {:.9f}".format(r, x2, y2))
    if math.isclose(y2, y, rel_tol=_precision, abs_tol=_precision) or (r >= maxr):
        return x2
    return newton_raphson(x2, r + 1, maxr)


if __name__ == "__main__":
    minx = newton_raphson(5, 1, 100)
    print("\n\rmin at x = {:.9f}, precision = {}".format(minx, _precision))

    minx = newton_raphson(0.5, 1, 100)
    print("\n\rmin at x = {:.9f}, precision = {}".format(minx, _precision))

    minx = newton_raphson(-0.5, 1, 100)
    print("\n\rmin at x = {:.9f}, precision = {}".format(minx, _precision))

    minx = newton_raphson(-5, 1, 100)
    print("\n\rmin at x = {:.9f}, precision = {}".format(minx, _precision))
