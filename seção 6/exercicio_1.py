'''
Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre
na tela os valores lidos.
'''
lista=[]
for i in range (1,7):
    num :int= int(input(f"Digite o {i}° valor inteiro :"))
    lista.append(num)
print(lista)