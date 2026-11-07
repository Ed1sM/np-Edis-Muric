from dataclasses import dataclass


@dataclass(frozen=True)
class Rezervacija:
    gost: str
    noci: int
    cijena_noci: float

    def __post_init__(self) -> None:
        if not self.gost.strip():
            raise ValueError("Ime gosta ne smije biti prazno.")

        if self.noci <= 0:
            raise ValueError("Broj nocenja mora biti pozitivan.")

        if self.cijena_noci < 0:
            raise ValueError("Cijena nocenja ne smije biti negativna.")

    @property
    def iznos(self) -> float:
        return self.noci * self.cijena_noci
