# (A)Ambulancia (B)Bombeiro (C)CorsadaKath
# Painel com 6 'bolinhas' de cada carro
# Pista com 3 carros e 5 casas, ganha quem completar 5 pontos primeiro
# O andar dos Carros será definido por um while, os números deverão ser selecionados pelo Usuário

import random


def criaPainel():
    painel = []
    painel_front = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    aleatorio = 0
    a = 0
    b = 0
    c = 0
    for i in range(18):
        while True:
            aleatorio = random.randint(1, 3)
            if (aleatorio == 1 and a < 6):
                painel.append(aleatorio)
                a += 1
                break
            elif (aleatorio == 2 and b < 6):
                painel.append(aleatorio)
                b += 1
                break
            elif (aleatorio == 3 and c < 6):
                painel.append(aleatorio)
                c += 1
                break
    return painel, painel_front


def pickNumero(numero, a, b, c):
    if painel[numero] == 1:
        painel_front[numero] = 'A'
        a += 1
    elif painel[numero] == 2:
        painel_front[numero] = 'B'
        b+= 1
    elif painel[numero] == 3:
        painel_front[numero] = 'C'
        c += 1
    painel[numero] = 0

    return painel_front[numero], a, b, c

if __name__ == '__main__':
    a = 0
    b = 0
    c = 0
    check = 'N/A'
    painel, painel_front = criaPainel()

    while True:
        if a == 6 or b == 6 or c == 6:
            break
        print("ULTIMA LETRA TIRADA: " + str(check))
        print(painel_front)
        print("A: " + str(a))
        print("B: " + str(b))
        print("C: " + str(c))
        while True:
            numero = int(input("Digite o número: "))
            if painel[numero] == 0:
                print("Digite um número que não foi escolhida")
            elif numero < 0 or numero > 17:
                print("Digite um número que esteja no painel")
            else:
                break
        check,a,b,c = pickNumero(numero, a, b, c)
        print("_________________________________")
        print("\n"*40)
    if a == 6: result = 'A'
    elif b == 6: result = 'B'
    elif c == 6: result = 'C'
    print("O vencedor da corrida foi: " + result)