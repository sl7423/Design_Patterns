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
        return self.datasource.writeData(data)

    def readData(self):
        return self.datasource.readData()


class EncryptionDecorator(DataSourceDecorator):
    def writeData(self, data):
        print("Encrypt data")
        return self.datasource.writeData(data)

    def readData(self):
        print("Unencrypt data")
        return self.datasource.readData()


class CompressionDirector(DataSourceDecorator):
    def writeData(self, data):
        print("Compressed passed data")
        return self.datasource.writeData(data)

    def readData(self):
        print("Uncompress data")
        return self.datasource.readData()


source = FileDataSource("file.txt")
source.writeData("Salary Records")
source = CompressionDirector(source)
source.writeData("Another Salary record")
source = EncryptionDecorator(source)
source.writeData("More secured records")
source.readData()


