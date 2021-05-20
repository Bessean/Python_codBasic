# mostrar tipo primitivo

a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaço: ', a.isspace())
print('É um número: ', a.isnumeric())
print('Está em maiúsculo: ', a.isupper())
print('Está em minúsculo: ', a.islower())
print('Está em captalizada: ', a.istitle())