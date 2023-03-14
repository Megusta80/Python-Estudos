salarios = []
soma = 0

for _ in range(4):
    salario = float(input('Salário: R$ '))
    soma += salario
    salarios.append(salario)
    #append é anexo, no sentido de adicionar algo

media = soma / 4
print(f'Média = R$ {media:.2f}')

for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R$ {salario:.2f}')
        
