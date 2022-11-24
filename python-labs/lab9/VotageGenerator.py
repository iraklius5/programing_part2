from Impulses import Impulses


class VoltageGenerator(Impulses):
    def __init__(self, name, voltage, current, amountOfImpulses, voltageGenerated):
        super(VoltageGenerator, self).__init__(name, voltage, current, amountOfImpulses)
        self.voltageGenerated = voltageGenerated

    def __str__(self):
        return super(VoltageGenerator, self).__str__()\
            + f"Voltage generated -> {self.voltageGenerated}\n"