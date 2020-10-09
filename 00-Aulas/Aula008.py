#==== Dicionários e funções - Parte 2

#--- Dicionários
#conjunto de dados
#chave e nao indice

animal1 = {'grupo' : 'ave'
, 'alimentação' : 'carnivoro'
, 'especie' : 'urubu'
, 'habitat' : 'mata atlantica'
, 'voa' : True }
animal2 = {'grupo' : 'mamifero'
, 'alimentação' : 'onivoro'
, 'especie' : 'bizarro'
, 'habitat' : 'hidroseilaoque'
, 'voa' : False }



#=== escopo global
animais = [animal1, animal2]


#--- Função - typehinting
def funcao_cadastrar_animal(grupo:str, alimentacao:str, especie:str, habitat:str, voa:bool) ->str :
    #== escopo local ou de função
    animal = {}
    animal['grupo'] = grupo
    animal['alimentação'] = alimentacao
    animal['especie'] = especie
    animal['habitat'] = habitat
    animal['voa'] = voa
    animais.append(animal)
    return 'animal cadastrado com sucesso'

grupo = input('digite o grupo')
alimentacao = 'herbivoro'
especie = 'dinossauro'
habitat = 'deserto'
voa= True
funcao_cadastrar_animal(grupo, alimentacao, especie, habitat, voa)


for a in animais:
    print(a['especie'])


#--- Procedimento
# não ha return
# executa um conjunto de instruções

def procedimento_cadastrar_animal(grupo, alimentacao, especie, habitat, voa):
    #== escopo local ou de função
    animal = {}
    animal['grupo'] = grupo
    animal['alimentação'] = alimentacao
    animal['especie'] = especie
    animal['habitat'] = habitat
    animal['voa'] = voa
    animais.append(animal)