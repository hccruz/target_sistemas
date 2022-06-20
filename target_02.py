print('-=' * 11)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 11)

N = input('Informe um número? ')

while N.isalpha():
    print('Você deve informar um número.')
    N = input('Informe um número? ')

while int(N) <= 0:
    print('Você deve informar um número não negativo.')
    N = input('Informe um número? ')

segundoTermo = 0
primeiroTermo = 0
fibo = 0

contador = 1
fibonacci = []

while fibo <= int(N):
    if contador == 2 or contador == 3:
        primeiroTermo = 1
    fibo = primeiroTermo + segundoTermo
    fibonacci.append(fibo)
    segundoTermo = primeiroTermo
    primeiroTermo = fibo
    contador += 1

if int(N) in fibonacci:
    print(f'\nO número informado {N} pertence a sequência de Fibonacci.')
else:
    print(f'\nO número informado {N} não pertence a sequência de Fibonacci.')
