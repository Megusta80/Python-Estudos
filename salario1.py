soma = 0

salario_0 = float(input('Salário: R$ '))
soma += salario_0

salario_1 = float(input('Salário: R$ '))
soma += salario_1

salario_2 = float(input('Salário: R$ '))
soma += salario_2

salario_3 = float(input('Salário: R$ '))
soma += salario_3

media = soma / 4
print(f'Média = R$ {media:.2f}')

if salario_0 < media:
    print(f'Abaixo da média: R$ {salario_0:.2f}')
if salario_1 < media:
    print(f'Abaixo da média: R$ {salario_1:.2f}')
if salario_2 < media:
    print(f'Abaixo da média: R$ {salario_2:.2f}')
if salario_3 < media:
    print(f'Abaixo da média: R$ {salario_3:.2f}')
