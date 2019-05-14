import model

def izpis_igre(igra):
    tekst = (
    '=======================================\n\n'
    '{trenutno_stanje}'
    'Poskusili ste ze: {poskusi}\n\n'
    '========================================'
    ).format(trenutno_stanje = igra.pravilni_del_gesla(), poskusi = igra.napacne_crke())
    return tekst

def izpis_zmage(igra):
    return "Zmagali ste, geslo je {}.".format(igra.geslo)

def izpis_poraza(igra):
    return "Izgubili ste! Pravilno geslo je {}.".format(igra.geslo)

def zahtevaj_vnos():
    vnos = input("poskusi uganiti crko: ")
    return vnos

def preveri_vnos(vnos):
    if not len(vnos) == 1:
        print("Neveljaven vnos, vnesite le eno crko")
        return False
    else:
        return True


# Izvajanje vmesnika
def zazeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        # ugiba
        poskus = zahtevaj_vnos()
        if not preveri_vnos(poskus):
            continue
        igra.ugibaj(poskus)
        # prverimo, ce je igre konec
        if igra.poraz():
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return 


