#Aluguel de Carros 

dia = int(input('Por quantos dias que o carro foi alugado? '))
horas = int(input('Por quantas horas? '))
res = dia*60+horas*0.15

print('O valor a ser pago pelo aluguel é de R${:.2f}'.format(res))
