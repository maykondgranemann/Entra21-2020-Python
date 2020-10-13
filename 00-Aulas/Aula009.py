#=== Arquivos - Manipulação texto

#-open

#-- Escrita
#-- x = cria um novo arquivo, caso o arquivo ja exista, da erro
#-- w = cria um novo arquivo, porem se o arquivo existir ele apaga o antigo
#-- a = adiciona uma nova linha ao final do arquivo
dict_person = {'first':'maykon', 'last':'granemann', 'age':18}
arquivo = open('pessoa.txt','a')
arquivo.write(f"{dict_person['first']};{dict_person['last']};{dict_person['age']}; \n")
arquivo.close()


#-- Leitura
arquivo = open('pessoa.txt','r')
for linha in arquivo:
    linha_limpa = linha.strip() #-- limpa espaços em brando e caracteres de formatação (\n \t)
    lista_dados = linha_limpa.split(';')
    print(f"nome:{lista_dados[0]} - sobrenome:{lista_dados[1]}, idade:{lista_dados[2]}")

arquivo.close()