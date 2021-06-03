from math import sqrt

while True:
    print('==' * 30)
    print(""" \033[1;33m        DIGITE UM VALOR CORRESPONDENTE AS OPÇÕES \033[m
    \033[1;m
[1] SOMAR
[2] MULTIPLICAR
[3] DIVIDIR
[4] SUBTRAIR
[5] RAIZ QUADRADA
[6] POTENCIA
[7] MAIOR
[8] SAIR DO PROGRAMA""")
    print(' ')
    print('==' * 30)
    print('\033[m ')
    escolha = int(input('\033[1mDigite a Escolha do Menu: \033[m'))
    print(' ')

    if escolha == 1:
        primeiro_numero = input('Digite Um Numero: ')
        segundo_numero = input('Digite Outro Numero: ')
        somar = int(primeiro_numero) + int(segundo_numero)
        print(' ')
        print(f'\033[1;32mA Soma dos Valores é: \033[1;31m{somar}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break

        
    elif escolha == 2:
        primeiro_numero = input('Digite Um Numero: ')
        segundo_numero = input(f'Digite Outro Numero: {primeiro_numero} x ')
        multiplicar = int(primeiro_numero) * int(segundo_numero)
        print(' ')
        print(f'\033[1;32mA Multiplicação dos Valores é: \033[1;31m{multiplicar}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break

    elif escolha == 3:
        primeiro_numero = input('Digite Um Numero: ')
        segundo_numero = input(f'{primeiro_numero} ÷ ')
        dividir = float(primeiro_numero) / float(segundo_numero)
        print(f'\033[1;32mA Divisão dos Valores é: \033[1;31m{dividir:.1f}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break

    elif escolha == 4:
        primeiro_numero = input('Digite Um Numero: ')
        segundo_numero = input(f'{primeiro_numero} -  ')
        subtrair = int(primeiro_numero) - int(segundo_numero)
        print(f'\033[1;32mA Subtração dos Valores é: \033[1;31m{subtrair}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break

    elif escolha == 5:
        primeiro_numero = input('Digite Um Numero: √')
        raiz_quadrada2 = sqrt(float(primeiro_numero))
        print(f'\033[1;32mA Raiz Quadrada de {primeiro_numero} é: \033[1;31m{raiz_quadrada2:.2f}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break    

    elif escolha == 6:
        primeiro_numero = input('Digite um Numero: ')
        segundo_numero = input(f'{primeiro_numero} ^ ')
        potencia = int(primeiro_numero) ** int(segundo_numero)
        print(f'\033[1;32mO Numero {primeiro_numero} Elevado a {segundo_numero} \033[m'
        f'\033[1;32mPotencia é: \033[1;31m{potencia}\033[m')
        sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
        if sim_nao == 'S':
            print(' ')
            continue
        else:
            break    


    elif escolha == 7:
        primeiro_numero = input('Digite Um Numero: ')
        segundo_numero = input('Digite Outro Numero: ')
        if primeiro_numero > segundo_numero:
            print(' ')
            print(f'\033[1;32mEntre \033[1;95m{segundo_numero} \033[1;32me \033[1;95m{primeiro_numero}'
                  f' \033[1;32mO Numero Maior é: \033[1;31m{primeiro_numero}\033[m')
            sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
            if sim_nao == 'S':
                print(' ')
                continue
            else:
                break
        else:
            print(' ')
            print(f'\033[1;32mEntre \033[1;95m{segundo_numero}\033[m \033[1;32me \033[1;95m{primeiro_numero}'
                  f' \033[1;32mO Numero Maior é: \033[1;31m{segundo_numero}\033[m')
            sim_nao = str(input('\033[1;90mDESEJA CONTINUAR? [S/N]: \033[m')).upper()
            if sim_nao == 'S':
                print(' ')
                continue
            else:
                break

    elif escolha == 8:
        sim_nao = str(input('\033[1;90mTem Certeza Que Deseja sair [S/N]: \033[m')).upper()
        if sim_nao == 'N':
            print(' ')
            continue
        else:
            break
    else:
        print('DIGITE UM NUMERO VALIDO!!!')

print(' ')
print((14 * '\033[1;31m' '=='), 'FIM', (14 * '==')), '\033[m'
