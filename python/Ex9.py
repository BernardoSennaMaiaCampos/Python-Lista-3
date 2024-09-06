from random import randint


def dados():
    numeros = []

    for i in range (1,51):
        n = randint(1,6)
        numeros.append(n)
        porcentagem = round((numeros.count(6)/50)*100, 2)
    print(f'O percentual de vezes que o número 6 aparece é: {porcentagem}%')

if __name__ == "__main__":

    dados()        