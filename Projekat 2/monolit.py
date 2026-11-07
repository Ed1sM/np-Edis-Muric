import csv
from pathlib import Path


class UpravljanjeRezervacijama:
    def __init__(self, putanja: Path) -> None:
        self.putanja = putanja

    def obradi(self) -> str:
        with self.putanja.open(
            newline="", encoding="utf-8"
        ) as datoteka:
            redovi = list(csv.DictReader(datoteka))

        iznosi = [
            int(r["noci"]) * float(r["cijena_noci"])
            for r in redovi
        ]

        tekst = "\n".join(
            ["IZVJESTAJ O REZERVACIJAMA"]
            + [
                f"{r['gost']}: {iznos:.2f} EUR"
                for r, iznos in zip(redovi, iznosi)
            ]
            + [f"UKUPNO: {sum(iznosi):.2f} EUR"]
        )

        (self.putanja.parent / "izvjestaj_monolit.txt").write_text(
            tekst, encoding="utf-8"
        )

        print(tekst)
        return tekst


if __name__ == "__main__":
    UpravljanjeRezervacijama(
        Path(__file__).resolve().parent / "rezervacije.csv"
    ).obradi()
