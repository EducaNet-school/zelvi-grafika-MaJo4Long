hodnota = 1

vyska = int(input("Zadej číslo kterým chceš končit:"))

seznam = []

for num in range(hodnota, vyska+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            seznam.append(num)
print(seznam)
#moc pekne, drobnost: poprve je v cyklu num == 1
#takze to vzdy preskocis. Zacni od 2 a podminku na
#radku 8 vyhod
