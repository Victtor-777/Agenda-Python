from time import sleep

#Totas as Funções do Programa: (Poderia posteriormente ser utilizado módulos nessa parte das funções e só deixar o programa principal aqui)

#Verifica se o valor digitado no menu é válido:
def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('VALOR INVÁLIDO! Digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('O usuário preferiu não inserir os dados.')
            return 0
        else:
            return valor


#Faz um linha para funções visuais do programa
def linha(tam=70):
    return '='*tam


#Faz um "mini menu" para funções visuais do programa
def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())


#Função que faz o Menu Principal do Programa
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Escolha uma opção: ')
    return opc


#Função que faz um "Relatório" Lista, de todas as pessoas cadastradas no programa.
def mostrar_contatos(agenda):
    print("{:<4s} {:<12s} {:<22s} {:<15s} {:<15s}".format("Nro", "Nome", "E-mail", "Twitter", "Instagram"))
    for i, contato in enumerate(agenda, start=1):
        nome = contato.get('Nome', '')
        email = contato.get('e-mail', '')
        twitter = contato.get('Twitter', '')
        instagram = contato.get('Instagram', '')
        print("{:<4d} {:<12s} {:<22s} {:<15s} {:<15s}".format(i, nome, email, twitter, instagram))


#Função que faz o cadastro das pessoas no programa, cadastra quantas pessoas o usuário quiser até que ele deseje parar.
def cadastrar_contato():
    while True:
        contato = {}
        contato['Nome'] = input('Nome: ').strip()
        contato['Telefone'] = input('Telefone: ').strip()
        contato['e-mail'] = input('E-mail: ').strip()
        contato['Twitter'] = input('Twitter: ').strip()
        contato['Instagram'] = input('Instagram: ').strip()
        print(f'Novo contato {contato["Nome"]} adicionado com sucesso!')
        agenda.append(contato)
        resposta = ''
        while resposta != 'S' and resposta != 'N':
            resposta = input('Deseja cadastrar uma nova pessoa [S] ou [N] ? ').strip().upper()
        if resposta == 'N':
            break


#Função que mostra pelo nome os todos dados de uma pessoa específica cadastrada na agenda.
def consultar_contato(agenda, nome):
    encontrado = False
    for contato in agenda:
        if contato['Nome'] == nome:
            print(', '.join(contato.values()))
            encontrado = True
            break
    if not encontrado:
        print("Contato não encontrado.")


#Função que altera todos os dados de uma pessoa já cadastrada na agenda do programa.
def alterar_contato(agenda, nome):
    encontrado = False
    for contato in agenda:
        if contato['Nome'] == nome:            
            print(f"Digite os novos dados do contato {contato['Nome']}")
            novo_nome = input('Novo Nome: ')
            novo_telefone = input('Novo Telefone: ')
            novo_email = input('Novo E-mail: ')
            novo_twitter = input('Novo Twitter: ')
            novo_instagram = input('Novo Instagram: ')

            contato['Nome'] = novo_nome
            contato['Telefone'] = novo_telefone
            contato['e-mail'] = novo_email
            contato['Twitter'] = novo_twitter
            contato['Instagram'] = novo_instagram

            print(f"Dados de {contato['Nome']} atualizados com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print('Contato não encontrado')


#Função que romove, todos os dados, de uma pessoa do programa.
def remover_contato(agenda, nome):
    encontrado = False
    for contato in agenda:
        if contato['Nome'] == nome:
            agenda.remove(contato)
            print(f'Contato {nome} removido')
            encontrado = True
            break
    if not encontrado:
        print('Contato não encontrado.')



#--------------- PROGRAMA PRINCIPAL ---------------

cabecalho('Agenda Telefonica')

agenda = []

while True:
    #Gerando o menu do programa pela função menu(), com as opções dele.
    resposta = menu(['Ver Lista de Contatos', 'Adicionar Novo Contato', 'Consultar Dados de um Contato', 'Alterar Dados de um Contato', 'Remover um Contato','Sair do Programa'])
    if resposta == 1:
        #Opção de listar todos os contatos da agenda.
        cabecalho('Lista de Contatos')
        mostrar_contatos(agenda)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa, pode-se cadastrar quantas pessoas o usuário desejar.
        cabecalho('Novo Contato')
        cadastrar_contato()
    elif resposta == 3:
    # Opção de consultar dados de apenas um contato específico, pelo seu nome.
        cabecalho('Consultar Dados')
        nome_consulta = input('Digite o nome do contato que deseja consultar: ').strip()
        consultar_contato(agenda, nome_consulta)
    elif resposta == 4:
        #Opção de alterar os dados de um contato.
        cabecalho('Alterar Dados')
        novos_dados = input('Digite o nome do contato que deseja alterar os dados: ').strip()
        alterar_contato(agenda, novos_dados)
    elif resposta == 5:
        #Opção de remover um contato da agenda.
        cabecalho('Remover Contato')
        nome = input('Digite o nome do contato que será removido: ').strip()
        remover_contato(agenda, nome)
    elif resposta == 6:
        #Opção de finalizar o programa.
        cabecalho('Saindo do Programa...')
        break
    else:
        #Opção caso o usuário digite uma opção errada ou inválida no menu.
        print('OPÇÃO INVÁLIDA! Digite um opção válida.')
    sleep(2)


sleep(1)
print(f'{" FIM ":=^70}')
