#Define uma classe chamada pessoa
class Pessoa:
    #o método __init__ é um construtor, chamado quando um objeto de classe é criado.
    def __init__(self, nome, idade, genero):
        #self é uma convenção de python que se refere à própria instância da classe.
        #Os parâmetros nome, idade e gênero são passado durante a criação do objeto.
        #Eles são usado para inicializar os atributos da instância.
        self.nome = nome # Atribui o valor de nome ao atributo nome da instância.
        self.idade = idade #atribui o valor idade ao atributo idade da instância.
        self.genero = genero #Atribui o valor de genero ao atributo genero da instância
    # O Método Cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    def aniversário(self):
        self.idade += 1
pessoa1 = Pessoa("Leonardo", 26, "Masculino")
print(pessoa1.cumprimentar())
print(f'Idade: {pessoa1.idade}')
pessoa1.aniversário()
print(f'Idade após aniversário: {pessoa1.idade}')
