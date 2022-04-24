class Memento:
    def __init__(self, text, curX, curY, selection_width):
        self.text = text
        self.curX = curX
        self.curY = curY
        self.selection_width = selection_width

class Editor:
    def __init__(self):
        self._text = None
        self._curX = None
        self._curY = None
        self._selectionWidth = None

    def __str__(self):
        return f"Text: {self._text}, Coordinates: ({self._curX}, {self._curY}), Selection Width: {self._selectionWidth}"

    @property
    def setText(self):
        return self._text

    @setText.setter
    def setText(self, text):
        self._text = text

    @property
    def curl(self):
        return (self._curX, self._curY)

    @curl.setter
    def curl(self, lst):
        if len(lst) == 2:
            self._curX, self._curY = lst[0], lst[1]
        else:
            raise Exception("List has to length of 2")

    @property
    def selectionWidth(self):
        return self._selectionWidth

    @selectionWidth.setter
    def selectionWidth(self, selectionWidth):
        self._selectionWidth = selectionWidth

    @property
    def memento(self):
        return Memento(self._text, self._curX, self._curY, self._selectionWidth)

    @memento.setter
    def memento(self, memento):
        self._text = memento.text
        self._curX = memento.curX
        self._curY = memento.curY
        self._selectionWidth = memento.selection_width

class CareTaker:
    def __init__(self, Editor):
        self._Editor = Editor
        self._mementos = []

    def save(self):
        print("CareTaker: Saving a copy of this state")
        memento = self._Editor.memento
        self._mementos.append(memento)

    def restore(self, index):
        print("CareTaker: Restoring Originators state from Memento")
        memento = self._mementos[index]
        self._Editor.memento = memento


    

EDITOR = Editor()
CARETAKER = CareTaker(EDITOR)

EDITOR.setText = "Hello"
EDITOR.curl = (5, 10)
EDITOR.selectionWidth = 10.5
CARETAKER.save()

EDITOR.setText = "World"
EDITOR.curl = (6, 11)
EDITOR.selectionWidth = 11.5
CARETAKER.save()

CARETAKER.restore(1)
print(EDITOR)