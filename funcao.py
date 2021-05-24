#treinar funções simples.
print('=========='*15)
print('===== Funções simples, exemplo 1 ===== ')
def somar(a, b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma de A + B = {s}')


somar(12, 3)
somar(15, 3)
somar(17, 3)
somar(24, 3)

print('=========='*15)

#empacotar paramêtros:
print('=========='*15)
print('===== Empacotar paramêtros, exemplo 2.1 ===== ')
def contador(*num):
    for valor in num:
        print(f' {valor} ', end='')
    print(';')


contador(10,3,9,8)
contador(9,8)
contador(12,12,15555,8,10,3,9,8)
print('=========='*15)


#ex 2:
print('=========='*15)
print('===== Empacotar paramêtros, exemplo 2.2 ===== ')
def contador(*num):
    tam = len(num)
    print(f'Recebido os valores: {num} e são ao todo {tam} numeros.')


contador(10,3,9,8)
contador(9,8)
contador(12,12,15555,8,10,3,9,8)
print('=========='*15)




#dobrar valores de uma lista:
print('=========='*15)
print('===== Função dobrar valores de uma lista, exemplo 3 ===== ')
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [5, 3, 9, 7, 2]
dobra(valores)
print(valores)
print('=========='*15)



#Desenpacotar :
print('=========='*15)
print('===== Função desempacotar valores de uma lista, exemplo 4 ===== ')
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s} .')    


soma(1,6,9,8,7)
soma(9,7,14,3)
print('=========='*15)
print('FIM')
