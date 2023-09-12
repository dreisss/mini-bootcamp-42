# fazer uma lista selecionavel em ordem aleatoria com os nomes dos participantes

from random import choice
alunos = ["aluno1", "aluno2", "aluno3", "aluno4", "aluno5", "aluno6", "aluno7","aluno8", "aluno9"]
alunos_por_grupo = 5
# lista para armazenar os alunos selecionados
equipes = []

# seleção aleatoria de multiplos itens
while len(alunos) > alunos_por_grupo:
    equipe = []
    for _ in range (alunos_por_grupo):
        aluno = choice(alunos)
        equipe.append(aluno)
        alunos.remove(aluno)

    equipes.append(equipe)


equipes.append(alunos)
print(equipes)


