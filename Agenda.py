AGENDA = {}
#AGENDA['rodrigo'] = {'telefone': '21882823',
 #                 'email': 'rodrigo@gmail.com',
  #               'endereco': 'Av rondon', }
def mostrar_contatos(): #Função para mostrar a agenda todos os contatos
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print("---------------------------------------")
    else:
        print('>>>>>>Agenda vazia......')

def buscar_contato(contato):
    try:
        print("Nome:",contato)
        print("Telefone:",AGENDA[contato]["telefone"])
        print("Email:",AGENDA[contato]["email"])
        print("Endereço:",AGENDA[contato]["endereco"])
    except KeyError:
        print('>>>>Contado Invalido....')
    except Exception as error:
        print('>>>>Erro inesperado.....')

def ler_detalhes_contato():
    telefone = input("Digite o número de telefone:...")
    email = input("Digite o email:...")
    endereco = input ("Digite o endereço:...")
    return telefone,email,endereco

def incluir_editar_contato(contato,telefone,email,endereco):
    AGENDA[contato] = {
      "telefone": telefone,
      "email": email,
      "endereco": endereco,
    }
    salvar()
    print(">>>>>> Contato {} adicionado".format(contato))
    print("--------------------")


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(">>>>>>> contato {} excluido com sucesso".format(contato))
        print("--------------------")
    except KeyError:
        print(">>>>>Contato Invalido...")
    except Exception as error:
        print(">>>>>Erro inesperado....")

def exportar_contatos(filename):
    try:
        with open(filename,'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
                print(">>>>>Agenda exportada com sucesso!!!")
    except Exception as error:
        print(">>>>Ocorreu um erro na operação...")
        print(error)

def importar_contatos(filename):
    try:
        with open(filename,'r') as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome,telefone,email,endereco)
    except FileNotFoundError:
        print(">>>Arquivo nao encontrado...")
    except Exception as error:
        print(">>>Erro na importação")
        print(error)

def salvar():
    exportar_contatos('database.csv')

def load():
    try:
        with open('database.csv', 'r') as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco,
                }
        print('>>> Database carregado com sucesso')
        print('>>> {} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print(">>>Arquivo nao encontrado...")
    except Exception as error:
        print(">>>Erro na importação")
        print(error)


def imprimir_menu():
    print("==================================")
    print("1- Mostrar contatos")
    print("2- Buscar contato")
    print("3- Incluir contato")
    print("4- editar contato")
    print("5- Excluir contato")
    print("6- Exportar Agenda para CSV")
    print("7- Importar Agenda CSV")
    print("0- Fechar agenda")
    print("==================================")

#Inicio do progama
load()
while True:
    imprimir_menu()

    opcao = input("Escolha uma opção: ") #Variavel que é uma string
    if opcao == "1": #colocar todos os numeros entre parentese porque a variavel é uma string...
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato:...")
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Digite o nome do contato:...")
        try:
            AGENDA[contato]
            print(">>>Contato já existente.")
        except KeyError:
            telefone,email,endereco = ler_detalhes_contato()
            incluir_editar_contato(contato,telefone,email,endereco)
    elif opcao == "4":
        contato = input("Digite o Nome do contato:")
        try:
            AGENDA[contato]
            print('>>>Editanto o contato',contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print(">>>>Contato Inexistente ")
    elif opcao == "5":
        contato = input("Digite o nome do contato para exclui-lo:")
        excluir_contato(contato)
    elif opcao == "6":
        filename = input("Digite o nome do arquivo para ser exportado:...")
        exportar_contatos(filename)
    elif opcao == "7":
        filename = input("Digite o nome do arquivo para ser importado:...")
        importar_contatos(filename)
    elif opcao == "0":
         print("Fechando progama...")
         break
    else:
        print("Operação inválida")
        break

