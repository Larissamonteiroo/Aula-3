print('Este caixa só possui notas de 20 reais diponíveis')

valor = int(input('Quanto deseja sacar? '))


if valor % 20 == 0:
  print(f'O valor saíra em {valor // 20} notas de 20 reais')
else:
    print(f'Não é possível tirar esse valor')
