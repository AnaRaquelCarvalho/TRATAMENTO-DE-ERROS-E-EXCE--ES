print('CADASTRO DE PESSOAS'.center(38))

import Arquivo.Dados
import Arquivo.ArquivoDados 
from time import sleep

arquivo = 'Bancodedados.txt'

if not Arquivo.ArquivoDados.ArquivoExiste(arquivo):
   Arquivo.ArquivoDados.CriarArquivo(arquivo)   

while True:
    resposta = Arquivo.Dados.menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        Arquivo.Dados.cabeçalho(' Opção 1')
    elif resposta == 2:
        Arquivo.Dados.cabeçalho(' Oção 2')
    elif resposta == 3:
        Arquivo.Dados.cabeçalho(' SAINDO DO PROGRAMA...')          
        sleep(2)