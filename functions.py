contatos = {}

def salvar_contato():
    nome = input("Insira o nome do contato").lower().strip()
    telefone = input("Insira o telefone do contato")
    email = input("Insira o email do contato")

    contatos[nome] = {'telefone': telefone, 'email': email}
