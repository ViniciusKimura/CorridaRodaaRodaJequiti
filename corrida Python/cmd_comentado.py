# (A)Ambulancia (B)Bombeiro (C)CorsadaKath
# Painel com 6 'bolinhas' de cada carro
# Pista com 3 carros e 5 casas, ganha quem completar 5 pontos primeiro
# O andar dos Carros será definido por um while, os números deverão ser selecionados pelo Usuário

# biblioteca utilizada para gerar números aleatórios 
import random

# função responsável por criar o painel e o painel_front
def criaPainel():
    painel = []
    # o painel front não tem segredo, ele sempre vai ser uma lista de 18 valores com numeros de 0 a 17, que é o que o usuário vai digitar 
    # para selecionar o 'bloco' que ele quer abrir
    painel_front = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    # o aleatorio é a variavel que vai receber o numero aleatorio.
    aleatorio = 0
    # a, b e c são utilizados para contar o numero de tipos de carro que já estão na tabela, conforme elas vão sendo colocadas na lista, elas vão sendo acrescentadas
    a = 0
    b = 0
    c = 0
    # for loop que vai passar por todas as 18 casas do painel
    for i in range(18):
        while True:
            # o while começa gerando um numero aleatorio de 1 a 3 (1 = A, 2 = B e 3 = C)
            aleatorio = random.randint(1, 3)
            # esse if verifica se o numero gerado corresponde a A, B ou C e se essa letra já ultrapassou o limite de 6 letras dentro do painel
            # se ele tiver ultrapassado o limite, ele gera outro numero e faz a verificação de novo, caso contrario, ele adiciona essa letra no painel
            # e incrementa em 1 a variavel correspondente à aquela letra e quebra o while, assim passando para a proxima casa do painel  
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

# essa função faz a verificação do número que o usuario escolheu e atualiza o painel e o placar
def pickNumero(numero, a, b, c):
    # aqui é bem simples, ele verifica o item que o usuario escolheu, e é aquele mesmo esquema, A = 1, B = 2, C = 3, e ele atualiza o placar de acordo com o carro no painel
    # ele também muda o painel_front, ele muda o valor do numero da casa para o valor correspondente no painel
    if painel[numero] == 1:
        painel_front[numero] = 'A'
        a += 1
    elif painel[numero] == 2:
        painel_front[numero] = 'B'
        b+= 1
    elif painel[numero] == 3:
        painel_front[numero] = 'C'
        c += 1
    # após fazer as alterações acima, ele altera a casa escolhida pelo usuário para 0
    painel[numero] = 0

    return painel_front[numero], a, b, c


# essa daqui é a função principal, é o que vai rodar primeiro na execução do programa
if __name__ == '__main__':
    # inicializa as variaveis a, b e c, que representam a casa em que o carro está. 
    a = 0
    b = 0
    c = 0
    # o check é utilizado para armazenar qual que foi ok ultimo carro 'sorteado'. É usado apenas para efeitos visuais
    check = 'N/A'
    # roda a função criaPainel() para preencher as variaveis painel e painel_front
    painel, painel_front = criaPainel()

    # loop principal do programa
    while True:
        # verifica se algum dos carros já chegou na linha de chegada, caso sim, o programa sai do loop
        if a == 6 or b == 6 or c == 6:
            break
        # esse é basicamente o visual do programa, é onde é mostrado qual foi a ultima letra tirada, o painel com os números restantes e as
        # letras já tiradas e a posição de cada um dos carros
        print("ULTIMA LETRA TIRADA: " + str(check))
        print(painel_front)
        print("A: " + str(a))
        print("B: " + str(b))
        print("C: " + str(c))
        # esse while vai rodar até o usuário digitar um número válido
        while True:
            numero = int(input("Digite o número: "))
            # verifica se o numero escolhido já foi escolhido
            if painel[numero] == 0:
                print("Digite um número que não foi escolhida")
            # verifica se o numero está entre 0 e 17
            elif numero < 0 or numero > 17:
                print("Digite um número que esteja no painel")
            # caso contrario, ele para o while e segue com o programa
            else:
                break
        # aqui ele roda a função pickNumero() e atualiza os valores do check e as posições dos carros. Lembrando que dentro da função ainda são atualizados os valores de dentro do painel_front.
        check,a,b,c = pickNumero(numero, a, b, c)
        print("_________________________________")
        # basicamente pula a linha 40x para dar uma sensação de pular de linha
        print("\n"*40)
    # aqui é o final do programa, depois que o loop principal do programa foi interrompido. Aqui ele verifica qual dos carros chegou no final e mostra uma mensagem de acordo
    if a == 6: result = 'A'
    elif b == 6: result = 'B'
    elif c == 6: result = 'C'
    print("O vencedor da corrida foi: " + result)