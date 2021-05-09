n = 1
primeiro_numero = []
segundo_numero = []

while n != 0:
    primeiro_numero = input('Digite Um Numero: ')
    segundo_numero = input('Digite Outro Numero: ')
    print('==' * 30)
    print(""" \033[1;33m        DIGITE UM VALOR CORRESPONDENTE AS OPÇÕES \033[m
    \033[1;m
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")
    print(' ')
    print('==' * 30)
    print('\033[m ')
    escolha = int(input('\033[1mDigite a Escolha do Menu: \033[m'))

    if escolha == 1:
        somar = int(primeiro_numero) + int(segundo_numero)
        print(' ')
        print(f'\033[1;32mA Soma dos Valores é: \033[1;31m{somar}\033[m')
        break
    if escolha == 2:
        multiplicar = int(primeiro_numero) * int(segundo_numero)
        print(' ')
        print(f'\033[1;32mA Multiplicação dos Valores é: \033[1;31m{multiplicar}\033[m')
        break

    if escolha == 3:
        if primeiro_numero > segundo_numero:
            print(' ')
            print(f'\033[1;32mEntre \033[1;95m{segundo_numero} \033[1;32me \033[1;95m{primeiro_numero}'
                  f' \033[1;32mO Numero Maior é: \033[1;31m{primeiro_numero}\033[m')
            break
        else:
            print(' ')
            print(f'\033[1;32mEntre \033[1;95m{segundo_numero}\033[m \033[1;32me \033[1;95m{primeiro_numero}'
                  f' \033[1;32mO Numero Maior é: \033[1;31m{segundo_numero}\033[m')
            break

    if escolha == 4:
        print(' ')
        continue

    if escolha == 5:
        sim_nao = str(input('\033[1;90mTem Certeza Que Deseja sair [S/N]: \033[m')).upper()
        if sim_nao == 'N':
            print(' ')
            pass
        else:
            break

print(' ')
print((14 * '\033[1;31m' '=='), 'FIM', (14 * '==')), '\033[m'
