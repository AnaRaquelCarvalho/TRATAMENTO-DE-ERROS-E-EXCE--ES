def ArquivoExiste(nome):
    try:
        arquivo = open(nome,'LerArq')   #AbrirArquivo
        arquivo.close()  #FecharArquivo
    except FileNotFoundError:
        return False
    except:
        return True

def CriarArquivo(nome):
    try:
        arquivo = open(nome, 'criar +')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print('Arquivo {nome} criado com Sucesso!') 