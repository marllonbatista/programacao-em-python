'''
Crie um programa que tenha uma função que recebe um parâmetro
inteiro e devolve o seu dobro.
'''
def dobro (num):
    return num*2

n: int = int(input("Digite um numero:"))

resultado=dobro(n)
print(f'O dobro do número {n} é {resultado}')