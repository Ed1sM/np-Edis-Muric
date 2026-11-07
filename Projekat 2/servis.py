from protokoli import IzvorRezervacija, Izvjestavac


class ServisRezervacija:
    def __init__(
        self,
        izvor: IzvorRezervacija,
        izvjestavac: Izvjestavac,
    ) -> None:
        self.izvor = izvor
        self.izvjestavac = izvjestavac

    def obradi(self) -> str:
        rezervacije = self.izvor.ucitaj()

        redovi = ["IZVJESTAJ O REZERVACIJAMA"]

        for rezervacija in rezervacije:
            redovi.append(
                f"{rezervacija.gost}: "
                f"{rezervacija.iznos:.2f} EUR"
            )

        ukupno = sum(
            rezervacija.iznos
            for rezervacija in rezervacije
        )

        redovi.append(f"UKUPNO: {ukupno:.2f} EUR")

        tekst = "\n".join(redovi)
        self.izvjestavac.sacuvaj(tekst)

        return tekst
