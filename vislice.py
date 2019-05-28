import bottle, model
SKRIVNI_KLJUC = "bravo, uganil si kluc"


vislice = model.Vislice("Repozitorij/vislice/stanje.json")

# id_testne_igre = vislice.nova_igra()
# (testna_igra, poskus) = vislice.igre[id_testne_igre]
# Dodajmo teste:
# vislice.ugibaj(id_testne_igre, "A")
# vislice.ugibaj(id_testne_igre, "B")
# vislice.ugibaj(id_testne_igre, "C")


@bottle.get('/')
def prva_stran():
    return bottle.template('Repozitorij/vislice/views/index.tpl')

@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # POST naredi novo igro, reusmeri na naslov za igranje te nove igre
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path="/")
    bottle.redirect('/igra/')
    return

#Moramo preusmeruti na GET ker bi drugače ob osvežitvi vse izgubili
@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    (igra, poskus) = vislice.igre[id_igre]
    return bottle.template('Repozitorij/vislice/views/igre.tpl', igra=igra, id_igre=id_igre, poskus=poskus)

#Če imaš post metodo VEDNO nato redirectaj na GET
@bottle.post('/igra/')
def ugibaj_crko():
    crka = bottle.request.forms.getunicode("poskus")
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')



bottle.run(debug=True, reloder=True)
