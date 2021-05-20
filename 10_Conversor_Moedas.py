#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Informe quantos reais você tem na carteira: R$'))
dolar = real / 5.26

print('Com R${:.2f} reais você pode comprar {:.2f} dólar. Boa Sorte!'.format(real, dolar))
