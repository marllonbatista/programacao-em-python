'''
    Faça um programa que leia um número inteiro fornecido pelo usuário.
    Se esse número for positivo, calcule a raiz quadrada do número e apresente-a.
    Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
'''

num= int(input("Digite um número inteiro: "))
if num > 0:
    raiz= num ** 0.5
    print(f'A raiz quadrada do {num} é : {raiz}')
else:
    print("número inválido")