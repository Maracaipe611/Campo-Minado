import numpy as np
import random

# Definições da matriz:
# 0: casa vazia
# 1: casa com bomba
# 2: casa cavada
# 3: casa aberta sem bomba
# 4: casa aberta com bomba


class Casas:
    def __init__(self, matriz, posicaoX, posicaoY):
        self.Superior = 0 if (
            posicaoY + 1 >= 8) else matriz[posicaoX][posicaoY + 1]
        self.Direito = 0 if (
            posicaoX + 1 >= 8) else matriz[posicaoX + 1][posicaoY]
        self.Inferior = 0 if (
            posicaoY - 1 <= 0) else matriz[posicaoX][posicaoY - 1]
        self.Esquerdo = 0 if (
            posicaoX - 1 <= 0) else matriz[posicaoX - 1][posicaoY]
        self.SuperiorEsquerdo = 0 if (
            posicaoX - 1 <= 0 or posicaoY + 1 >= 8) else matriz[posicaoX - 1][posicaoY + 1]
        self.SuperiorDireito = 0 if (
            posicaoY + 1 >= 8 or posicaoX + 1 >= 8) else matriz[posicaoX + 1][posicaoY + 1]
        self.InferiorDireito = 0 if (
            posicaoX - 1 <= 0 or posicaoX + 1 >= 8) else matriz[posicaoX + 1][posicaoY - 1]
        self.InferiorEsquerdo = 0 if (
            posicaoX - 1 <= 0 or posicaoY - 1 <= 0) else matriz[posicaoX - 1][posicaoY - 1]


class Table:
    def generateTable(dificuldade):
        matriz = np.zeros((8, 8))
        matriz = Table.sortPumps(matriz, dificuldade)
        return matriz

    def sortPumps(matriz, dificuldade):
        if(dificuldade == '1'):
            dificuldade = 5
        elif(dificuldade == '2'):
            dificuldade == 3
        elif(dificuldade == '3'):
            dificuldade = 2
        # elemento da matriz vai ter bomba dependendo da dificuldade. Se caso o número sortido, for dividendo da dificuldade, a casa terá bomba
        for x in range(8):
            for y in range(8):
                matriz[x][y] = 1 if random.randint(
                    0, 9) % dificuldade == 0 else 0

        return matriz

    def getPumpsAround(matriz, posicaoX, posicaoY):
        pumpCount = 0
        vizinho = Casas(matriz, posicaoX, posicaoY)

        if(vizinho.Superior == 1 or vizinho.Superior == 4):
            pumpCount = pumpCount + 1
        if(vizinho.Inferior == 1 or vizinho.Inferior == 4):
            pumpCount = pumpCount + 1
        if(vizinho.Esquerdo == 1 or vizinho.Esquerdo == 4):
            pumpCount = pumpCount + 1
        if(vizinho.Direito == 1 or vizinho.Direito == 4):
            pumpCount = pumpCount + 1
        if(vizinho.SuperiorDireito == 1 or vizinho.SuperiorDireito == 4):
            pumpCount = pumpCount + 1
        if(vizinho.SuperiorEsquerdo == 1 or vizinho.SuperiorEsquerdo == 4):
            pumpCount = pumpCount + 1
        if(vizinho.InferiorDireito == 1 or vizinho.InferiorDireito == 4):
            pumpCount = pumpCount + 1
        if(vizinho.InferiorEsquerdo == 1 or vizinho.InferiorEsquerdo == 4):
            pumpCount = pumpCount + 1

        return str(pumpCount)

    def maskTable(matriz):
        maskedMatriz = np.zeros((8, 8), dtype='object')
        for x in range(8):
            for y in range(8):
                if(matriz[x][y] == 0 or matriz[x][y] == 1):
                    maskedMatriz[x][y] = "\u2588"
                elif(matriz[x][y] == 2):
                    maskedMatriz[x][y] = Table.getPumpsAround(matriz, x, y)
                elif(matriz[x][y] == 3 or matriz[x][y] == 4):
                    maskedMatriz[x][y] = "\u2705"
        return maskedMatriz

    def changeMatriz(matriz, playerInput):

        casaX = playerInput.Casa
        colunaY = playerInput.Coluna
        acao = playerInput.Acao
        casaSelecionada = matriz[casaX][colunaY]

        if(acao == "CAVAR"):
            if (casaSelecionada == 0 or casaSelecionada == 3):
                # casa deixa de ser um misterio, e passa a estar escavada
                matriz[casaX][colunaY] = 2
            elif(casaSelecionada == 1 or casaSelecionada == 4):
                print("ESSA CASA TINHA UMA BOMBA!")
                exit()
            elif(casaSelecionada == 2):
                print("Você já explorou essa casa, selecione outra")

        elif(acao == "ABRIR"):
            if(casaSelecionada == 0):
                # marcar uma casa q está vazia
                matriz[casaX][colunaY] = 3
            elif(casaSelecionada == 1):
                matriz[casaX][colunaY] = 4
            elif(casaSelecionada == 3):
                print("Você já marcou essa casa, selecione outra")

    def matrizIsOver(matriz):
        todasAsCasasForamExploradas = True
        for x in range(8):
            for y in range(8):
                if(matriz[x][y] == 0 or matriz[x][y] == 3):
                    # se ainda houver casas q não foram cavadas e q n tem bombas, o jogo n termina
                    todasAsCasasForamExploradas = False

        return todasAsCasasForamExploradas
