n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1 + n2
m = n1 *  n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisao é {:.3f}' .format(s, m, d), end='>>>')
print('A divisao inteira é {} e a potencia é {}' .format(di, e))