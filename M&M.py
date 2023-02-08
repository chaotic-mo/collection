import random
kleur = ['oranje', 'blauw', 'groen', 'bruin', 'geel']

def zakje():
    zak = []
    amount = int(input("Hoe veel M & M rap god wilt u? "))
    zak.append(amount)
    for __i__ in range(amount):
        rand = random.randrange(len(kleur))
        zak.append(kleur[rand])
    return zak

print(zakje())

