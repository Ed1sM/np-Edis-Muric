from abc import ABC, abstractmethod
from dataclasses import dataclass

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from factory import kreiraj_model
from metrics import izaberi_metriku
from observers import PracenjeTreninga
from timing import mjeri_vrijeme


@dataclass(frozen=True)
class Rezultat:
    model: str
    metrika: str
    vrijednost: float


class Eksperiment(ABC):
    def __init__(self, pracenje: PracenjeTreninga) -> None:
        self.pracenje = pracenje

    @mjeri_vrijeme
    def pokreni(self) -> Rezultat:
        self.pracenje.obavijesti("Eksperiment je zapocet.")

        podaci = self.ucitaj()
        pripremljeni = self.pripremi(podaci)
        model = self.treniraj(pripremljeni)
        rezultat = self.evaluiraj(model, pripremljeni)

        self.pracenje.obavijesti("Eksperiment je zavrsen.")
        return rezultat

    @abstractmethod
    def ucitaj(self):
        pass

    @abstractmethod
    def pripremi(self, podaci):
        pass

    @abstractmethod
    def treniraj(self, podaci):
        pass

    @abstractmethod
    def evaluiraj(self, model, podaci) -> Rezultat:
        pass


class IrisEksperiment(Eksperiment):
    def __init__(
        self,
        naziv_modela: str,
        naziv_metrike: str,
        pracenje: PracenjeTreninga,
    ) -> None:
        super().__init__(pracenje)
        self.naziv_modela = naziv_modela
        self.naziv_metrike = naziv_metrike

    def ucitaj(self):
        self.pracenje.obavijesti("Ucitavanje Iris podataka.")
        return load_iris(return_X_y=True)

    def pripremi(self, podaci):
        self.pracenje.obavijesti("Podjela podataka.")
        x, y = podaci

        return train_test_split(
            x,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y,
        )

    def treniraj(self, podaci):
        self.pracenje.obavijesti(f"Treniranje modela: {self.naziv_modela}")

        x_train, _, y_train, _ = podaci
        model = kreiraj_model(self.naziv_modela)
        model.fit(x_train, y_train)

        self.pracenje.obavijesti("Treniranje zavrseno.")
        return model

    def evaluiraj(self, model, podaci) -> Rezultat:
        self.pracenje.obavijesti("Evaluacija modela.")

        _, x_test, _, y_test = podaci
        predvidjanja = model.predict(x_test)

        metrika = izaberi_metriku(self.naziv_metrike)
        vrijednost = metrika(y_test, predvidjanja)

        return Rezultat(
            model=self.naziv_modela,
            metrika=self.naziv_metrike,
            vrijednost=vrijednost,
        )
