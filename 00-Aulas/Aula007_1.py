#====== Funções
from Aula007_2 import imprimir_tela, ler_opcoes, carregar_opcoes

opcoes_menu = '''1) Cadastrar funcionário:\n 
    2) Listar funcionários:\n 
    3) Editar funcionário:\n 
    4) Deletar funcionário:\n 
    5) Sair:'''

imprimir_tela(opcoes_menu)
item = ler_opcoes()
carregar_opcoes(item)