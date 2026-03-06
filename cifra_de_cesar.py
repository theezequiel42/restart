#desafio: Cifra de Cesar

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = int(input('Digite a chave de deslocamento: '))

texto = input('Digite o texto a ser cifrado: ')

texto_cifrado = ''
for letra in texto:
    if letra in alfabeto:
        indice = (alfabeto.index(letra) + chave) % 26
        texto_cifrado += alfabeto[indice]
    else:
        texto_cifrado += letra

print('Texto cifrado:', texto_cifrado)