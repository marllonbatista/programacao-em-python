'''
Faça um programa que tenha uma função que recebe uma data no formato string
exemplo "01/01/2024" e imprima ela por extenso com "1 de janeiro de 2024".
'''

meses= {'01':'Janeiro','02':'Fevereiro', '03':'Março', '04':'Abril',
'05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto',
'09':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}

def formataData(data):
    dia,mes,ano= data.split("/")

    return f"{int(dia)} de {meses[mes]} de {ano}"

data ="03/09/2026"
print(formataData(data))
