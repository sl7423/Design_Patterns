from abc import ABC, abstractmethod

class Graphic:
    def move(self, x,y):
        pass

    def draw(self):
        pass

class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"{self.x} * {self.y}")

class Circle(Dot):

    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Drawn circle with {self.x}, {self.y}, and radius {self.radius}")



class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self.children:
            self.children.append(obj)

    def draw(self):
        for child in self.children:
            child.draw()

    def remove(self, obj):
        index = self.children.index(obj)
        del self.children[index]

    def move(self, x, y):
        for child in self.children:
            child.x += x
            child.y += y


all = CompoundGraphic()
all.add(Dot(1,2))
all.add(Circle(5,3,10))
all.move(1,2)
all.draw()
