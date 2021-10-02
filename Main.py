# Digite tres informacoes separadas por vırgula: Linha da
# casa (1 a 8), coluna da casa (1 a 8) e se ´e pra cavar ou abrir (0 pra cavar, 1 para abrir)”

from Table import *
import os
def clear(): return os.system('cls')


Finished = False


class Player:
    def __init__(self, Casa, Coluna, Acao):
        self.Acao = Acao
        self.Coluna = Coluna
        self.Casa = Casa


def getPlayerInput(matriz):
    print(Table.maskTable(matriz))
    print(
        "Informe a sua jogada conforme o modelo a seguir: [Casa], [Coluna], [Cavar/Abrir]\n Casa: 1-8,\n Coluna: 1-8,\n Cavar = 0 / Abrir = 1\n")
    inputOfPlayer = input()
    inputOfPlayer = validateInput(inputOfPlayer, matriz)
    return inputOfPlayer


def validateInput(inputOfPlayer, matriz):
    try:
        input = inputOfPlayer.split()

        input[0] = int(input[0].replace(",", ""))
        input[1] = int(input[1].replace(",", ""))
        input[2] = int(input[2].replace(",", ""))

        playerInput = Player((input[0] - 1), (input[1] - 1), input[2])

        if (playerInput.Casa < 0 or playerInput.Casa >= 8 or
            playerInput.Coluna < 0 or playerInput.Coluna >= 8 or
                playerInput.Acao < 0 or playerInput.Acao > 1):
            clear()
            print("Valores inseridos estão incorretos, digite novamente!")
            getPlayerInput(matriz)
    except:
        print("Erro ao validar as informações de entrada, tente novamente!")
        getPlayerInput(matriz)

    playerInput.Acao = "CAVAR" if playerInput.Acao == 0 else "ABRIR"
    print("Você escolheu Casa: %d, Coluna: %d, Acao: %s," %
          (playerInput.Casa + 1, playerInput.Coluna + 1, playerInput.Acao))
    return playerInput


print("Selecione a dificuldade: \n1- Fácil\n2-Médio\n3- Difícil")
dificuldade = input()
matriz = Table.generateTable(dificuldade)
while(Finished is False):
    clear()
    print("------- MINA ------")
    inputOfPlayer = getPlayerInput(matriz)
    print("-------------------")
    NewMatriz = Table.changeMatriz(matriz, inputOfPlayer)
    Finished = Table.matrizIsOver(matriz)

print("Parabéns!! Você ganhou :)")
