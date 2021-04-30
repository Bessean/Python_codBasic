print ('========'*5)
print ('Como exibir uma Matriz em seu formato real!')
print ('========'*5)

def exibe (matriz, linhas, colunas):
    for L in range (3):     # refere-se as linhas
        for C in range (2): # refere-se as colunas
            print (matriz [L][C], end=' ')
        print ()  

#  Coluna  0  1  
matriz = [[10,20],  # linha 0
          [30, 40], # linha 1
          [50, 60]] # linha 2

exibe (matriz, 2, 2)


print ('========'*5)
print ('FIM DO CÓDIGO')
print ('========'*5)
