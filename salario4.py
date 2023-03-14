qtd = int(input('Quantidade de funcionários: '))
salarios = qtd*[0]
soma = 0
i = 0 # variável que será usada como índice.

while i < qtd:
    salarios[i] = float(input('Salário: R$ '))
    soma += salarios[i]
    i += 1
    
media = soma / qtd
print(f'Média = R$ {media:.2f}')

i = 0 # variável que será usada como índice.
while i < qtd:
    if salarios[i] < media:
        print(f'Abaixo da média: R$ {salarios[i]:.2f}')
    i += 1
