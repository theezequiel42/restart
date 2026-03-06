# pergunta a capital dos estados brasileiros
#confere resposta do usuário
#A cada pegunta, o usuario pode parar o jogo ou continuar
#no final do jogo, o programa mostra quais perguntas o usuário acertou e quais errou
#o programa mostra o total de acertos e erros do usuário e a porcentagem de acertos

import random

estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

acertos = []
erros = []
for estado, capital in random.sample(list(estados_capitais.items()), k=len(estados_capitais)):
    
    resposta = input(f'Qual é a capital de {estado}? (Digite "sair" para encerrar o jogo) ')
    
    if resposta.lower() == 'sair':
        break
    
    if resposta.strip().lower() == capital.lower():
        print('Resposta correta!')
        acertos.append(estado)
    else:
        print(f'Resposta incorreta! A capital de {estado} é {capital}.')
        erros.append(estado)

print('\nResumo do jogo:')
print(f'Acertos: {len(acertos)} - {", ".join(acertos)}')
print(f'Erros: {len(erros)} - {", ".join(erros)}')
total_perguntas = len(acertos) + len(erros)
if total_perguntas > 0:
    porcentagem_acertos = (len(acertos) / total_perguntas) * 100
    print(f'Porcentagem de acertos: {porcentagem_acertos:.2f}%')
else:
    print('Nenhuma pergunta foi respondida.')

 