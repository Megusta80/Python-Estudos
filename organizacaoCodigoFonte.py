# Importações
import math

# Definição de funções
def dobro(x):
    return 2 * x

def saudacao(nome):
    print(f'Bem-vindo {nome}!')

# Código principal
nome = input('Qual o seu nome? ')
saudacao(nome)
dobro_pi = dobro(math.pi)
print(f'O dobro de {math.pi:.4f} é {dobro_pi:.4f}')
