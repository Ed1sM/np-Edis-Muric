import pytest

from experiment import IrisEksperiment, Rezultat
from factory import kreiraj_model
from metrics import izaberi_metriku
from observers import PracenjeTreninga


@pytest.mark.parametrize(
    "naziv",
    ["linearni", "stablo", "knn"],
)
def test_factory_kreira_modele(naziv):
    model = kreiraj_model(naziv)
    assert hasattr(model, "fit")
    assert hasattr(model, "predict")


def test_factory_nepoznat_model():
    with pytest.raises(ValueError):
        kreiraj_model("nepostojeci")


def test_accuracy_metrika():
    metrika = izaberi_metriku("accuracy")
    rezultat = metrika([0, 1, 2], [0, 1, 1])
    assert rezultat == pytest.approx(2 / 3)


def test_f1_metrika():
    metrika = izaberi_metriku("f1")
    rezultat = metrika([0, 1, 2], [0, 1, 2])
    assert rezultat == 1.0


def test_nepoznata_metrika():
    with pytest.raises(ValueError):
        izaberi_metriku("nepostojeca")


def test_observer_prima_poruku():
    poruke = []
    pracenje = PracenjeTreninga()

    pracenje.pretplati(poruke.append)
    pracenje.obavijesti("Treniranje zavrseno")

    assert poruke == ["Treniranje zavrseno"]


def test_iris_eksperiment():
    poruke = []
    pracenje = PracenjeTreninga()
    pracenje.pretplati(poruke.append)

    eksperiment = IrisEksperiment(
        "linearni",
        "accuracy",
        pracenje,
    )

    rezultat = eksperiment.pokreni()

    assert isinstance(rezultat, Rezultat)
    assert rezultat.model == "linearni"
    assert 0.0 <= rezultat.vrijednost <= 1.0
    assert "Eksperiment je zavrsen." in poruke
