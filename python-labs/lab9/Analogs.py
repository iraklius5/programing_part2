from Electronics import Electronics


class Analogs(Electronics):
    def __init__(self, name, voltage, current, connection: bool):
        super(Analogs, self).__init__(name, voltage, current)
        self.connection = connection

    def __str__(self):
        return super(Analogs, self).__str__() \
               + f"Battery -> :{self.connection}\n"
