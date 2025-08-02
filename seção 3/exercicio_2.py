'''
    Faça um programa  que peça para o usuário digitar três
    valores  inteiro e imprima a soma deles.
'''
soma =0
for i in range(1,4):
    num= int(input(f'Digite o {i}° número: '))
    soma+=num
print(f'Total: {soma}')