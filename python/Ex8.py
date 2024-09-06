vetor = []
i = 0

print("Digite 5 números para adicioná-los ao vetor:")
while i <= 5:
    vetor.append(int(input()))
    i+=1
i = 0

encontreValor = int(input("Encontre a posição de uma valor dentro do vetor: "))
valorEncontrado = False

while i <= 5:
    if encontreValor == vetor[i]:
        print("O valor ", encontreValor, " está na posição: ", i, " do vetor")
        valorEncontrado = True
    i+=1    
if valorEncontrado == False:
    print("-1")