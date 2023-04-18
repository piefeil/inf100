# Nome do aluno: Lucas Silva
# Data:04/04/2023
# 1 -> No primeiro bloco o programa mostra diversas informações sobre a UFV, alinhadas por coluna, por meio da função print(), usando variáveis e strings.
# 2 -> No segundo bloco o programa mostra a área total do campus de Viçosa, usando diferentes larguras e casas decimais com o comando %f.
# 3 -> No terceiro bloco o programa usa a função input() e print() que, respectivamente, recebem e imprimem dados sobre em qual período do curso o aluno está.

nomeInst = 'Universidade Federal de Viçosa'
num_alunos = 16560     # alunos de graduação matriculados no campus Viçosa
rel_cand_vagas = 10.3  # relação candidatos / vagas total
area = 2353.94         # área física total em hectares (ha)
anoAtual = 2023        # ano corrente
#OBS: Esse bloco é responsável por definir o valor das variáveis usadas abaixo. 

print() #este comando imprime uma linha em branco

############################################################################

print('\nNome da instituição:' , (25*' ') , '%s' %nomeInst)
print('Alunos de grad. matriculados no campus Viçosa: %d' %num_alunos)
print('Relação candidatos / vagas total:' , (12*' ') , '%.1f' %rel_cand_vagas)
print('Área total do campus Viçosa:' , (17*' ') , '%.2f ha' %area)

print('\nÁrea total do campus Viçosa (ha):')
print('Usando largura 7 e 2 casas decimais: %7.2f' %area)
print('Usando largura 9 e 2 casas decimais: %9.2f' %area)
print('Usando largura 9 e 3 casas decimais: %9.3f' %area)
print('Usando largura 9 e nenhuma casa decimal: %9.0f' %area)
print()
nome = input('Qual o seu nome?' ' ')
curso = input('Qual o seu curso?' ' ')
ano_inc = int(input('Em que ano você iniciou seu curso?' ' '))
periodo = ((((anoAtual) - (ano_inc))*2) + 1)
print('%s, você está no %dº período de %s' %(nome, periodo, curso))

#############################################################################
