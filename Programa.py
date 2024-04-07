print('-='*22)
print('TRATAMENTO DE ERROS E EXCEÇÕES'.center(44))
print('-='*22)

def LeiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro, por favor, insira um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n1
        
def LeiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro, por favor, insira um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n2
   
Inteiro = LeiaInt('Digite um número Inteiro: ')
Real = LeiaFloat('Digite um número Real: ')
print('-='*22)
print(f'O valor Inteiro foi {Inteiro} e o Real foi {Real}')
print('-='*22)
   
                
       
       
       
       
       
