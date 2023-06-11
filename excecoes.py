# class MeuErro(Exception):
#     ...
# def levantar():
#     exception_ = MeuErro('a', 'b', 'c' , 'd')
#     raise exception_
#
# try:
#     levantar()
# except MeuErro as error:
#     print(error)



class Pessoa:
    codi = 1
    nome = 'joaquim'
    altura = 2
    peso = 3
    idade = 10
    escolaridade = 'formado'


    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, fruta):
        return f'{self.nome} está comando {fruta}'


    def crescer(self, centimetros):

        return altura + centimetros

    def formar(self, titulo):
        self.titulo = titulo

    def velho(self, anos):
        if anos > 0:
            idade += anos


tes = Pessoa(nome='Joaquim2')


print(tes.nome)



