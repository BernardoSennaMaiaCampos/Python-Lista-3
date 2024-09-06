n1 = 1
n2 = 1
lista1 = []
lista2 = []
print("Soma da serie = ", end ="")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    lista1.append(n1)
    lista2.append(n2)
    n1 += 1
    n2 += 2
print(n1, "/", n2, " = ", sum(lista1), "/", sum(lista2))