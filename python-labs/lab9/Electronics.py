class Electronics(object):
    def __init__(self, name: str, voltage: float, current: float) -> None:
        self.name = name
        self.voltage = voltage
        self.current = current

    def __str__(self):
        return f"Name -> {self.name}\n"\
               f"Volatage -> {self.voltage}\n" \
               f"Current -> {self.current}\n"
