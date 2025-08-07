'''
    Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
'''

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite mais um número inteiro:"))
if num1 > num2:
    print(f'O número {num1} é maior.')
elif num2 >num1:
    print(f'O número {num2} é maior.')
else:
    print(f'O primeiro número é igual o segundo número.')

