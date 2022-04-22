from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def writeData(self,data):
        pass

    @abstractmethod
    def readData(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename
        self.document = []

    def writeData(self, data):
        self.document.append(data)

    def readData(self):
        print(self.document)

class DataSourceDecorator(DataSource):
    def __init__(self, datasource):
        self.datasource = datasource

    def writeData(self, data):
        self.datasource.writeData(data)

    def readData(self,):


class EncryptionDecorator(Data):
    ...




