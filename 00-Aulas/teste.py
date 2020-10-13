lista = []
id = 0

def cadastro_pessoa(nome, sobrenome, idade):
    cadastro = {}
    cadastro['id'] = id +1
    cadastro['nome'] = nome
    cadastro['sobrenome'] = sobrenome
    cadastro['idade'] = idade

    if idade < 18:
        print('ERRO. Idade menor que 18.')
    else:
        lista.append(cadastro)
        print('Seu id é {}'.format(id + 1))


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
cadastro_pessoa(nome, sobrenome, idade)
print(lista)