from collections import Counter


x = int(input())
n = int(input())

valores = []
for _ in range(n): # guarda os valores lidos na lista
    valores.append(int(input()))

qtd = 0
for num in valores: # percorre a lista e verifica quais são iguais a x
    if num == x:
        qtd += 1

c = Counter(valores)
print(c[x]) # quantidade de vezes que "x" ocorre em "valores"

'''v = [np.random.randint(0, 10) for i in range(10)]

type(v)
list'''