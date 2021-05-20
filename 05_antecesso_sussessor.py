#Exercício Python 05: Faça um programa que leia um número Inteiro 
# e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
a = num - 1
s = num + 1


print('O número digitado foi {} e o antecessor dele é o {} e o sucessor é o {} !'.format(num, a, s))

print('=========='*10)
print('ourta forma: ')

n = int(input('Digite um número: '))
print('O número digitado foi {} e o antecessor dele é o {} e o sucessor é o {} !'.format(num, (num-1), (num+1)))