print ('--'*30)
print ('SELEÇÃO ANINHADA ENCADEADA EX 04')
print ('--'*30)
tipo = input ('Tipo de Voo é D ou N: ')
qtd = int(input('Informe a quantidade de pessoas: '))
if tipo == 'D':
    if qtd <=50:
        tarifa = 200.0
    else:
        tarifa = 120.0
else:
    if qtd <= 50:
        tarifa = 100.0
    else:
        tarifa = 80.0
total = qtd * tarifa
print ('Total: R$ %.2f' % total)
        
