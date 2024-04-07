print('-='*22)
print('ACESSANDO O SITE PUDIM'.center(44))
print('-='*22)

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://https://www.pudim.com.br')
except (urllib.error.URLError):
    print('\033[1;31mO site Pudim não está acessível no momento.\033[m')
    print('-='*22)
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print('')
    print('-='*22)
    print('LINK PARA ACESSAR O SITE LOGO ABAIXO'.center(44))
    print(site.read())
    print('-='*22)
           