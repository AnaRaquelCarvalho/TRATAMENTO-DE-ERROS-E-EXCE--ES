import Cadastramento.pessoas

def ArquivoExiste(nome):
    try:
        arquivo = open(nome,'rt')   #AbrirArquivo
        arquivo.close()  #FecharArquivo
    except FileNotFoundError:
        return False
    except:
        return True

def CriarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print('Arquivo {nome} criado com Sucesso!')  

def LerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        Cadastramento.pessoas.cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        arquivo.close()            

def cadastrar(arquivo, nome = 'desconhecido', idade=0):
    try:
        arquivo = open (arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print(f'Novo registro de {nome} adicionado')
            arquivo.close()








