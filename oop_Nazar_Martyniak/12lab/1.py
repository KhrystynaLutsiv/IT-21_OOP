class VideoFile:
    def __init__(self, filename):
        self.filename = filename


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:
    @staticmethod
    def extract(file):
        return OggCompressionCodec()


class BitrateReader:
    @staticmethod
    def read(filename, codec):
        return "buffer"

    @staticmethod
    def convert(buffer, codec):
        return "converted_data"


class AudioMixer:
    @staticmethod
    def fix(data):
        return "fixed_data"


class VideoConverter:
    def convert(self, filename, format):
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)
        destination_codec = MPEG4CompressionCodec() if format == "mp4" else OggCompressionCodec()
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer.fix(result)
        return File(result)


class File:
    def __init__(self, data):
        self.data = data

    def save(self):
        print("File saved!")


class Application:
    @staticmethod
    def main():
        converter = VideoConverter()
        mp4 = converter.convert("funny-cats-video.ogg", "mp4")
        mp4.save()


if __name__ == "__main__":
    Application.main()
