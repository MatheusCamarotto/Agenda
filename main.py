from functions import *

def main():
    while True:
        print("-------------------------------")
        print("1 - Salvar Novo Contato")
        print("2 - Visualizar Contatos")
        print("3 - Visualizar Favoritos")
        print("4 - Editar Contatos")
        print("5 - Sair")
        print("-------------------------------")
        op = input("Selecione a opção desejada: ")
        
        match op:
            case '1':
                salvar_contato()
            case '2':
                visualizar_contatos()
            case '3':
                visualizar_favoritos()
            case '4':
                editar_contatos()
            case '5':
                exit()
            case _:
                print("Opção invalida!")

if __name__ == "__main__":
    main()