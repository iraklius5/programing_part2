from Electronics import Electronics


class Digitals(Electronics):
    def __init__(self, name, voltage, current, battery: int):
        super(Digitals, self).__init__(name, voltage, current)
        self.battery = battery

    def __str__(self):
        return super(Digitals, self).__str__() \
               + f"Battery -> :{self.battery}\n"
