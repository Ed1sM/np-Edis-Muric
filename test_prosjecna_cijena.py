
import pytest

from prosjecna_cijena import prosjecna_cijena


def test_normalne_cijene():
    assert prosjecna_cijena([10, 20, 30]) == 20


def test_jedna_cijena():
    assert prosjecna_cijena([15]) == 15


def test_decimalne_cijene():
    assert prosjecna_cijena([10.5, 20.5]) == 15.5


def test_prazna_lista():
    with pytest.raises(ValueError):
        prosjecna_cijena([])


def test_negativna_cijena():
    with pytest.raises(ValueError):
        prosjecna_cijena([10, -5, 20])
