
continuar = input('Deseja iniciar o lançamento de notas? (S/N): ').upper()

while (continuar != 'S' and continuar != 'N'):
    print('Opção inválida!').upper()
    continuar = input('Informe S-sim ou N-não: ').upper()

totalAlunos = 0
totalAlunosMasculino = 0
totalAlunosFeminino = 0
totalAlunosAprovados = 0
totalAlunosAprovadosM = 0
totalAlunosAprovadosF = 0
totalAlunosReprovados = 0
totalAlunosReprovadosM = 0
totalAlunosReprovadosF = 0
totalAlunosExame = 0
totalAlunosExameM = 0
totalAlunosExameF = 0
# Evitar erro de divisão por 0
def percentual(v1, v2):
    try:
        return (v1*100)/v2
    except ZeroDivisionError:
        return 0

while (continuar == 'S'):
    totalAlunos +=1
    nome = input('Nome do aluno: ')

    sexo = input('Qual o sexo (M/F): ').upper()
    while(sexo != 'M' and sexo != 'F'):
        print('Opção inválida!')
        sexo = input('Informe M-Masculino ou F-Feminino: ').upper()
    
    #Alunos por Sexo  
    if(sexo == 'M'):
        totalAlunosMasculino +=1
    else:
        totalAlunosFeminino +=1

    nota1 = float(input('Informa a nota 1: '))
    while(nota1 > 10.0):
        print('Nota inválida!')
        nota1 = float(input('Informa a nota 1 valores de 0 a 10: '))

    nota2 = float(input('Informa a nota 2: '))
    while(nota2 > 10.0):
        print('Nota inválida!')
        nota2 = float(input('Informa a nota 2 valores de 0 a 10: '))
    
    nota3 = float(input('Informa a nota 3: '))
    while(nota3 > 10.0):
        print('Nota inválida!')
        nota3 = float(input('Informa a nota 3 valores de 0 a 10: '))

    media = ((nota1 + nota2 + nota3)/ 3)

    if media<4.0:
        totalAlunosReprovados +=1
        if(sexo == 'M'):
            totalAlunosReprovadosM +=1
        else:
            totalAlunosReprovadosF +=1
    elif media<7.0:
        totalAlunosExame +=1
        if(sexo == 'M'):
            totalAlunosExameM +=1
        else:
            totalAlunosExameF +=1
    else:
        totalAlunosAprovados +=1
        if(sexo == 'M'):
            totalAlunosAprovadosM +=1
        else:
            totalAlunosAprovadosF +=1
    
    continuar = input('Deseja continuar o sistema(S/N) ?: ').upper()
    while (continuar != 'S' and continuar != 'N'):
        print('Opção Inválida')
        continuar = input('Informe S-Sim ou N-Não: ').upper()
else:
    print('=-=' * 20)
    print ('\n\nApresentar os resultados finais\n\n')
    print('Total de alunos cadastrados:',totalAlunos)
    print ('\n\nPorcentagem dos alunos\n\n')
    print('Porcentagem de alunos Aprovados: ', percentual(totalAlunosAprovados,totalAlunos), '%')
    print('Porcentagem de alunos Exame: ', percentual(totalAlunosExame,totalAlunos), '%')
    print('Porcentagem de alunos Reprovados: ', percentual(totalAlunosReprovados,totalAlunos), '%')
    print ('\nPorcentagem de alunos por sexo:\n')
    print('Porcentagem de alunos do sexo Feminino: ', percentual(totalAlunosFeminino,totalAlunos), '%')
    print('Porcentagem de alunos do sexo Masculino: ', percentual(totalAlunosMasculino,totalAlunos), '%')
    print ('\nValores Absolutos\n')
    print('Total de alunos sexo Feminino Aprovados:', totalAlunosAprovadosF)
    print('Total de alunos sexo Masculino Aprovados:', totalAlunosAprovadosM)
    print('=-=' * 20)
    print('Total de alunos sexo Feminino Exame:', totalAlunosExameF)
    print('Total de alunos sexo Masculino Exame:', totalAlunosExameM)
    print('=-=' * 20)
    print('Total de alunos sexo Feminino Reprovados:', totalAlunosReprovadosF)
    print('Total de alunos sexo Masculino Reprovados:', totalAlunosReprovadosM)
