'''
Faça um programa que leia 10 valores,  armazene-os em uma lista e apresente
quantos valores pares ele possui.
'''
i =1
lista=[]
cont = 0 #  variavel para contar a quantidade de valores pares
while i<=10:
    num = int(input((f"Digite o {i}° valor:")))
    lista.append(num)
    if num % 2 == 0:
        cont = cont + 1
    i +=1
if cont != 0:
    print(f" Você digitou {cont} valor(es) par(es)")
else:
    print("Você só digitou valor impar")
