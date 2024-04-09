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
def linha(tam = 20):
    return '-=' *tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')    
    c = 1
    for item in lista:
        print(f'\033[33m{c} \033[34m{item} \033[m')
        c += 1
    print(linha())    
    opc = LeiaInt('\033[32m Sua Opção: \033[m')
    return opc