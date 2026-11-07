from experiment import IrisEksperiment
from observers import PracenjeTreninga, ispis_dogadjaja


def main() -> None:
    pracenje = PracenjeTreninga()
    pracenje.pretplati(ispis_dogadjaja)

    modeli = ["linearni", "stablo", "knn"]
    metrike = ["accuracy", "f1"]

    print("=== MINI OKVIR ZA ML EKSPERIMENTE ===")

    for naziv_modela in modeli:
        for naziv_metrike in metrike:
            print(f"\nModel: {naziv_modela} | Metrika: {naziv_metrike}")

            eksperiment = IrisEksperiment(
                naziv_modela,
                naziv_metrike,
                pracenje,
            )

            rezultat = eksperiment.pokreni()

            print(f"REZULTAT: {rezultat.vrijednost:.4f}")


if __name__ == "__main__":
    main()
