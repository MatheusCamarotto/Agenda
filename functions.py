contatos = {}

def salvar_contato():
    nome = input("Insira o nome do contato: ").lower().strip()
    telefone = input("Insira o telefone do contato: ")
    email = input("Insira o email do contato: ")

    contatos[nome] = {'telefone': telefone, 'email': email}

def visualizar_contatos():
    for contato, infos in contatos.items():
        telefone = infos.get('telefone')
        email = infos.get('email')
        print(f'{contato} \nTelefone: {telefone} \nEmail: {email}')

