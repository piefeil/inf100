soma = 0
n = 0

for i in range(1, 5):
    cap = float(input(f'Peso da capivara {i}: '))
    if cap > 0:
        soma += cap
        n += 1
    else:
        print('Peso inválido!')

if n > 0:
    pmedio = soma / n
    print(f'\nPeso médio: {pmedio:.1f}kg \n(considerando {n} pesos válidos)')
else:
    print('\nNenhum peso válido fornecido.')
