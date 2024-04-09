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
        Cadastramento.pessoas.cabeçalho(' Opção 1')
    elif resposta == 2:
        Cadastramento.pessoas.cabeçalho(' Oção 2')
    elif resposta == 3:
        Cadastramento.pessoas.cabeçalho(' SAINDO DO PROGRAMA...')          
        sleep(2)
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')    