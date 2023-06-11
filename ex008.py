# CRIE UM PROGRAMA QUE LEIA QUANTO VOCE TEM EM REAIS E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
real = float(input('Quanto dinheiro voce tem na carteira: '))
dolar = real / 3.27
print('Com R$ {:.2f} voce pode comprar {:.2f} US$'.format(real, dolar))