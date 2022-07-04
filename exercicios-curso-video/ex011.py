# Calculo Tinta da Parede
# A cada 2m^2 de parede é necessário 1l de tinta

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
tinta = area/2

print("Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².\nPara pintar essa parede, você precisa de {:.2f}l de tinta".format(larg,alt,area,tinta))
