from typing import Protocol

from modeli import Rezervacija


class IzvorRezervacija(Protocol):
    def ucitaj(self) -> list[Rezervacija]: ...


class Izvjestavac(Protocol):
    def sacuvaj(self, tekst: str) -> None: ...
