

import random

def gerar_baralho(copias=1, coringas=False, embaralhar=True):
    
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    baralho = []

    for _ in range(copias):
        for naipe in naipes:
            for valor in valores:
                baralho.append(f"{valor}{naipe}")

        if coringas:
            baralho.append("Coringa")
            baralho.append("Coringa")

    if embaralhar:
        random.shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):

    print(f"\nBaralho possui {len(baralho)} cartas:\n")

    for carta in baralho:
        print(carta, end=" ")

    print("\n")

def dar_as_cartas(baralho, jogadores, cartas_por_jogador):

    maos = []

    for _ in range(jogadores):
        mao = []
        for _ in range(cartas_por_jogador):
            if baralho:
                mao.append(baralho.pop())
        maos.append(mao)

    return maos

def mostrar_jogadores(maos):

    for i, mao in enumerate(maos, start=1):
        print(f"\nJogador {i} possui {len(mao)} cartas:")

        for carta in mao:
            print(carta, end=" ")

        print()

#exemplo de uso
if __name__ == "__main__":
    baralho = gerar_baralho(copias=2, coringas=True)
    mostrar_baralho(baralho)

    jogadores = 4
    cartas_por_jogador = 5
    maos = dar_as_cartas(baralho, jogadores, cartas_por_jogador)
    mostrar_jogadores(maos)


