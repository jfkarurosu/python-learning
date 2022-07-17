from math import hypot

catOp = float(input("Digite o valor do cateto oposto: "))
catAd = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(catOp, catAd)

print("O valor da hipotenusa é {:.2f}".format(hip))