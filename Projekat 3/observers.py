from collections.abc import Callable

Posmatrac = Callable[[str], None]


class PracenjeTreninga:
    def __init__(self) -> None:
        self.posmatraci: list[Posmatrac] = []

    def pretplati(self, posmatrac: Posmatrac) -> None:
        if posmatrac not in self.posmatraci:
            self.posmatraci.append(posmatrac)

    def obavijesti(self, poruka: str) -> None:
        for posmatrac in self.posmatraci:
            posmatrac(poruka)


def ispis_dogadjaja(poruka: str) -> None:
    print(f"[OBSERVER] {poruka}")
