import random
kleur = ['oranje', 'blauw', 'groen', 'bruin', 'geel']

def zakje():
    zak = []
    amount = int(input("Hoe veel M & M rap god wilt u? "))
    # zak.append(amount)
    for __i__ in range(amount):
        rand = random.randrange(len(kleur))
        zak.append(kleur[rand])
    return zak

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

def sorteer_zak(zak):
    if isinstance(zak, dict):
        return dict(sorted(zak.items()))
    elif isinstance(zak, list):
        return sorted(zak)
    else:
        print("Try again: koekwous. ")
        sorteer_zak(zak)
zakje_een = zakje()
zakje_twee = zakjedeeltwee()

print(f"zakje_een \n unsorted: {zakje_een} \n sorted: {sorteer_zak(zakje_een)}")
print(f"zakje_twee \n unsorted: {zakje_twee} \n sorted: {sorteer_zak(zakje_twee)}")