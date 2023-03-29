
class ResistorOld:
    def __init__(self, ohms) -> None:
        self._ohms = ohms   # protected

    def get_ohms(self) -> float:
        return self._ohms

    def set_ohms(self, ohms) -> None:
        self._ohms = ohms


if __name__ == '__main__':
    r0 = ResistorOld(50e3)
    print('before: ', r0.get_ohms())
    r0.set_ohms(10e3)
    print('after: ', r0.get_ohms())
