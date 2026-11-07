from collections.abc import Callable

from sklearn.metrics import accuracy_score, f1_score

Metrika = Callable[[object, object], float]


def tacnost(y_true, y_pred) -> float:

    return float(accuracy_score(y_true, y_pred))


def f1_metrika(y_true, y_pred) -> float:

    return float(f1_score(y_true, y_pred, average="macro", zero_division=0))


METRIKE: dict[str, Metrika] = {
    "accuracy": tacnost,
    "f1": f1_metrika,
}


def izaberi_metriku(naziv: str) -> Metrika:
    if naziv not in METRIKE:
        raise ValueError(f"Nepoznata metrika: {naziv}")

    return METRIKE[naziv]
