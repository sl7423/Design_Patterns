from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

#Button portion of the codde
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    def paint(self):
        return 'Paint a Windows Button in Windows Style'

class MacButton(Button):
    def paint(self):
        return 'Paint a Mac Button in Mac Style'

#Checkbox
class Checkbox(ABC):
    @abstractmethod
    def draw(self):
        pass

class WinCheckbox(Checkbox):
    def draw(self):
        return 'Paint a Windows Checkbox in Windows Style'

class MacCheckbox(Checkbox):
    def draw(self):
        return 'Paint a Mac Checkbox in Mac Style'

def Application(factory: GUIFactory) -> None:
    product_a = factory.create_checkbox()
    product_b = factory.create_button()

    print(f"{product_a.draw()}")
    print(f"{product_b.paint()}")

if __name__ == '__main__':
    
    config = input("Please enter your operating system? (Windows & Mac)")

    if config == "Windows":
        Application(WinFactory())

    elif config == "Mac":
        Application(MacFactory())

    else:
        RuntimeError("Not a type of operating system")