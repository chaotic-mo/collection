def alles():
    vraag = input("Wat wilt u zien a) week, b) arrithmathic display, c) random game: ")
    vraag = vraag.lower()
    if vraag == 'a':
        week()
    elif vraag == 'b':
        math()
    elif vraag == 'c':
        spelProgramma(spelList, 3, 11)
    else:
        print("sorry probeer het nog eens")
        alles()

dagen = ['Maandag', 'Dinsdag', 'Woendag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']
def week():
    for dag in dagen:
        print(dag, end= ', ')
    print()
    for dag in dagen[0:5]:
        print(dag, end=', ' )
    print()
    for dag in dagen[5:7]:
        print(dag, end= ', ')
    print()
    dagen.reverse()
    for dag in dagen:
        print(dag, end= ', ')
    print()
    for dag in dagen[2:7]:
        print(dag, end= ', ')
    print()
    for dag in dagen[0:2]:
        print(dag, end= ', ')
    print()

listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def math():
    def addAndDisplayLists(list1, list2):
        for i in range(len(list1)):
            print('{:<2} + {:>2} = {:>3}'.format(list1[i], list2[i], list1[i] + list2[i]))

    addAndDisplayLists(listOne, listTwo)

    def subtractAndDisplayLists(list1, list2):
        for i in range(len(list1)):
            print('{:<2} - {:>2} = {:>3}'.format(list1[i], list2[i], list1[i] - list2[i]))

    subtractAndDisplayLists(listOne, listTwo)

    def multiplyAndDisplayLists(list1, list2):
        for i in range(len(list1)):
            print('{:<2} * {:>2} = {:>3}'.format(list1[i], list2[i], list1[i] * list2[i]))
    multiplyAndDisplayLists(listOne, listTwo)

    def divideAndDisplayLists(list1, list2):
        for i in range(len(list1)):
            print('{:<2} / {:>2} = {:>3}'.format(list1[i], list2[i], list1[i] / list2[i]))
    divideAndDisplayLists(listOne, listTwo)

import random
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimaal, maximum):
    for i in range(random.randrange(minimaal, maximum)):
        rand = random.randrange(len(spelList))
        print(f'{i+1} {spelList[rand]}')

alles()

