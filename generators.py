"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension...porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))


# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# getsizeof() -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(9876655))
print(getsizeof(True))


from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof((x * 10 for x in range(1000)))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension {list_comp} bytes')
print(f'Set Comprehension {set_comp} bytes')
print(f'Dictionary Comprehension {dic_comp} bytes')
print(f'Generator Expression {gen} bytes')
"""

# Eu posso iterar no Genarator Expression? Sim!

gen = (x * 10 for x in range(10))
print(gen)
print(type(gen))

for num in gen:
    print(num)

