from pathlib import Path


class TekstualniIzvjestavac:
    def __init__(self, putanja: Path) -> None:
        self.putanja = putanja

    def sacuvaj(self, tekst: str) -> None:
        self.putanja.write_text(tekst, encoding="utf-8")
