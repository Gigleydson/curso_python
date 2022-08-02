print('')
print('Calculadora em Python\n')

num1 = float(input('Digite o primeiro número: '))
op = input('Escolha a operação: ')
num2 = float(input('Digite o segundo número: '))

if op == '+':
    print(f'O resultado da operação é {num1 + num2}')
elif op == '-':
    print(f'O resultado da operação é {num1 - num2}')
elif op == '*':
    print(f'O resultado da operação é {num1 * num2}')
elif op == '/':
    print(f'O resultado da operação é {num1 / num2}')
else:
    print('Operação inválida!')
