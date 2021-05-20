#Exercício 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Informe o metro: '))
cm = n*100 #Centimétro
mm = n*1000 #Milímetro
dm = n*10  #Decímetro
dam = n/10 #Decâmetro
hm = n/100 #Hectômetro
km = n/1000 #Quilômetro


print('Metro = {}. \nEm centimétro = {}. \nEm milímetro = {}. \nEm Decímetro = {}. \nDecâmetro = {}. \nHectômetro = {}. \nQuilômetro = {}.'.format(n, cm, mm, dm, dam, hm, km))