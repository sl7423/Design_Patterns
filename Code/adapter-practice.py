from abc import ABC, abstractmethod

class Roundhole:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return f'The radius of the roundhole is {self.radius}'

    def fits(self, RoundPeg) -> None:
        if RoundPeg.getRadius() <= self.radius:
            print("The round peg fits the roundhole!")
        else:
            print("It doesn't fit, please find another item that fits.")

class RoundPeg:
    def __init__(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

class SquarePeg:
    def __init__(self, width):
        self.width = width

    def getWidth(self):
        return self.width


class SquarePegAdaptor:
    def __init__(self, value):
        self.class_roundpeg = RoundPeg(value)

    def getRadius(self):
        return self.class_roundpeg.getRadius()

def main():
    hole = Roundhole(5)
    rpeg = RoundPeg(5)
    hole.fits(rpeg)

    small_sqpeg = SquarePeg(5)
    small_adapt = SquarePegAdaptor(5)
    print(small_adapt.getRadius())
    hole.fits(small_adapt) #In an update, we can change this typechecking

if __name__ == "__main__":
    main()
