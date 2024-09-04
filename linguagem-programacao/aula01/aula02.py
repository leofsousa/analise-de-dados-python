import time
#Estruturas condicionas:
# <  : Menor que 
# <= : Menor ou igual que
# >  : Maior que
# >= : Maior ou igual que
# == : Igual
# != : Diferente
# is : Identidade do objeto
# is not : Negação da identidade do objeto

# Operadores Relacionais: 
# and = E
# or = ou
# not = não

# Vendedor Automático de ingressos de cinema com verificador de faixa etária!

#Verificador de idade:
idade = int(input('Digite sua idade: '))
if idade < 12:
    print(f'Sua idade é {idade}, o filme permitido será o filme 1!')
elif idade >= 12 and idade < 18:
    print(f'Sua idade é {idade}, os filmes permitidos serão os filmes 1 e 2!')
else:
    print(f'Sua idade é {idade}, você poderá assistir qualquer um dos filmes. 1, 2 ou 3!')

#decisão do filme escolhido

decisao = str(input('Digite o número do filme escolhido:'))
print(f' O filme escolhido foi o filme {decisao}, vamos verificar se há ingressos disponíveis, um momento...')
print('Verificando, só mais um momento...')
time.sleep(10)


#Verifica disponibilidade de ingressos:

quantidade_ingressosf1 = 10
quantidade_ingressosf2 = 6
quantidade_ingressosf3 = 5
if decisao == 1:
    if quantidade_ingressosf1 > 0:
        print(f'Essa sessão tem {quantidade_ingressosf1} ingressos disponíveis, divirta-se!)')
    else:
        print(f'Sentimos muito, os ingressos para essa sessão estão esgotados')