# Conjunto SET
meu_conjunto = set()
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
print(f'Conjunto após adicionar elementos: ' , meu_conjunto)

# Verificando elementos dentro do conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f'{elemento} está no meu conjunto!')
else:
    print(f'{elemento} não está no meu conjunto!')

meu_conjunto.remove(elemento)
print(f'Meu conjunto após remover o elemento {elemento}: ' , meu_conjunto)