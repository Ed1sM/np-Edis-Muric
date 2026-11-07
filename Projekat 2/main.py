from pathlib import Path

from izvjestaji import TekstualniIzvjestavac
from izvori import CsvIzvorRezervacija
from servis import ServisRezervacija


def main() -> None:
    folder = Path(__file__).resolve().parent

    servis = ServisRezervacija(
        CsvIzvorRezervacija(folder / "rezervacije.csv"),
        TekstualniIzvjestavac(folder / "izvjestaj.txt"),
    )

    print(servis.obradi())


if __name__ == "__main__":
    main()
