## Opis projekta

Ovaj projekat predstavlja jednostavan okvir za izvođenje eksperimenata mašinskog učenja korišćenjem biblioteke scikit-learn.

Cilj projekta je demonstracija pet projektnih šablona: Factory, Strategy, Observer, Template Method i Decorator.

## Funkcionalnosti

- Kreiranje različitih ML modela.
- Treniranje modela na skupu Iris.
- Podjela podataka na trening i test skup.
- Evaluacija pomoću Accuracy i F1 metrika.
- Praćenje događaja tokom eksperimenta.
- Mjerenje vremena izvršavanja.
- Automatsko testiranje pomoću pytest-a.

## Korišćeni modeli

1. Logistička regresija – linearni klasifikacioni model.
2. Stablo odlučivanja – klasifikacija kroz skup pravila.
3. kNN – klasifikacija na osnovu najbližih susjeda.

## Projektni šabloni

Factory: Funkcija `kreiraj_model()` omogućava kreiranje modela na osnovu naziva.

Strategy: Funkcija `izaberi_metriku()` omogućava izbor metrike evaluacije.

Observer: Klasa `PracenjeTreninga` obavještava registrovane posmatrače o događajima.

Template Method: Osnovna klasa `Eksperiment` definiše zajednički redosljed učitavanja, pripreme, treniranja i evaluacije.

Decorator: Funkcija `mjeri_vrijeme()` mjeri trajanje izvršavanja eksperimenta.

## Mermaid dijagram


## Pokretanje aplikacije

```bash
python main.py
```

## Pokretanje testova

```bash
python -m pytest -v test_experiment.py
```

## Provjera kvaliteta

```bash
python -m ruff check .
python -m ruff format --check .
```

## Upotreba AI asistenta

U izradi projekta korišćen je ChatGPT za generisanje početne implementacije, objašnjenje projektnih šablona i pripremu testova.

### Upotrijebljeni upiti

1. "Implementiraj Factory Pattern za kreiranje tri ML modela u Pythonu."
2. "Dodaj Strategy Pattern za izbor Accuracy i F1 metrika."
3. "Implementiraj Observer Pattern za praćenje događaja tokom treniranja."
4. "Napravi Template Method za tok eksperimenta i Decorator za mjerenje vremena."
5. "Napiši najmanje pet pytest testova za ML okvir."
6. "Generiši Mermaid dijagram klasa i objasni odnose između komponenti."

## Kritička analiza i unapređenja AI koda

- Skaliranje je uključeno u Pipeline za modele osjetljive na razmjeru karakteristika.
- Za ponovljivost eksperimenta koristi se fiksni `random_state`.
- Podaci su podijeljeni na trening i test skup prije treniranja.
- Nepoznati nazivi modela i metrika izazivaju jasne izuzetke.
- Za čuvanje rezultata upotrijebljena je dataclass klasa.
- Dodati su automatski testovi za provjeru najvažnijih funkcionalnosti.

### Ograničenja

- Koristi se samo Iris skup podataka.
- Nema automatskog podešavanja hiperparametara.
- Ne koristi se unakrsna validacija.
- Eksperimenti se izvršavaju sekvencijalno.
- Fajlovi ne čuvaju trenirane modele na disk.

## Zaključak

Projekat demonstrira kako projektni šabloni olakšavaju organizaciju koda, razdvajanje odgovornosti, testiranje i proširivanje sistema za mašinsko učenje.

Dodavanje novih modela, metrika i posmatrača moguće je bez značajnih izmjena osnovnog toka eksperimenta.
