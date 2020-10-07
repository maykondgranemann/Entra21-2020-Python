#===== Dicionarios 
#OBS: CRUD - Create, Read, Update, Delete

#=== declaração vazio
dicionario_pessoa1 = {}

#=== declaração com chave/valor
dicionario_pessoa2 = { 'nome':'Arthur' }

#=== adicionando chave após criação do dicionário
dicionario_pessoa1['nome']= 'Helion'
dicionario_pessoa1['idade'] = 32

dicionario_pessoa2['idade'] = 27
dicionario_pessoa2['rua'] = 'rua....'
dicionario_pessoa2['bairro'] = 'centro....'

#=== alterando o valor de uma chave
dicionario_pessoa2['idade'] = 17

#=== removendo uma chave do dicionário
del dicionario_pessoa2['rua']
bairro = dicionario_pessoa2.pop('bairro')

#=== Lendo dados do dicionário, chave a chave
print(dicionario_pessoa1['nome'], dicionario_pessoa1['idade'])

#=== lendo dados de forma dinamica 
conjunto_chave_valor = dicionario_pessoa2.items()
for chave,valor in conjunto_chave_valor: 
    print(chave, ' - ', valor)


#=== lendo dados de forma dinamica e alterando uma chave especifica
for chave,valor in dicionario_pessoa2.items(): 
    if chave == 'idade' and valor < 18:
        dicionario_pessoa2['idade'] = 18

print(dicionario_pessoa2)
