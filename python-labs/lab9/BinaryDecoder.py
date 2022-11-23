from Digitals import Digitals


class BinaryDecoder(Digitals):
    def __init__(self, name, voltage, current, battery, decodingRate: float):
        super(BinaryDecoder, self).__init__(name, voltage, current, battery)
        self.decodingRate = decodingRate

    def __str__(self):
        return super(BinaryDecoder, self).__str__()\
            + f"Decoding rate -> {self.decodingRate}\n"
