from abc import ABC, abstractmethod

class Strategy(ABC):
    @classmethod
    @abstractmethod
    def execute(cls):
        pass

class ConcreteStrategyAdd(Strategy):
    @classmethod
    def execute(cls, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    @classmethod
    def execute(cls, a, b):
        return a - b

class ConcreteStrategyMultiply(Strategy):
    @classmethod
    def execute(cls, a, b):
        return a * b


class Context:
    def __init__(self):
        self._strategy = None

    @property
    def setStrategy(self):
        return self._strategy

    @setStrategy.setter
    def setStrategy(self, strategy):
        self._strategy = strategy 

    def executeStrategy(self, a, b):
        return self._strategy.execute(a,b)


def main():
    Strategy1 = Context()
    Strategy1.setStrategy = ConcreteStrategyAdd()
    print(Strategy1.executeStrategy(1,2))
    Strategy1.setStrategy = ConcreteStrategyMultiply()
    print(Strategy1.executeStrategy(1,2))



main()
