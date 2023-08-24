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


# Função para exibir os menus secundários.
def submenu():
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Menu Principal")

# Existe um arquivo JSON para cada categoria (estudante, disciplinas, professores, turmas, matrículas).
# A variável "nome_arquivo" irá receber o arquivo de acordo com a categoria selecionada.

# Função de cadastrar um usuário.
# Dependendo de qual arquivo JSON ela recebeu, um determinado loop será executado solicitando dados ao usuário.
# Em todos os loops, é validado se o código inserido já existe.
# Caso a entrada de dados seja inválida, exibirá mensagem de erro.
# No início, o arquivo JSON é aberto para leitura. No final, é escrito o conteúdo de "lista" nele e encerrado.

def incluir(nome_arquivo):
    print()
    print("Operação Selecionada: === INCLUIR ===")
    lista = ler_lista_do_json(nome_arquivo)
    try:
        lista = ler_lista_do_json(nome_arquivo)
        if nome_arquivo == 'lista_estudantes.json' or nome_arquivo == 'lista_professores.json':
            cod = int(input("Digite o código: "))
            nome = str(input("Digite o nome: "))
            cpf = int(input("Digite o CPF: "))
            cadastro = [cod, nome, cpf]
            existe = validar(lista, cod)
        elif nome_arquivo == 'lista_disciplinas.json':
            cod = int(input("Digite o código:"))
            nome = str(input("Digite o nome: "))
            cadastro = [cod, nome]
            existe = validar(lista, cod)
        elif nome_arquivo == 'lista_turmas.json':
            cod = int(input("Digite o código da turma:"))
            cod_prof = int(input("Digite o código do professor:"))
            cod_disc = int(input("Digite o código da disciplina:"))
            cadastro = [cod, cod_prof, cod_disc]
            existe = validar(lista, cod)
        elif nome_arquivo == 'lista_matriculas.json':
            cod = int(input("Digite o código da matrícula:"))
            cod_turma = int(input("Digite o código da turma:"))
            cod_estudante = int(input("Digite o código do estudante:"))
            cadastro = [cod, cod_turma, cod_estudante]
            existe = validar(lista, cadastro)
        if existe == 0:
            print("Cadastro efetuado com sucesso.\n")
            lista.append(cadastro)
        escrever_lista_em_json(lista, nome_arquivo)
    except ValueError:
        print("Ação inválida. Tente novamente.")

# Função de editar as informações de um usuário cadastrado.
# Esta função atribui o conteúdo de um arquivo JSON a uma variável, verifica se há algum elemento e prossegue.
# Solicita código ao usuário e caso não exista exibe erro.
# Se existir irá solicitar ao usuário os novos dados para atualização, e então salvar no arquivo JSON.

def atualizar():
    print()
    print("Operação Selecionada: === ATUALIZAR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:
        print("Não há cadastros. \n")
    else:
        try:
            cod = int(input("Informe o código: "))
            existe = 0
            for registro in lista:
                if cod == registro[0]:
                    if nome_arquivo == 'lista_estudantes.json' or nome_arquivo == 'lista_professores.json':
                        registro[0] = int(input("Digite o novo código: "))
                        registro[1] = str(input("Digite o novo nome: "))
                        registro[2] = int(input("Digite o novo CPF: "))
                    elif nome_arquivo == 'lista_disciplinas.json':
                        registro[0] = int(input("Digite o novo código:"))
                        registro[1] = str(input("Digite o novo nome: "))
                    elif nome_arquivo == 'lista_turmas.json':
                        registro[0] = int(input("Digite o novo código da turma:"))
                        registro[1] = int(input("Digite o novo código do professor:"))
                        registro[2] = int(input("Digite o novo código da disciplina:"))
                    elif nome_arquivo == 'lista_matriculas.json':
                        registro[0] = int(input("Digite o novo código da matrícula"))
                        registro[1] = int(input("Digite o novo código da turma:"))
                        registro[2] = int(input("Digite o novo código do estudante:"))
                    existe = 1
                    print("Cadastro atualizado com sucesso. \n")
            if existe == 0:
                print("Código inválido. Tente novamente.")

            escrever_lista_em_json(lista, nome_arquivo)
        except ValueError:
            print("Ação inválida. Tente novamente.")


# Função de listar todos os usuários cadastrados.
# Atribui o conteúdo de um arquivo JSON a uma variável, verifica se há algum elemento nela e prossegue.
# Caso haja elementos, exibe os dados cadastrais de acordo com o arquivo JSON utilizado.

def listar():
    print()
    print("Operação Selecionada: === LISTAR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:
        print("Não há cadastros. \n")
    else:
        for i in range(len(lista)):
            cadastro = lista[i]
            if nome_arquivo == 'lista_estudantes.json':
                print("Código: ", cadastro[0])
                print("Nome: ", cadastro[1])
                print("CPF: ", cadastro[2], "\n")
            elif nome_arquivo == 'lista_disciplinas.json':
                print("Código da Disciplina: ", cadastro[0])
                print("Nome da Disciplina: ", cadastro[1], "\n")
            elif nome_arquivo == 'lista_professores.json':
                print("Código: ", cadastro[0])
                print("Nome: ", cadastro[1])
                print("CPF: ", cadastro[2], "\n")
            elif nome_arquivo == 'lista_turmas.json':
                print("Código da Turma: ", cadastro[0])
                print("Código do Professor: ", cadastro[1])
                print("Código da Disciplina: ", cadastro[2], "\n")
            elif nome_arquivo == 'lista_matriculas.json':
                print("Código da Matrícula: ", cadastro[0])
                print("Código da Turma: ", cadastro[1])
                print("Código do Estudante: ", cadastro[2])

# Função de excluir um usuário cadastrado.
# Solicita código ao usuário, compara com a lista que está sendo lida e caso exista, exclui o cadastro.

def excluir():
    print()
    print("Operação Selecionada: === EXCLUIR ===")
    lista = ler_lista_do_json(nome_arquivo)
    if len(lista) == 0:  # Caso não haja itens na lista, executará este loop.
        print("Não há cadastros. \n")
    else:
        try:
            cod = int(input("Informe o código do cadastro a ser excluído: "))
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

# Função de validação
# Esta função procura no primeiro elemento de cada lista dentro de outra lista, e caso exista, exibe aviso.
# Caso não exista, retorna o valor original de "existe", que é utilizado em outras funções como condicional.
def validar(lista,cod):
    existe = 0
    for registro in lista:
        if cod == registro[0]:
            print("Código já cadastrado.")
            existe = 1
    return existe

# Esta função recebe o valor da variável "funcao" e executa outras funções de acordo com o valor recebido.
# Ela é utilizada para todas as categorias.

def operacoes(funcao):
    if funcao == "1" or funcao.lower() == "incluir":
        incluir(nome_arquivo)
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

# IMPORTANTE

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
# Cada laço irá definir um arquivo JSON de acordo com a categoria correspondente, assim dividindo os dados
# cadastrais em 5 arquivos diferentes que serão chamados por outras funções neste mesmo laço.

    # ESTUDANTES

    elif proximo == "1" or proximo.lower() == "gerenciar estudantes":
        nome_arquivo = 'lista_estudantes.json'
        menu_atual = "2"
        while menu_atual == "2":
            print("---{ESTUDANTES} Menu de Operações---")
            submenu()
            funcao = input("Informe a operação desejada: ")
            operacoes(funcao)


    # DISCIPLINAS

    elif proximo == "2" or proximo.lower() == "gerenciar disciplinas":
        nome_arquivo = 'lista_disciplinas.json'
        menu_atual = "2"
        while menu_atual == "2":
            print("---{DISCIPLINAS} Menu de Operações---")
            submenu()
            funcao = input("Informe a operação desejada: ")
            operacoes(funcao)


    # PROFESSORES

    elif proximo == "3" or proximo.lower() == "gerenciar professores":
        nome_arquivo = 'lista_professores.json'
        menu_atual = "2"
        while menu_atual == ("2"):
            print("---{PROFESSORES} Menu de Operações---")
            submenu()
            funcao = input("Informe a operação desejada: ")
            operacoes(funcao)

    # TURMAS

    elif proximo == "4" or proximo.lower() == "gerenciar turmas":
        nome_arquivo = 'lista_turmas.json'
        menu_atual = "2"
        while menu_atual == "2":
            print("---{TURMAS} Menu de Operações---")
            submenu()
            funcao = input("Informe a operação desejada: ")
            operacoes(funcao)

    # MATRÍCULAS

    elif proximo == "5" or proximo.lower() == "gerenciar matrículas":
        nome_arquivo = 'lista_matriculas.json'
        menu_atual = "2"
        while menu_atual == "2":
            print("---{MATRÍCULAS} Menu de Operações---")
            submenu()
            funcao = input("Informe a operação desejada: ")
            operacoes(funcao)