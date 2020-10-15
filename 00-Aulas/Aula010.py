#==== Agil 1 - Cerimonia
#--- Daily - 15min realiza em pé
# - O que fiz no ultimo dia
# - O que (estou fazendo / farei) hoje
# - Existe algum impedimento para que eu execute a 
#      minha terefa hoje?

#==== Dicionarios - Merge

pessoa1 = {'id':1, 'nome':'maykon', 'sobrenome':'granemann','idade':18}
end1 = {'id_pessoa':1, 'rua':'Rua 1', 'numero':18, 'complemento':'sem', 'bairro':'Reino das Itoupavas', 'cidade':'Bnu','estado':'SC'}

pessoa1.update(end1)
print(pessoa1)

# Join - Uniao
# pessoa_end = pessoa1.copy()
# pessoa_end.update(end1)
# print(pessoa_end)

# join 2 - Uniao
# pessoa_end = { **pessoa1, **end1 }
# print(pessoa_end)
