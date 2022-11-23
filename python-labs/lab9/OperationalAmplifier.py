from Analogs import Analogs


class OperationalAmplifier(Analogs):
    def __init__(self, name, voltage, current, connection, amplifingCoeficient):
        super(OperationalAmplifier, self).__init__(name, voltage, current, connection)
        self.amplifingCoeficient = amplifingCoeficient

    def __str__(self):
        return super(OperationalAmplifier, self).__str__() \
               + f"Amplifying Coeficient -> {self.amplifingCoeficient}\n"
