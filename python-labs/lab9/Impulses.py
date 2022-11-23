from Electronics import Electronics


class Impulses(Electronics):
    def __init__(self, name, voltage, current, amountOfImpulses: float):
        super(Impulses, self).__init__(name, voltage, current)
        self.amountOfImpulses = amountOfImpulses

    def __str__(self):
        return super(Impulses, self).__str__() \
               + f"Battery -> :{self.amountOfImpulses}\n"
