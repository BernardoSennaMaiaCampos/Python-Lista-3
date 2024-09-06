from collections import Counter
from statistics import mode 

numeros = [1, 67, 78, 34, 90, 876, 0, 12, 8, 3, 56, 987, 3, 2,45,12,10, 45]

contador = Counter(numeros)

repetidos = [
    item for item, quantidade in contador.items() 
        if quantidade > 1
]

quantidade_repetidos = len(repetidos)

print(f'Há {quantidade_repetidos} números repetidos na lista')


#for i in range(5):
   # x = i.split(",")
    #numeros.append(int(f"Número:{x} "))
    
   
   #porcentagem = round((numeros.count(6)/50)*100, 2)