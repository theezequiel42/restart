# Desafio iteração com múltiplas listas. Pt.2

# Dado duas listas, printe uma mensagem dizendo se existe

# algum elemento em comum entre elas ou não

lista1 = [2, 3, 4, 6]
lista2 = [1, 2, 6, 9, 10]  
comum = False
for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            print(f'Valor em comum encontrado: {valor1}')

# Segundo exemplo
lista3 = [10.0,'banana',True]
lista4 = ['maçã',False,20]
comum = False
for valor3 in lista3:
    if comum:
        break
    for valor4 in lista4:
        if valor3 == valor4:
            compum = True
            break

if comum:
    print(f'Existe pelo menos um valor em comum entre as listas {lista3} e {lista4}.')
else:
    print(f'Não existe nenhum valor em comum entre as listas {lista3} e {lista4}.')

