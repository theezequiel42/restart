import random;
print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randint(1, 100)
total_de_tentativas = 0
pontos = 1000

print("Escolha o nível de dificuldade:")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if nivel == 1:
        total_de_tentativas = 20
elif nivel == 2:
        total_de_tentativas = 10
else:
        total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto}!")
            print(f"Sua pontuação final é {pontos} pontos.")
            break
        else:
            if maior:
                print("Seu chute foi maior que o número secreto.")
            elif menor:
                print("Seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

else:
        print(f"O número secreto era {numero_secreto}. Melhor sorte na próxima vez!")
