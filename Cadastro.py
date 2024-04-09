print('-='*20)
print('CADASTRO DE PESSOAS'.center(38))

import Cadastramento.pessoas
import Cadastramento.BancoDADOS 
from time import sleep

arquivo = 'Bancodedados.txt'

if Cadastramento.BancoDADOS.ArquivoExiste(arquivo):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!') 
    Cadastramento.BancoDADOS.CriarArquivo(arquivo)   

while True:
    resposta = Cadastramento.pessoas.menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        Cadastramento.BancoDADOS.LerArquivo(arquivo)
    elif resposta == 2:
        #Opção cadastrar novas pessoas
        Cadastramento.pessoas.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = Cadastramento.pessoas.LeiaInt('Idade: ')
        Cadastramento.BancoDADOS.cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        #oPÇÃO DE SAIR DO SISTEMA
        Cadastramento.pessoas.cabeçalho(' SAINDO DO PROGRAMA...')          
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')    