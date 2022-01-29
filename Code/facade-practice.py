class VideoFile:
    def __init__(self, filename):
        self.filename = filename

class OggCompressioCode:
    def __init__(self):
        self.compression_code = 'OggCompressionCode'
    
    def __repr__(self):
        return self.compression_code

class MPEG4CompressCodec:
    def __init__(self):
        self.compression_code = 'MPEG4CompressionCode'
    
    def __repr__(self):
        return self.compression_code


class CodecFactory:
    @staticmethod
    def extract(file):
        return str(file)


class BitrateReader:
    @staticmethod
    def read(filename, sourcecode):
        return 'CompleteRead'

    @staticmethod
    def convert(buffer, destinationCodec):
        return 'CompleteConvert'

class Audiomixer:
    @staticmethod
    def fix(result):
        return result

class File:
    def __init__(self, result):
        self.result = result
    
    def save(self):
        print("File has been saved!")

class VideoConverter:
    @staticmethod
    def convert(filename, format):
        file = VideoFile(filename)
        sourceCodec = CodecFactory().extract(file)
        if format == 'mp4':
            destinationCodec = MPEG4CompressCodec()
        else:
            destinationCodec = OggCompressioCode()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = Audiomixer().fix(result)
        print("Video has been converted")
        return File(result)

def main():
    converter = VideoConverter()
    mp4 = converter.convert("youtube.com", 'mp4')
    mp4.save()

main()


