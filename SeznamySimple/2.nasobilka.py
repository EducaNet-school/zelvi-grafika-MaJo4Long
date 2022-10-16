cislos = int(input("Zadej číslo malé násobilky od 1 do 10: "))

seznamos = []


def cislosnasobilka():
    if 11 > cislos >= 2:

        for nasobek in range(1, 11):
            seznamos.append(cislos * nasobek)
            print(cislos, '*', nasobek, '=', cislos * nasobek)

    else:
        print("To jsi přehnal, řekl jsem přece malou násobilku!")

    print("Zde je malá násobilka tvých čísel v seznamu:", seznamos)


cislosnasobilka()
#chvalim zabaleni do funkce (naucime se pouzit trochu lepe) a taky kontrolu uzivatelskeho vstupu
