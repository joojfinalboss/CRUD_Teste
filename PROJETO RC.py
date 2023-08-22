# NOME: João Vitor Ferreira Antunes de Lima
# CURSO: Tecnologia em Análise e Desenvolvimento de Sistemas

# IMPORTANTE


menu_atual = "1" # O valor "menu_atual" é utilizado para navegação entre os menus.
lista_estudantes = []

# MENU PRINCIPAL
# Loop inicial para apresentação do menu principal.
while menu_atual == "1":
    print("-----MENU PRINCIPAL-----")
    print("1. Gerenciar Estudantes")
    print("2. Gerenciar Disciplinas")
    print("3. Gerenciar Professores")
    print("4. Gerenciar Turmas")
    print("5. Gerenciar Matrículas")
    print("0. Sair")
    proximo = input("Informe o menu desejado: ")        # O sistema recebe o valor de "proximo", que irá determinar qual será o próximo loop a ser rodado.
    if proximo == "0" or proximo.lower() == "sair":             # Caso a opção de sair seja selecionada, "menu_atual" recebe o valor de 0 para impedir que o loop do menu principal seja executado novamente, e o programa encerra.
        print("Encerrando aplicação. Até a próxima! =)")
        menu_atual = "0"

    # ESTUDANTES

    elif proximo == "1" or proximo.lower() == "gerenciar estudantes":
        menu_atual = "2"
        while menu_atual == "2":
            print("---{ESTUDANTES} Menu de Operações---")
            print()
            print("1. Incluir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Menu Principal")
            funcao = input("Informe a operação desejada: ")  # "funcao" recebe um valor que determina qual será o próximo loop a ser executado.
            if funcao == "1" or funcao.lower() == "incluir":
                print()
                print("Operação Selecionada: === INCLUIR ===")
                try:
                    cod = int(input("Digite o código do estudante: "))
                    nome = str(input("Digite o nome do estudante: "))
                    cpf = int(input("Digite o CPF do estudante: "))
                    cadastro = [cod, nome, cpf]
                    lista_estudantes.append(cadastro)
                    print("Estudante cadastrado com sucesso.\n")  # Após isso, o loop do menu de operações é executado novamente.
                except ValueError:
                    print("Ação inválida. Tente novamente.")

            elif funcao == "2" or funcao.lower() == "listar":
                print()
                print("Operação Selecionada: === LISTAR ===")
                if len(lista_estudantes) == 0:  # Caso não haja itens na lista, executará este loop.
                    print("Não há estudantes cadastrados\n")
                else:
                    for i in range(
                            len(lista_estudantes)):  # Este loop exibirá cada item armazenado em "lista_estudantes", e será executado de acordo com quantos itens existem nesta lista.
                        cadastro = lista_estudantes[i]
                        print("Código: ", cadastro[0])
                        print("Nome: ", cadastro[1])
                        print("CPF: ", cadastro[2], "\n")

            # Caso selecionem atualizar ou excluir, retornará uma mensagem.

            elif funcao == "3" or funcao.lower() == "atualizar":
                print()
                print("Operação Selecionada: === ATUALIZAR ===")
                if len(lista_estudantes) == 0:  # Caso não haja itens na lista, executará este loop.
                    print("Não há estudantes cadastrados\n")
                else:
                    try:
                        cod = int(input("Informe o código do aluno a ser editado: "))
                        for registro in lista_estudantes:
                            if cod == registro[0]:
                                registro[0] = int(input("Digite o código do estudante: "))
                                registro[1] = str(input("Digite o nome do estudante: "))
                                registro[2] = int(input("Digite o CPF do estudante: "))
                            else:
                                print("Código inválido. Tente novamente.")
                    except ValueError:
                        print("Ação inválida. Tente novamente.")
            elif funcao == "4" or funcao.lower() == "excluir":
                print()
                print("Operação Selecionada: === EXCLUIR ===")
                if len(lista_estudantes) == 0:  # Caso não haja itens na lista, executará este loop.
                    print("Não há estudantes cadastrados\n")
                else:
                    try:
                        cod = int(input("Informe o código do aluno a ser excluído: "))
                        for registro in lista_estudantes:
                            if cod == registro[0]:
                                lista_estudantes.remove(registro)
                                print("O cadastro do estudante foi excluído com sucesso.\n")
                            else:
                                print("Código inválido. Tente novamente.")
                    except ValueError:
                        print("Ação inválida. Tente novamente.")

            # Caso selecionem o menu principal, "menu_atual" receberá o valor 1, que forçará a execução do loop do menu principal.
            elif funcao == "0" or funcao.lower() == "menu principal":
                menu_atual = "1"
            # Caso o que o usuário digite não seja válido, exibirá uma mensagem.
            else:
                print()
                print("Operação Selecionada: INVÁLIDA. Tente novamente\n")


    # Os próximos loops apresentam uma mensagem caso o usuário selecione outras opções além de GERENCIAR ESTUDANTES no MENU PRINCIPAL.

    # DISCIPLINAS

    elif proximo == "2" or proximo.lower() == "gerenciar disciplinas":
        print("EM DESENVOLVIMENTO\n")

    # PROFESSORES

    elif proximo == "3" or proximo.lower() == "gerenciar professores":
        print("EM DESENVOLVIMENTO\n")

    # TURMAS

    elif proximo == "4" or proximo.lower() == "gerenciar turmas":
        print("EM DESENVOLVIMENTO\n")

    # MATRÍCULAS

    elif proximo == "5" or proximo.lower() == "gerenciar matrículas":
        print("EM DESENVOLVIMENTO\n")

    else:
        print("Operação Selecionada: INVÁLIDA. Tente novamente\n")