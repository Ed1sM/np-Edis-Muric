
def prosjecna_cijena(cijene):
    if not cijene:
        raise ValueError("Lista cijena ne smije biti prazna.")

    if any(cijena < 0 for cijena in cijene):
        raise ValueError("Cijene ne mogu biti negativne.")

    return sum(cijene) / len(cijene)


if __name__ == "__main__":
    cijene = [10, 20, 30, 40]
    print("Prosjecna cijena:", prosjecna_cijena(cijene))
