# Calculando Descontos
prod = float(input("Qual o valor do produto: "))
res = prod -(prod*5/100)

print('O produto que custava R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(prod,res))