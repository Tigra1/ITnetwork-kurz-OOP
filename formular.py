from menu import Menu
from evidence import Evidence


class Formular:
    def __init__(self):
        self.evidence = Evidence()  # Inicializace třídy pro práci s uživateli
        print("--------------------")
        print("Evidence pojištěných")
        print("--------------------")
        self.spustit()

    def spustit(self):
        pokracovat = "ano"
        while pokracovat.lower() == "ano":
            Menu()  # Vyvolání menu
            volba = int(input())
            match volba:

                case 1:
                    # Přidání nového pojištěnce
                    while True:
                        jmeno = input("Zadejte jméno pojisteného: ").strip()
                        if not jmeno or not jmeno.isalpha():
                            print("Jméno nesmí být prázdné a musí obsahovat pouze písmena.")
                        else:
                            break

                        # Zadání příjmení s ověřením
                    while True:
                        prijmeni = input("Zadejte přijméní pojisteného: ").strip()
                        if not prijmeni or not prijmeni.isalpha():
                            print("Přijmení nesmí být prázdné a musí obsahovat pouze písmena.")
                        else:
                            break

                        # Zadání věku s ověřením
                    while True:
                        vek = input("Zadejte vek pojisteného: ").strip()
                        if not vek.isdigit():
                            print("Věk musí být číslo.")
                            continue
                        vek_int = int(vek)
                        if not (0 < vek_int <= 130):
                            print("Věk musí být v rozmezí od 1 do 130.")
                        else:
                            break

                        # Zadání telefonu
                    telefon = input("Zadejte telefon pojisteného: ").strip()
                    self.evidence.add_pojisteny(jmeno, prijmeni, vek, telefon)
                    print(f"Pojištěný {jmeno} {prijmeni} úspěšně přidán.")

                case 2:
                    # Výstup všech pojištěnců
                    if self.evidence.seznam:
                        print("\nSeznam všech pojištěných:")
                        for pojisteny in self.evidence.seznam:
                            print(pojisteny)
                    else:
                        print("Žádní pojištěnci nejsou v evidenci.")

                case 3:
                    # Vyhledávání pojištěnce

                    hledane_jmeno = input("Zadejte jméno nebo přijmení pro vyhledání: ").strip()

                    nalezeni = False
                    for pojisteny in self.evidence.seznam:
                        if (pojisteny.jmeno.lower() == hledane_jmeno.lower() or
                                pojisteny.prijmeni.lower() == hledane_jmeno.lower()):
                            print(pojisteny)
                            nalezeni = True
                    if not nalezeni:
                        print("Pojištěný s tímto jménem nebo přijmením nebyl nalezen.")

                case 4:
                    # Ukončení aplikace
                    print("Děkuji za použití aplikace.")
                    break

            if volba != 4:
                pokracovat = input("Přejete si zadat další akci? [ano/ne]: ")
            else:
                break
