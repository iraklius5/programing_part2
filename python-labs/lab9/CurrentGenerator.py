from Impulses import Impulses


class CurrentGenerator(Impulses):
    def __init__(self, name, voltage, current, amountOfImpulses, generatedCurrent):
        super(CurrentGenerator, self).__init__(name, voltage, current, amountOfImpulses)
        self.generatedCurrent = generatedCurrent

    def __str__(self):
        return super(CurrentGenerator, self).__str__()\
            + f"Generated current -> {self.generatedCurrent}]\n"
