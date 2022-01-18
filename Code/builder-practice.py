from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from enum import Enum

class Engine(Enum):
    sports, sedan = 1, 2


class Builder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self):
        pass
    
    @abstractmethod
    def setEngine(self):
        pass

    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGPS(self):
        pass

class CarBuilder(Builder):
    
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def get_product(self):
        product = self._product
        self.reset()
        return product

    def setSeats(self, num):
        if isinstance(num, int):
            self._product.add(f"added {num} Seats!")
        else:
            raise TypeError("Please enter a number!")

    def setEngine(self, engineType):
        print(engineType)
        if engineType in Engine._member_names_:
            self._product.add(f"set Engine as {engineType}")
        else:
            raise TypeError("Please enter a correct engine type!")

    def setTripComputer(self):
        self._product.add("set Trip Computer!")

    def setGPS(self):
        self._product.add("set GPS!")


class ManualBuilder(Builder):
    
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Manual()

    @property
    def get_manual(self):
        product = self._product
        self.reset()
        return product

    def setSeats(self):
        self._product.add("set Seat Manual!")

    def setEngine(self):
        self._product.add("set Engine Manual!")

    def setTripComputer(self):

        self._product.add("set Trip Computer Manual!")

    def setGPS(self):
        self._product.add("set GPS Manual!")


class Car:
    def __init__(self):
        self.parts = []
    
    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Manual:
    def __init__(self):
        self.parts = []
    
    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Manual includes: {', '.join(self.parts)}", end="")

class Director:
    def __init__(self):
        self._builder = None

    @property
    def setBuilder(self):
        return self._builder  

    @setBuilder.setter
    def builder(self,builder:Builder):
        self._builder = builder 

    def construct_car(self,engineType):
        self.builder.setSeats(4)
        self.builder.setEngine(engineType)
        self.builder.setTripComputer()
        self.builder.setGPS()

    def construct_manual(self):
        self.builder.setSeats()
        self.builder.setEngine()
        self.builder.setGPS()


def Application():
    director = Director()
    builder = CarBuilder()
    director.builder = builder

    print("Building a car")
    engine_style = input("Please enter the type of engine you want? (sports, sedan)? ")
    director.construct_car(engine_style)
    builder._product.list_parts()

    print("\n")

    builder = ManualBuilder()
    director.builder = builder

    print("Add the manual!")
    director.construct_manual()
    builder._product.list_parts()

    print("\n")


if __name__ == "__main__":

    Application()    