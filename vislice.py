import bottle, model

vislice = model.Vislice()

# id_testne_igre = vislice.nova_igra()
# (testna_igra, poskus) = vislice.igre[id_testne_igre]
# Dodajmo teste:
# vislice.ugibaj(id_testne_igre, "A")
# vislice.ugibaj(id_testne_igre, "B")
# vislice.ugibaj(id_testne_igre, "C")


@bottle.get('/')
def prva_stran():
    return bottle.template('Repozitorij/vislice/views/index.tpl')

@bottle.post('/igra/')
def zacni_novo_igro():
    # POST naredi novo igro, reusmeri na naslov za igranje te nove igre
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}'.format(id_igre))
    return

#Moramo preusmeruti na GET ker bi drugače ob osvežitvi vse izgubili
@bottle.get('/igra/<id_igre:int>')
def prikazi_igro(id_igre):
    (igra, poskus) = vislice.igre[id_igre]
    return bottle.template('Repozitorij/vislice/views/igre.tpl', igra=igra, id_igre=id_igre, poskus=poskus)

#Če imaš post metodo VEDNO nato redirectaj na GET
@bottle.post('/igra/<id_igre:int>')
def ugibaj_crko(id_igre):
    crka = bottle.request.forms.getunicode("poskus")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}'.format(id_igre))




bottle.run(debug=True, reloder=True)
