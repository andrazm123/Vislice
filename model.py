import random
import json

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZAČETEK = "s"
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

with open("Repozitorij/vislice/besede.txt", "r", encoding="utf-8") as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)


def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


class Vislice:

    def __init__(self, datoteka_s_stanjem):
        # V slovarju igre ima vsaka igra svoj celoštevilski id.
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # Preverimo za n+1 stevil izmed n iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
    
    def nova_igra(self):
        # Naredi novo igro z naključnim geslom in shrani v slovar z novim ID, shrani (začetek, igra)
        self.nalozi_igre_iz_datoteke()
        igra = nova_igra()
        nov_id = self.prost_id_igre()
        self.igre[nov_id] = (igra, ZAČETEK)
        self.zapisi_igre_v_datoteko()
        return nov_id

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        (igra, _) = self.igre[id_igre]
        nov_poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, nov_poskus)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as datoteka:
            zakodirane_igre = json.load(datoteka) #Dobimo slovar z (geslom, crke)
            igre = {}
            for id_igre in zakodirane_igre:
                igra = zakodirane_igre[id_igre]
                igre[int(id_igre)] = (Igra(igra["geslo"], igra["crke"]), igra["poskus"])
            self.igre = igre
        

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, "w") as datoteka:
            zakodirane_igre = {}
            for id_igre in self.igre:
                (igra, poskus) = self.igre[id_igre]
                zakodirane_igre[id_igre] = {"geslo": igra.geslo, "crke": igra.crke, "poskus": poskus}
            json.dump(zakodirane_igre, datoteka)