# Conversor de Dólar
# Considerando o preço do Dólar igual a 5.29 Reais

real = float(input('Quantos reais você tem na carteira? R$'))
dol = real/5.29

print('R$ {:.2f} é igual a US$ {:.2f}'.format(real,dol))
