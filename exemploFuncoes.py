def soma(n1, n2):
    print('Início do bloco da função')
    s = n1 + n2
    return s
soma(3,5)
soma(7,-9)
print('Fora da função')

def media(a,b,c):
    m =(a + b + c)/3
    return m

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
