# _*_ utf-8 _*_

from math import hypot


class Vector():
    """
    define a simple 2D vector
    Vector(2, 1) + Vector(4, 1) = Vector(6, 2)
    abs(Vector(3, 4)) = 5
    Vector(3, 4) * 3 = Vector(9, 12)
    abs(Vector(9, 12)) = 15
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # also can use __str__
    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # if Vector(0, 0), means false
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(9, 12)
    v3 = v1 + v2
    print(v3)
    print(abs(v1), abs(v2), abs(v3))
    print(v1*3, abs(v1*3))
    v4 = Vector(-3, 4)
    print(v4)
    print(abs(v4))

    # TypeError, must be number not str
    v5 = Vector("3", "5")
    # print(v5, abs(v5))
   