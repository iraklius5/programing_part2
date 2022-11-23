from Digitals import Digitals


class BinnaryAdder(Digitals):
    def __init__(self, name, voltage, current, battery, outputValue):
        super(BinnaryAdder, self).__init__(name, voltage, current, battery)
        self.outputValue = outputValue

    def __str__(self):
        return super(BinnaryAdder, self).__str__()\
            + f"Output Value -> {self.outputValue}\n"
