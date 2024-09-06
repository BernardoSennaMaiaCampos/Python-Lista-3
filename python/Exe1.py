((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))

lista0 = (1,5,6,10)
lista00 = sum(lista0)
print(f"0: {lista00}")

lista1 = (2,4,6,8)
lista11 = sum(lista1)
print(f"1: {lista11}")

lista2 = (2)
print(f"2: {lista2}")

lista3 = (10,20,30,10,80)
lista33 = sum(lista3)
print(f"3: {lista33}")

listaMedia = (lista00) + (lista11) + (lista2) + (lista33)
media = listaMedia / 2

print(f"Media : {media}")
