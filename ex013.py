# FAÇA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM RODADOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
# CALCULE O PREÇO A PAGAR, SABENDO QUE O CAROO CUSTA R$ 60 POR DIA E R$ 0.15 POR KM RODADO
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
p1 = dias * 60
p2 = km * 0.15
print('O total a pagar é de R$ {:.2f}'.format(p1+p2))
