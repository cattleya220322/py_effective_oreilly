
class Resistor:
    def __init__(self, ohms) -> None:
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class ResistorVoltage(Resistor):
    def __init__(self, ohms) -> None:
        super().__init__(ohms)
        self._voltage = 0   # protected

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, voltage) -> None:
        self._voltage = voltage
        self.current = self._voltage/self.ohms


if __name__ == '__main__':
    r1 = Resistor(50e3)
    print(r1.ohms)
    r1.ohms = 10e3
    print(r1.ohms)
    r1.ohms += 5e3
    print(r1.ohms)

    r2 = ResistorVoltage(1e3)
    print(f'before: {r2.current:.2f} amps')
    r2.voltage = 10
    print(f'after: {r2.current:.2f} amps')
