from OperationalAmplifier import OperationalAmplifier
from CurrentGenerator import CurrentGenerator
from VotageGenerator import VoltageGenerator
from BinaryDecoder import BinaryDecoder
from BinnaryAdder import BinnaryAdder


def main():
    operationalAmplifier1 = OperationalAmplifier("Biggie ", 50, 10, True, 45)
    currentGenerator1 = CurrentGenerator("Voltiz", 13, 15, 40, 50)
    voltageGenerator1 = VoltageGenerator("Currz", 15, 20, 30, 40)
    binaryDecoder1 = BinaryDecoder("Enigma", 12, 14, 12, 1.2)
    binaryAdder1 = BinnaryAdder("Expoz", 5, 3, 15, 100)

    print(operationalAmplifier1.__str__())
    print(currentGenerator1.__str__())
    print(voltageGenerator1.__str__())
    print(binaryDecoder1.__str__())
    print(binaryAdder1.__str__())


if __name__ == "__main__":
    main()
