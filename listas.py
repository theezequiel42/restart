numeros = [1,2,3,4,5,6,7,8,9,10]
outros_numeros = [11,12,13,14,15]
soma = 0
maximo = numeros[0]

for numero in numeros:
    soma += numero
    if numero > maximo:
        maximo = numero

media = soma / len(numeros)

print(f'A média dos números é {media} , a soma é {soma} e o máximo é {maximo}')

palavras = ['maçã', 'banana', 'laranja', 'uva']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'A palavra "{palavra}" tem 5 ou mais letras.')