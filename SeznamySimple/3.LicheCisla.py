Zacatek = int(input("Zadej první číslo: "))

Konec = int(input("Zadej poslední číslo: "))


def funkcos():
    if Konec > Zacatek:
        for cislos in range(Zacatek, Konec + 1):
            if cislos % 2 != 0:
                print(cislos, end=" ")
    else:
        print("To mi nevychádza, jak může být konečné číslo větší jako to na začátku")


print("\nTvoje čísla jsou:")

funkcos()
#trochu sis upravil zadani, vysledkem ma byt soucet
