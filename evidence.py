# Třída pro přídaní dat do seznamu
from pojisteny import Pojisteny


class Evidence:
    def __init__(self):
        self.seznam = []  # Seznam všech pojištěnců

    def add_pojisteny(self, jmeno, prijmeni, vek, telefon):

        # Pokud jsou všechny údaje zadány správně, vytvořti objekt pojištěnce a přida jej do seznamu
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam.append(pojisteny)
