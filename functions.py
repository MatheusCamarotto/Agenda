contatos = {}

def salvar_contato():
    nome = input("Insira o nome do contato: ").lower().strip()
    telefone = input("Insira o telefone do contato: ")
    email = input("Insira o email do contato: ")
    favorito = input("Deseja favoritar o contato?(s = sim, n = não) ").lower().strip()
    contatos[nome] = {'telefone': telefone, 'email': email}
    if favorito == 's':
        contatos[nome].update({'favorito': True})
    elif favorito == 'n':
        contatos[nome].update({'favorito': False})
    else:
        print("Opção invalida!")


def visualizar_contatos():
    for contato, infos in contatos.items():
        telefone = infos.get('telefone')
        email = infos.get('email')
        favorito = 'Favoritado' if infos['favorito'] == True else ''
        print(f'{contato} \nTelefone: {telefone} \nEmail: {email} \n{favorito}')

