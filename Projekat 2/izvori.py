import csv
from pathlib import Path

from modeli import Rezervacija


class CsvIzvorRezervacija:
    def __init__(self, putanja: Path) -> None:
        self.putanja = putanja

    def ucitaj(self) -> list[Rezervacija]:
        with self.putanja.open(
            newline="", encoding="utf-8"
        ) as datoteka:
            redovi = csv.DictReader(datoteka)

            return [
                Rezervacija(
                    gost=red["gost"],
                    noci=int(red["noci"]),
                    cijena_noci=float(red["cijena_noci"]),
                )
                for red in redovi
            ]
