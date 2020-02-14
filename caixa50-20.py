valor = int(input('Informe o valor desejado: '))

nota50=0
nota20=0

if valor % 10 != 0:
    print('valor inválido')
else:
    if valor % 20 == 0:
        print(f'{int(valor/20)} notas de 20')
    elif valor % 50 == 0:
        print(f'{int(valor/50)} notas de 50')
    elif valor==30 or valor==10:
        print('valor inválido')
    else:
        while valor > 0:
          if valor >= 20:
                nota20 += 1
                valor = valor-20

          if valor >= 50:
                nota50 += 1
                valor = valor-50

        print(f'{nota50} notas de 50')
        print(f'{nota20} notas de 20')
