dyszki = [10 * i for i in range(1, 11)]
print(dyszki)

lista = ["zuza", "ala", 78, 3.41]
lista2 = range(1,100)
krotka = (8.0, 6.0)

# petla typu "for each"
for element in lista:
    print(element)

for i in range(len(lista)):
    print(lista[i])

kol1, kol2, skladka, pi = lista #indeksowanie
print("kol1", kol1)

krotka = (8.0, 6.0)
x, y = krotka
print("x =", x)

for idx, element in enumerate(lista):
    print(idx, ":", element, lista[idx])

zdanie = "Grazynka nie lubi dupysaca"
fragment = zdanie[-8:]
print(fragment)

# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))