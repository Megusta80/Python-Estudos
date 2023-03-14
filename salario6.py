def preenche(qtd):
    salarios = []
    for _ in range(qtd):
        salario = float(input('Salário: R$ '))
        salarios.append(salario)
    return salarios

def soma_salarios(salarios):
    soma = 0
    for salario in salarios:
        soma += salario
    return soma

def abaixo_media(salarios, media):
    for salario in salarios:
        if salario < media:
            print(f'Abaixo: R$ {salario:.2f}')

qtd = int(input('Quantidade: '))
salarios = preenche(qtd)
soma = soma_salarios(salarios)

media = soma /len(salarios)
print(f'Média: R$ {media:.2f}')
abaixo_media(salarios, media)

