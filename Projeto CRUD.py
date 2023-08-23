# NOME: João Vitor Ferreira Antunes de Lima
# CURSO: Tecnologia em Análise e Desenvolvimento de Sistemas


# FUNÇOES

import json

# Função para escrever no arquivo JSON.
def escrever_lista_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)

# Função para ler lista no arquivo JSON.
def ler_lista_do_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

# Função para exibir o menu principal e opções.
def menu():
    print("-----MENU PRINCIPAL-----")
    print("1. Gerenciar Estudantes")
    print("2. Gerenciar Disciplinas")
    print("3. Gerenciar Professores")
    print("4. Gerenciar Turmas")
    print("5. Gerenciar Matrículas")
    print("0. Sair")

# Função para exibir os menus secundários e executar suas funcionalidades de acordo com a entrada do usuário.
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
        menu_atual = "1"
    else:
        print()
        print("Operação Selecionada: INVÁLIDA. Tente novamente\n")

# As funções de incluir, atualizar e excluir lêem o arquivo JSON, e, posteriormente escrevem nele. A de listar apenas lê.
# A variável "existe" é utilizada para validar se há outro cadastro com o mesmo código.

# Função de cadastrar um usuário.

def incluir():
        print()
        print("Operação Selecionada: === INCLUIR ===")
        try:
            lista = ler_lista_do_json(nome_arquivo)
            existe = 0
            cod = int(input("Digite o código: "))
            for registro in lista:
                if cod == registro[0]:
                    print("Código de usuário já cadastrado.")
                    existe = 1
            if existe == 0:
                nome = str(input("Digite o nome: "))
                cpf = int(input("Digite o CPF: "))
                cadastro = [cod, nome, cpf]
                lista.append(cadastro)
                print("Usuário cadastrado com sucesso.\n")
                escrever_lista_em_json(lista, nome_arquivo)
        except ValueError:
            print("Ação inválida. Tente novamente.")

# Função de editar as informações de um usuário cadastrado.

def atualizar():
    print()
    print("Operação Selecionada: === ATUALIZAR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:
        print("Não há usuários cadastrados\n")
    else:
        try:
            cod = int(input("Informe o código do usuário a ser editado: "))
            existe = 0
            for registro in lista:
                if cod == registro[0]:
                    registro[0] = int(input("Digite o código: "))
                    registro[1] = str(input("Digite o nome: "))
                    registro[2] = int(input("Digite o CPF: "))
                    existe = 1
            if existe == 0:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Ação inválida. Tente novamente.")
    escrever_lista_em_json(lista, nome_arquivo)

# Função de listar todos os usuários cadastrados.

def listar():
    print()
    print("Operação Selecionada: === LISTAR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:
        print("Não há usuários cadastrados\n")
    else:
        for i in range(len(lista)):
            cadastro = lista[i]
            print("Código: ", cadastro[0])
            print("Nome: ", cadastro[1])
            print("CPF: ", cadastro[2], "\n")

# Função de excluir um usuário cadastrado.

def excluir():
    print()
    print("Operação Selecionada: === EXCLUIR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:  # Caso não haja itens na lista, executará este loop.
        print("Não há usuários cadastrados\n")
    else:
        try:
            cod = int(input("Informe o código do usuário a ser excluído: "))
            existe = 0
            for registro in lista:
                if cod == registro[0]:
                    lista.remove(registro)
                    print("O usuário foi excluído com sucesso.\n")
                    existe = 1
            if existe == 0:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Ação inválida. Tente novamente.")
    escrever_lista_em_json(lista,nome_arquivo)

# IMPORTANTE

nome_arquivo = 'lista_estudantes.json'
menu_atual = "1" # O valor "menu_atual" é utilizado para navegação entre os menus.

# MENU PRINCIPAL
# Loop inicial para apresentação do menu principal.
while menu_atual == "1":
    menu()
    proximo = input("Informe o menu desejado: ")
    if proximo == "0" or proximo.lower() == "sair":
        print("Encerrando aplicação. Até a próxima! =)")
        menu_atual = "0"

# Após a exibição do menu principal, executa os próximos laços dependendo da entrada do usuário.

    # ESTUDANTES

    elif proximo == "1" or proximo.lower() == "gerenciar estudantes":
        menu_atual = "2"
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
        while menu_atual == "4":
            print("---{PROFESSORES} Menu de Operações---")
            submenu()
    # TURMAS

    elif proximo == "4" or proximo.lower() == "gerenciar turmas":
        print("EM DESENVOLVIMENTO\n")

    # MATRÍCULAS

    elif proximo == "5" or proximo.lower() == "gerenciar matrículas":
        print("EM DESENVOLVIMENTO\n")

    else:
        print("Operação Selecionada: INVÁLIDA. Tente novamente\n")