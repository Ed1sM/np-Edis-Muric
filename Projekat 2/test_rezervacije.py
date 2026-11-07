import pytest

from modeli import Rezervacija
from servis import ServisRezervacija


class LazniIzvor:
    def __init__(self, rezervacije: list[Rezervacija]) -> None:
        self.rezervacije = rezervacije

    def ucitaj(self) -> list[Rezervacija]:
        return self.rezervacije


class LazniIzvjestavac:
    def __init__(self) -> None:
        self.tekst: str | None = None

    def sacuvaj(self, tekst: str) -> None:
        self.tekst = tekst


def test_ukupan_iznos() -> None:
    izvor = LazniIzvor([
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 2, 50),
    ])
    izvjestavac = LazniIzvjestavac()

    tekst = ServisRezervacija(
        izvor, izvjestavac
    ).obradi()

    assert "UKUPNO: 340.00 EUR" in tekst


def test_izvjestaj_je_sacuvan() -> None:
    izvjestavac = LazniIzvjestavac()

    tekst = ServisRezervacija(
        LazniIzvor([Rezervacija("Ivana", 1, 120)]),
        izvjestavac,
    ).obradi()

    assert izvjestavac.tekst == tekst
    assert "Ivana: 120.00 EUR" in tekst


def test_prazan_izvor() -> None:
    tekst = ServisRezervacija(
        LazniIzvor([]),
        LazniIzvjestavac(),
    ).obradi()

    assert "UKUPNO: 0.00 EUR" in tekst


def test_neispravan_broj_noci() -> None:
    with pytest.raises(ValueError):
        Rezervacija("Ana", 0, 80)


def test_negativna_cijena() -> None:
    with pytest.raises(ValueError):
        Rezervacija("Ana", 2, -10)
