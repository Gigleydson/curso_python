print('Bem vindo a nossa tela de cadastro \n')

opcao = int(input("Para continuar o cadastro digite '1' ou digite '2' para sair: "))

cadastro = []

if opcao == 1:
    print('')
    nome = input('Nome: ').title()
    sobrenome = input('Sobrenome: ').title()
    idade = int(input('Idade: '))
    cidade = input('Cidade: ').title()
    print('')
    print('Cadastro realizado com sucesso!\n')
    print('Confira se os dados abaixo estão corretos:\n')

    cadastro.extend([nome, sobrenome, idade, cidade])

    for dado in cadastro:
        print(dado)

else:
    print('')
    print('Você saiu da tela de cadastro!')