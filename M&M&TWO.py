import random
kleur = ['oranje', 'blauw', 'groen', 'bruin', 'geel']

def zakjedeeltwee():
    global kleur
    zak = {}
    amount = int(input("Hoe veel M & M rap god wilt u? "))
    for __i__ in range(amount):
        rand = random.randrange(len(kleur)) #generate random index key
        huidig_kleur = kleur[rand]#get color based index key
        if huidig_kleur in zak:
            # zak huidigKluer + 1
            zak[huidig_kleur] +=1 
        else:
            # zak huidigkleur aanmaken = 1
            zak[huidig_kleur] = 1
    return zak
print(zakjedeeltwee())

