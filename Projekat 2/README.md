Refaktoring obrade rezervacija

## Opis projekta

Projekat prikazuje refaktoring monolitnog programa za obradu rezervacija primjenom SOLID principa S (Single Responsibility) i D (Dependency Inversion).

## Funkcionalnosti

- Učitavanje rezervacija iz CSV datoteke.
- Validacija podataka o rezervacijama.
- Izračunavanje iznosa pojedinačnih rezervacija.
- Izračunavanje ukupnog iznosa.
- Generisanje tekstualnog izvještaja.
- Automatsko testiranje zamjenskim izvorom podataka.

## Primjena SOLID principa

### Single Responsibility Principle (S)

Početna klasa je obavljala učitavanje, obračun, izvještavanje i ispis rezultata.

Nakon refaktoringa odgovornosti su razdvojene na model rezervacije, CSV izvor, izvještavač, servis i ulaznu tačku aplikacije.

### Dependency Inversion Principle (D)

Klasa `ServisRezervacija` ne zavisi direktno od CSV datoteke niti od konkretnog načina izvještavanja.

Koristi dva Protocol interfejsa: `IzvorRezervacija` i `Izvjestavac`. Konkretne implementacije se prosljeđuju kroz konstruktor.

## Pokretanje


```bash
python monolit.py
python main.py
```

## Testiranje

```bash
python -m pytest -v test_rezervacije.py
python -m ruff check .
```

## Upotreba AI asistenta

Za pripremu projekta korišćen je ChatGPT.

Upotrijebljeni upiti:

1. "Napravi primjer monolitnog Python programa za obradu rezervacija."
2. "Refaktoriši program primjenom Single Responsibility i Dependency Inversion principa."
3. "Uvedi Protocol interfejse za izvor rezervacija i izvještavanje."
4. "Napiši najmanje tri pytest testa sa zamjenskim izvorom podataka."
5. "Objasni prednosti i nedostatke refaktorisanog rješenja."

## Ispravke i unapređenja generisanog koda

- Uvedena validacija broja noćenja i cijene.
- Čitanje datoteke obavlja se pomoću `with` izraza.
- Direktne zavisnosti zamijenjene su Protocol ugovorima.
- Poslovna logika izdvojena je iz ulazne tačke programa.
- Testovi koriste zamjenske objekte, bez pristupa stvarnim datotekama.
- Dodate su anotacije tipova i jasnije definisane odgovornosti.

## Ograničenja

- Novčane vrijednosti koriste `float`; za produkcijski finansijski sistem preporučuje se `Decimal`.
- CSV izvor pretpostavlja ispravne nazive kolona.
- Nema baze podataka niti slanja stvarnih e-mail poruka.

## Zaključak

Refaktoring je omogućio bolje razdvajanje odgovornosti, jednostavnije testiranje i lakšu zamjenu izvora podataka i načina izvještavanja. Osnovna funkcionalnost obračuna rezervacija je očuvana.
