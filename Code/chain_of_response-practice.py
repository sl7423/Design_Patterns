import random

class Component:
    def __init__(self):
        self.container = None

    def add(self, component):
        if self.container is None:
            self.container = component
            return
        else:
            last = self.container
            while last.next:
                last = last.next    
            last.next = component

    def handle(self, prob):
        temp = self.container
        while temp is not None:
            randomValue = float(random.random())
            if randomValue >= prob:
                temp.showHelp()
                return
            else:
                temp = temp.next
        print("No one can help!")


class Container(Component):
    def __init__(self, name):
        self.name = name
        self.next = None


class Panel(Container):
    def showHelp(self):
        print("Panel Help!")

class Dialog(Container):
    def showHelp(self):
        print("Dialog Help")

class Button(Container):
    def showHelp(self):
        print("Button") 
    

dialog = Dialog("Talk to someon")
panel = Panel("This panel does not...")
button = Button("OK Button Help")
Components = Component()
Components.add(button)
Components.add(panel)
Components.add(dialog)
Components.handle(0.2)

    





