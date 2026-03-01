# Desafio: Contar vogais em uma string

texto = """
python é uma linguagem de programação de alto nível, interpretada e de propósito geral.
Ela é conhecida por sua sintaxe clara e legibilidade, o que a torna uma ótima escolha para iniciantes e profissionais.

"""

vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}

for char in texto.lower():
    if char in vogais:
        vogais[char] += 1
print("Contagem de vogais:")

for vogal, contagem in vogais.items():
    print(f"{vogal}: {contagem}")   