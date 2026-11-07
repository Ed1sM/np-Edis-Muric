import time
from functools import wraps


def mjeri_vrijeme(funkcija):
    @wraps(funkcija)
    def omotac(*args, **kwargs):
        pocetak = time.perf_counter()

        try:
            return funkcija(*args, **kwargs)
        finally:
            trajanje = time.perf_counter() - pocetak
            print(f"[VRIJEME] {trajanje:.4f} sekundi")

    return omotac
