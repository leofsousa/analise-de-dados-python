#Definindo uma funcão chamada "Soma"

def soma( a, b):
    resultado = a + b
    return resultado

#função para ver se números são pares

def e_par(numero):
    if numero % 2 == 0:
        print(f'{numero} é um número par')
        return True
    else:
        print(f'{numero} é um número impar')
        return False
    
num = e_par(567)
print(num)