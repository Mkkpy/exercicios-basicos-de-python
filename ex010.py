# FAÇA UM PROGRAMA QUE CALCULE O DESCONTO
preço = float(input('Qual é o preço do produto? R$ '))
desconto = preço -  (preço * 5 / 100)
print('O produto que custava R$ {}, na promocao com desconto de 5% vai custar R$ {:.2f}'.format(preço, desconto))