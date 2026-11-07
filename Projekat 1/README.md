Projekat: Prosjecna cijena

Ovaj projekat implementira Python funkciju prosjecna_cijena koja izračunava prosječnu vrijednost cijena iz liste.

Korišćene tehnologije:

Python 3.12+
Visual Studio Code
pytest
ruff
GitHub

Pokretanje programa:

python prosjecna_cijena.py

Pokretanje testova:

python -m pytest -v

Provjera kvaliteta koda:

python -m ruff check .

Upotreba AI asistenta:

Za pomoć pri izradi projekta korišćen je ChatGPT.

Upotrijebljeni upiti:

"Napiši Python funkciju prosjecna_cijena koja računa prosjek liste cijena."
"Dodaj provjeru za praznu listu i negativne cijene."
"Napiši pytest testove za funkciju prosjecna_cijena."
"Objasni kako da koristim ruff i pytest u Visual Studio Code-u."

Uočeni nedostaci generisanog koda:

Osnovna verzija funkcije nije sadržala provjeru prazne liste.
Bilo je potrebno dodati provjeru negativnih cijena.
Funkcija ne provjerava da li su svi elementi liste numeričke vrijednosti.
Računanje pomoću float vrijednosti može dovesti do malih grešaka zaokruživanja.

