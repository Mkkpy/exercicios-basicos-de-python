# crie um programa que leia a medida e mostre ela em centimetros e milimetros
medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}km, {}hm'.format(medida, km, hm), end=' ')
print('{}dam, {}dm, {}cm e {}mm'.format(dam, dm, cm, mm))