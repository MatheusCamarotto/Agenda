from functions import *

def main():
    while True:
        print("-------------------------------")
        print("1 - Salvar Novo Contato")
        print("2 - Visualizar Contatos")
        print("3 - Visualizar Favoritos")
        print("4 - Sair")
        print("-------------------------------")
        op = input("Selecione a opção desejada: ")
        
        match op:
            case '1':
                salvar_contato()
            case '1':
                visualizar_contatos()
            case '1':
                visualizar_favoritos()
            case '1':
                exit()


if __name__ == "__main__":
    main()