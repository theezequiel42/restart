correct_username = "admin"
correct_password = "1234"

user = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if user == correct_username and senha == correct_password:
    print("Acesso concedido.")
elif user != correct_username and senha == correct_password:
    print(f"Usuário {user} não encontrado.")    
elif user == correct_username and senha != correct_password:
    print("Senha incorreta.")
else:   
    print("Acesso negado.") 

