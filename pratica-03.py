# Nome do aluno: Lucas Silva
# Data: 11/04/2023

# Esse programa pede para o cliente inserir o valor do peso de 4 capivaras com o comando:
# x = float( input('Peso da capivara x: '))
# Em seguida, SE o valor for maior que 0 ele atribui valor para variável soma e variável n
# a soma determina a soma dos pesos e n o número de valores válidos, através do comando:
# if x > 0:
#    soma = soma + x
#    n = n + 1  
# SE o valor NÃO for maior que zero o programa mostrará "Peso inválido", através do comando:
# else:
#    print('Peso inválido!')
# Por fim, se n for maior que 0 o programa mostrará o peso médio das capivaras
# SENÃO, aparecerá "Nenhum peso válido fornecido"

###############################################################

soma = 0
n = 0

print('Digite o peso de 4 capivaras')

cap1 = float( input('Peso da capivara 1: '))
if cap1 > 0:
    soma = soma + cap1
    n = n + 1   
else:
    print('Peso inválido!')

cap2 = float( input('Peso da capivara 2: '))
if cap2 > 0:
    soma = soma + cap2
    n = n + 1  
else:
    print('Peso inválido!')

cap3 = float( input('Peso da capivara 3: '))
if cap3 > 0:
    soma = soma + cap3
    n = n + 1   
else:
     print('Peso inválido!')

cap4 = float( input('Peso da capivara 4: '))
if cap4 > 0:
    soma = soma + cap4
    n = n + 1
else:
    print('Peso inválido!')

if n > 0:
    pmedio = soma / n
    print ('\nPeso médio: %5.1fkg \n(considerando %d pesos válidos)' %(pmedio, n))
else:
    print('\nNenhum peso válido fornecido.')

    
################################################################
