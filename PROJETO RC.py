# NOME: João Vitor Ferreira Antunes de Lima
# CURSO: Tecnologia em Análise e Desenvolvimento de Sistemas


# FUNÇOES
def menu():
    print("-----MENU PRINCIPAL-----")
    print("1. Gerenciar Estudantes")
    print("2. Gerenciar Disciplinas")
    print("3. Gerenciar Professores")
    print("4. Gerenciar Turmas")
    print("5. Gerenciar Matrículas")
    print("0. Sair")

def submenu():
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Menu Principal")
    funcao = input("Informe a operação desejada: ")
    if funcao == "1" or funcao.lower() == "incluir":
        incluir()
    elif funcao == "2" or funcao.lower() == "listar":
        listar()
    elif funcao == "3" or funcao.lower() == "atualizar":
        atualizar()
    elif funcao == "4" or funcao.lower() == "excluir":
        excluir()
    elif funcao == "0" or funcao.lower() == "menu principal":
        menu_atual = "1".
    else:
        print()
        print("Operação Selecionada: INVÁLIDA. Tente novamente\n")

def incluir(lista):
        print()
        print("Operação Selecionada: === INCLUIR ===")
        try:
            cod = int(input("Digite o código: "))
            nome = str(input("Digite o nome: "))
            cpf = int(input("Digite o CPF: "))
            cadastro = [cod, nome, cpf]
            lista.append(cadastro)
            print("Usuário cadastrado com sucesso.\n")
        except ValueError:
            print("Ação inválida. Tente novamente.")

def atualizar(lista):
    print()
    print("Operação Selecionada: === ATUALIZAR ===")
    if len(lista) == 0:
        print("Não há usuários cadastrados\n")
    else:
        try:
            cod = int(input("Informe o código do usuário a ser editado: "))
            for registro in lista:
                if cod == registro[0]:
                    registro[0] = int(input("Digite o código: "))
                    registro[1] = str(input("Digite o nome: "))
                    registro[2] = int(input("Digite o CPF: "))
                else:
                    print("Código inválido. Tente novamente.")
        except ValueError:
            print("Ação inválida. Tente novamente.")

def listar(lista):
    print()
    print("Operação Selecionada: === LISTAR ===")
    if len(lista) == 0:
        print("Não há usuários cadastrados\n")
    else:
        for i in range(len(lista)):
            cadastro = lista[i]
            print("Código: ", cadastro[0])
            print("Nome: ", cadastro[1])
            print("CPF: ", cadastro[2], "\n")

def excluir(lista):
    print()
    print("Operação Selecionada: === EXCLUIR ===")
    if len(lista) == 0:  # Caso não haja itens na lista, executará este loop.
        print("Não há usuários cadastrados\n")
    else:
        try:
            cod = int(input("Informe o código do usuário a ser excluído: "))
            for registro in lista_estudantes:
                if cod == registro[0]:
                    lista.remove(registro)
                    print("O usuário foi excluído com sucesso.\n")
                else:
                    print("Código inválido. Tente novamente.")
        except ValueError:
            print("Ação inválida. Tente novamente.")

# IMPORTANTE


menu_atual = "1" # O valor "menu_atual" é utilizado para navegação entre os menus.
lista_estudantes = []
lista_professores = []

# MENU PRINCIPAL
# Loop inicial para apresentação do menu principal.
while menu_atual == "1":
    menu()
    proximo = input("Informe o menu desejado: ")
    if proximo == "0" or proximo.lower() == "sair":
        print("Encerrando aplicação. Até a próxima! =)")
        menu_atual = "0"

    # ESTUDANTES

    elif proximo == "1" or proximo.lower() == "gerenciar estudantes":
        menu_atual = "2"
        lista = lista_estudantes
        while menu_atual == "2":
            print("---{ESTUDANTES} Menu de Operações---")
            submenu()

    # DISCIPLINAS

    elif proximo == "2" or proximo.lower() == "gerenciar disciplinas":
        print("EM DESENVOLVIMENTO\n")

    # PROFESSORES

    elif proximo == "3" or proximo.lower() == "gerenciar professores":
        menu_atual = "4"
        lista = lista_professores
        while menu_atual = "4"
            print("---{ESTUDANTES} Menu de Operações---")
            submenu()
    # TURMAS

    elif proximo == "4" or proximo.lower() == "gerenciar turmas":
        print("EM DESENVOLVIMENTO\n")

    # MATRÍCULAS

    elif proximo == "5" or proximo.lower() == "gerenciar matrículas":
        print("EM DESENVOLVIMENTO\n")

    else:
        print("Operação Selecionada: INVÁLIDA. Tente novamente\n")