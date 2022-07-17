import math
from traceback import print_tb

angd = float(input("Digite um ângulo qualquer: "))
ang = math.radians(angd)
seno = math.sin(ang)
cose = math.cos(ang)
tang = math.tan(ang)

print("O ângulo de {}° tem seno de {:.2f} cosseno de {:.2f} e tangente de {:.2f}".format(angd,seno,cose,tang))
