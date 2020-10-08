cabecalho = 'Cadastro de funcionarios da HBSIS\n\n\n'
rodape = ' \n\n\n Obrigado pela preferencia'

def imprimir_tela(conteudo):
    print(cabecalho)
    print(conteudo)
    print(rodape)   

def ler_opcoes():
    opcao = int(input('Escolha uma opção do menu'))
    return opcao

def carregar_opcoes(opcao):
    if opcao == 1:
        imprimir_tela('opcao 1 escolhida\nCadastrar funcionário')
    elif opcao == 2:    
        imprimir_tela('opcao 2 escolhida\nListar funcionários')
    elif opcao == 3:
        imprimir_tela('opcao 3 escolhida\nEditar funcionário')
    elif opcao == 4:
        imprimir_tela('opcao 1 escolhida\nDeletar funcionário')
    elif opcao == 5:
        imprimir_tela('opcao 5 escolhida\nSaindo\n\nObrigado pela preferencia')