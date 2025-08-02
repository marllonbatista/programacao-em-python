'''
    Faça um programa  que recebe três valores e apresente a soma 
    dos quadrados dos valores lidos.
'''

soma =0
for i in range(1,4):
    num= float(input(f'Digite o {i}° número: '))
    soma+=(num*num)
print(f'A soma dos quadrados dos valores: {soma}')