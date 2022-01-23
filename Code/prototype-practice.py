from abc import ABC, abstractmethod
import copy


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

if __name__ == '__main__':
    a = Circle(20)
    b = Rectangle(10, 20)

    another_circle = copy.deepcopy(a)
    print(another_circle.calculate_area())


