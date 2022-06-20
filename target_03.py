# importar biblioteca
import json

# Carregar dados
with open('dados.json') as file:
    data = json.load(file)

valor = []

for i in range(len(data)):
    if data[i]['valor'] != 0:
        valor.append(data[i]['valor'])

print(f'O menor valor de faturamento do mês: {min(valor)}')
print(f'O maior valor de faturamento do mês: {max(valor)}')

media = sum(valor) / len(valor)
num = 0

for i in range(len(valor)):
    if valor[i] > media:
        num += 1

print(f'Total de dias em que valor de faturamento foi maior que a média: {num} dias.')