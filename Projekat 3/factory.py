from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def kreiraj_model(naziv: str):

    modeli = {
        "linearni": lambda: make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1000, random_state=42),
        ),
        "stablo": lambda: DecisionTreeClassifier(
            max_depth=4,
            random_state=42,
        ),
        "knn": lambda: make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=5),
        ),
    }

    if naziv not in modeli:
        raise ValueError(f"Nepoznat model: {naziv}")

    return modeli[naziv]()
