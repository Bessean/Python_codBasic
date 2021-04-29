#Ordenar uma lista do maior para o menor e menor para maior


lista = [1,23,5,6,7,0,55,43,2,78,56,43,23,1,2,4,3,5,6,]


lista.sort(reverse=True) #usa-se para ordernar do maior para o menor.
print ("maior para o menor>>", lista)

lista.sort() #usa-se para ordenar do menor para o maior. 
print ("menor para o maior>>",lista)

len(lista)