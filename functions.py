contatos = {}

def salvar_contato():
    nome = input("Insira o nome do contato: ").lower().strip()
    telefone = input("Insira o telefone do contato: ").strip()
    email = input("Insira o email do contato: ").strip()
    contatos[nome] = {'telefone': telefone, 'email': email}
    while True:
        favorito = input("Deseja favoritar o contato?(s = sim, n = não) ").lower().strip()
        if favorito == 's':
            contatos[nome].update({'favorito': True})
            break
        elif favorito == 'n':
            contatos[nome].update({'favorito': False})
            break
        else:
            print("Opção invalida!")


def visualizar_contatos():
    for contato, infos in contatos.items():
        telefone = infos.get('telefone')
        email = infos.get('email')
        favorito = 'Favoritado' if infos['favorito'] == True else ''
        print("-------------------------------")
        print(f'{contato} \nTelefone: {telefone} \nEmail: {email} \n{favorito}')

def editar_contatos():
    while True:
        visualizar_contatos()
        op = input("Qual contato deseja editar? ")
        if op in contatos:
            op_edicao = input(f"1 - Alterar nome \n2 - Alterar número \n3 - Alterar Email \n4 - (des)Favoritar\n5 - Apagar Contato\n")
            match op_edicao:
                case '1':
                    new_name = input("Nome: ")
                    contatos[new_name] = contatos.pop(op)
                    print("Nome atualizado com sucesso!")
                    break
                case '2':
                    new_number = input("N° de Telefone: ")
                    contatos[op]['telefone'] = new_number
                    print("Numero atualizado com sucesso!")
                    break
                case '3':
                    new_email = input("Endereço de Email: ")
                    contatos[op]['email'] = new_email
                    print("Email atualizado com sucesso!")
                    break
                case '4':
                    contatos[op]['favorito'] = not contatos[op].get('favorito')
                    print("Atualizado com sucesso!")
                    break
                case '5':
                    contatos.pop(op)
                    break
                case _:
                    print("Opção invalida!")
        else:
            print("Esse contato não existe!")
                 
def visualizar_favoritos():
    for contato, infos in contatos.items():
        telefone = infos.get('telefone')
        email = infos.get('email')
        favorito = 'Favoritado' if infos['favorito'] == True else ''
        if infos['favorito'] == True:
            print("-------------------------------")
            print(f'{contato} \nTelefone: {telefone} \nEmail: {email} \n{favorito}')

