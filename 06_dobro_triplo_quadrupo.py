#Exercício 06: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite o número: '))

print('Analisando o número {}... \nVerifico que o dobro é {}. \nO triplo {}. \nE a raiz quadrada {:.2f}.'.format(n, n*2, n*3, pow(n,(1/2))))

#obs: raiz quadrada pode ser reprensentada como pow(n,(1/2)