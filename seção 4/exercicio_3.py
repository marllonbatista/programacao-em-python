'''
    Faça um programa que recebe um número inteiro e informe se este número é
    par ou ímpar
'''

num = int(input(f'Digite um número inteiro: '))
if num % 2 == 0:
    print(f' o número {num} é par.')
else:
    print(f' o número {num} é ímpar.')
