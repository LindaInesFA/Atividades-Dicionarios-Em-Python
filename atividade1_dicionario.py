"""1. Crie um script e nele adicione um dicionário que deverá receber nome e o
telefone de 10 pessoas. Após receber todos os dados, liste os dados
recebidos. Crie uma opção de busca pelo nome, se o nome for encontrado o
telefone será exibido.
"""
print("\n--------------------------------------------")
print(" >>>>>>>>>>  Aluna: Linda Inês  <<<<<<<<<<")
print("--------------------------------------------\n")

# Criando dicionario vazio
pessoas = {}

# Laço de repetição para pedir os dados na quantidade definida
for contador in range (10):

    # Solicitando dados ao usuário
    nome = input("\nInforme o nome: ").upper()
    telefone = input("Informe o telefone: ")

    # Armazenando os dados digitados pelo usuário dentro do dicionário
    pessoas[nome] = {
        "telefone": telefone
    }
# Listando as pessoas da lista
print("\n----------------------------------------\n")
print(">>>>>>>> PESSOAS CADASTRADAS <<<<<<<<")
print("\n----------------------------------------")
for nome, detalhes in pessoas.items():
    print(f"\nNome: {nome}")
    print(f"Telefone: {detalhes['telefone']}")
    print("----------------------------------------")

# Pesquisando itens no dicionário
pesquisar = input("\nDigite um nome para pesquisar: ").upper()

# Estabelecendo condição para o resultado da pesquisa
if pesquisar in pessoas:
    detalhes = pessoas[pesquisar]

    print("\n----------------------------------------\n")
    print(f"Telefone: {detalhes['telefone']}")
    print("\n----------------------------------------\n")

else:
    print("\n-------------------------------------------------------\n")
    print(f"\nA pessoa com o nome {pesquisar} não foi encontrada.")
    print("\n-------------------------------------------------------\n")



"""2. Crie um script e nele adicione um dicionário que deverá receber nome do
cliente de uma oficina de veículos, neste programa deverão ser registrados a
placa do veículo, a cor do veículo, marca do veículo e a data de entrada do
veículo na oficina. O programa deverá ser capaz de fazer o registro dos
veículos, fazer a listagem dos veículos e fazer a busca de um determinado
veículo tendo como critério de busca a placa do veículo. """

veiculos = {}

def avisoDeCadastroVazio():
    print("\n-----------------------------------------------")
    print("    >>>> NÃO EXISTEM VEÍCULOS CADASTRADOS <<<<")
    print("------------------------------------------------\n")

print("\n>>>>> CADASTRO DE CLIENTES DA OFICINA <<<<<")

# Usando o while para o programa rodar até que o usuário o interrompa
while (True):

    # solicitando dados ao usuário e mostrando as opçoes existentes.
    opcao = input(f"\n- Novo cadastro [1]  \n- Listar veículos[2]\n- Pesquisar[3]\n- Sair [4]\n \n- Digite a opção: ")

    # definindo o que acontece se a opção '1' for escolhida
    if opcao == "1":
        cliente = input("\nNome do Cliente: ").upper()
        placa = input ("Placa: ")
        cor = input("Cor: ").upper()
        marca = input("Marca: ").upper()
        dataEntrada = input("Data da entrada do veículo: ")

        # Inserindo dados no dicionário
        veiculos [placa] = {
            'cliente': cliente,
            'cor' : cor,
            'marca': marca,
            'dataEntrada': dataEntrada
        }

    # definindo o que acontece se a opção '2' for escolhida
    if opcao == "2":
        if len(veiculos) > 0:

            # Acessando informaçoes com o for e Listando os veículos cadastrados e seus dados
            print("\n>>>> VEÍCULOS CADASTRADOS <<<<")
            for placa, dados in veiculos.items():
                print("----------------------------------------")
                print(f"\n- PLACA: {placa}")
                print(f"- CLIENTE: {dados['cliente']}")
                print(f"- COR: {dados['cor']}")
                print(f"- MARCA: {dados['marca']}")
                print(f"- DATA DE ENTRADA: {dados['dataEntrada']}")
                print("----------------------------------------\n")
        else:
            avisoDeCadastroVazio()

    # definindo o que acontece se a opção '3' for escolhida
    if opcao == "3":
        if len(veiculos) > 0:
            # Acessando informações com o for e Pesquisando o veículo pelo número da placa
            pesquisar= input("\nInforme a placa para encontrar um veículo: ")
            for placa, dados in veiculos.items():

                if pesquisar == placa:
                    print("\n>>>>>>>>> RESULTADO DA PESQUISA <<<<<<<<<")
                    print("----------------------------------------")
                    print(f"\n- PLACA: {placa}")
                    print(f"- CLIENTE: {dados['cliente']}")
                    print(f"- COR: {dados['cor']}")
                    print(f"- MARCA: {dados['marca']}")
                    print(f"- DATA DE ENTRADA: {dados['dataEntrada']}")
                    print("------------------------------------------\n")
                else:
                    print("\n-------------------------------------------------------")
                    print(f">>>> Placa de número {pesquisar} não foi encontrada <<<<")
                    print("-------------------------------------------------------\n")
        else:
            avisoDeCadastroVazio()

    # definindo o que acontece se a opção '4' for escolhida
    if opcao == "4":
        print("\n--------------------------")
        print("   >>>>> ENCERRADO <<<<<")
        print("--------------------------\n")
        break


"""3. Crie um script e nele adicione um dicionário que deverá receber nome e notas
de 5 alunos, cada aluno deve receber 4 notas. Após receber todos os dados,
liste separadamente os dados dos alunos aprovados e reprovados. Um aluno
é aprovado com a somatória das notas >= a 60 pontos, apresente também a
somatória das notas de cada aluno.
"""

# Criando dicionários vazios para armazenar dados
alunos = {}
aprovados = {}
reprovados = {}

# inicializando a variável soma
soma = 0

# função para acessar e mostrar dados do dicionário
def mostrarDados(dicionario,titulo):
    tamanho = len(dicionario)

    if (tamanho > 0):

        print(f"\n>>>>>>>> ALUNOS {titulo} <<<<<<<<")
        for nome, detalhes in dicionario.items():
            # desestruturando o conteúdo de detalhes
            nota1,nota2,nota3,nota4 = detalhes['notas']

            print(f"\nNome: {nome}")
            print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
            print(f"Soma: {detalhes['somaNotas']}")
            print("---------------------------------")
        print("\n==================================\n")
    else:
        print("\n--------------------------------------------")
        print(f"\n>>> NENHUM ALUNO NA LISTA DE {titulo} <<<")
        print("\n--------------------------------------------")

# Usando o for para repetir 5 vezes a solicitação ao usuário
for contador in range (5):
    notaAluno = []

    # Solicitando dados ao usuário
    nome = input("\nInforme o nome do aluno(a): ")

    # Usando o for para conseguir socilitar as quatro notas para cada aluno
    for contador2 in range (4):

        nota = float(input(f"Informe a {contador2+1}º nota: "))

        # Adicionando as notas em uma lista
        notaAluno.append(nota)

        # Armazenando os dados digitados pelo usuário dentro do dicionário
        alunos[nome] = {
            "notas": notaAluno
        }
# usando o for para acessar os itens do dicionário
for nome, detalhes in alunos.items():

    # inserindo a soma das notas em uma variável
    soma = sum(detalhes['notas'])

    # Inserindo 'soma' no dicionario alunos
    alunos[nome] = {
        "soma": soma
    }
    # fazendo verificação para preencher os dicionarios 'aprovados' e 'reprovados""
    if (soma >=  60):
        aprovados[nome] = {
            "notas": detalhes['notas'],
            "somaNotas" : soma,
        }
    else:
        reprovados[nome] = {
            "notas": detalhes['notas'],
            "somaNotas" : soma,
        }
# Utilizando a função 'mostrarDados'
mostrarDados(aprovados, "APROVADOS")

mostrarDados(reprovados, "REPROVADOS")



"""4. Crie um script e nele adicione um dicionário que deverá receber nome e notas
de “n” alunos, cada aluno deve receber 4 notas. O programa criado deverá
apresentar as seguintes características/funcionalidades:

a. Receber os dados de um aluno por vez;

b. Exibir os dados dos alunos de uma só vez(indicando a somatória das notas de
cada aluno);

c. Exibir a lista dos alunos aprovados e reprovados(só os nomes e a indicação de
aprovado e reprovado - se possível duas opções, uma para aprovados e outra
para reprovados);

d. Exibir um menu com as opções existentes no programa"""


turmaInformatica = {}
soma = 0

print(">>> CADASTRO DE ALUNOS DA TURMA DE INFORMÁTICA <<<")

while(True):

    print("\n  >>>>>>> <  MENU  > <<<<<<<  \n")
    print("- Cadastrar um aluno(a)          [1]")
    print("- Exibir dados dos alunos        [2]")
    print("- Exibir alunos Aprovados        [3]")
    print("- Exibir alunos Reprovados       [4]")
    print("- Sair                           [5]")
    print("\n==================================\n")

    opcao = input("\nDigite a opção escolhida: ")
    notas = []

    if opcao == "1":
        nome = input("\nNome do aluno: ")

        for contador in range (4):
            nota = float(input(f"Informe a {contador+1}º nota: "))
            notas.append(nota)

        turmaInformatica[nome] = {
            "notas" : notas
        }

    if opcao == "2":
            print("\n--------------------------------------------")
            print("\n>>>>>>>> ALUNOS CADASTRADOS <<<<<<<<")
            print("\n--------------------------------------------")
            tamanho = len(turmaInformatica)

            if (tamanho > 0):

                # Utilizando o for para acessar o conteúdo do dicionario
                for nome, dados in turmaInformatica.items():

                    # desestruturando o conteúdo de dados
                    nota1,nota2,nota3,nota4 = dados['notas']

                    print(f"\nAluno(a): {nome}".upper())
                    print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
                    print(f"Soma: {sum(dados['notas'])}")
            else:
                    print("\n--------------------------------------------")
                    print("\n           >>>>> Vazio <<<<<")
                    print("\n--------------------------------------------")

    if opcao == "3":
                print("\n--------------------------------------------")
                print("\n>>>>>>>> ALUNOS APROVADOS <<<<<<<<")
                print("\n--------------------------------------------")
                # Utilizando o for para acessar o conteúdo do dicionario
                for nome, dados in turmaInformatica.items():
                    soma = sum(dados['notas'])
                    if soma >= 60:
                        print(f"- {nome}".upper())
    if opcao == "4":
            print("\n--------------------------------------------")
            print("\n>>>>>>>> ALUNOS REPROVADOS <<<<<<<<")
            print("\n--------------------------------------------")
            # Utilizando o for para acessar o conteúdo do dicionario
            for nome, dados in turmaInformatica.items():
                soma = sum(dados['notas'])
                if soma < 60:
                    print(f"- {nome}".upper())

    if opcao == "5":
        print("\n--------------------------------------------")
        print("\n        >>>> CADASTRO ENCERRADO <<<<")
        print("\n--------------------------------------------")
        break
