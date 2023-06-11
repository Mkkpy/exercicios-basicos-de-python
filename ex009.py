# FACA UM PROGRAMA QUE CALCULE AS DIMENSOES DE UMA PAREDE E DE QUANTOS LITROS VOCE PRECISA
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede voce precisara de {}l detinta'.format(tinta))