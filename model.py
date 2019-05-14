import random

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZMAGA = "w"
PORAZ = "x"

# Definiramo logicni model igre

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() # string
        self.crke = crke # list

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for i in self.geslo:
            if i not in self.crke:
                return False
        return True
    
    def poraz(self):
        return len(self.napacne_crke()) > STEVILO_DOVOLJENIH_NAPAK
        
    def pravilni_del_gesla(self):
        niz = ""
        for i in self.geslo:
            if i in self.crke:
                niz += " " + i
            else:
                niz += " _"
        return niz.strip()

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA



# Izluščimo vse slovenske besede.
bazen_besed = []

with open("\\Tomo\\Repozitorij\\vislice\\besede.txt", "r", encoding="utf-8") as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

print(bazen_besed)

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


