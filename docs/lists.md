# Listas de Exercícios

As listas de exercícios são listas com diversos problemas para serem resolvidos
utilizando `C` ou `Shell`. Para resolver a lista é permitidu utilizar quaisquer
recursos. É permitido utilizar o Google, ChatGPT, etc., além de pedir ajuda dos
seus pares.

### Pontuação

Cada exercício nas listas conta ponto para o participante de acordo com o
seguinte esquema:

| Exercício | Pontos |
| :-------: | :----: |
|     0     |   1    |
|     1     |   2    |
|    ...    |        |
|     x     | x + 1  |

Ou seja, o ponto de um exercício é o seu número na lista mais um.

É importante resaltar que contarão pontos somente os exercícios corretos até a
primeira solução errada da lista, todos os exercícios, mesmo os corretos, serão
desconsiderados se algum exercício anterior estiver errado. Veja o exemplo:

| Exercício | Pontos | Está correto? | Contará no total? |
| :-------: | :----: | :-----------: | :---------------: |
|     0     |   1    |      Sim      |        Sim        |
|     1     |   2    |      Sim      |        Sim        |
|     2     |   3    |      Sim      |        Sim        |
|     3     |   4    |      Sim      |        Sim        |
|     4     |   5    |      Não      |        Não        |
|     5     |   6    |      Não      |        Não        |
|     6     |   7    |      Sim      |        Não        |

Assim, a pontuação total será: 1 + 2 + 3 + 4 = 10.

Caso o participante consiga acerta todos os exercícios da lista ele ganhará 5
pontos bonus.

Todos participantes terão 3 tentativas para conseguir o máximo de pontos de cada
lista. Caso não consiga ele avançará para a próxima lista com a maior pontuação
que conseguiu.

### Submissão

Para fazer a submissão das soluções é necessário que os participantes criem um
repositório no Github para armazenar as soluções (não importando o nome). Cada
solução deve ser separada da seguinte maneira:

- Um diretório para cada lista resolvida: `shell00`, `c01`, ...
- Dentro do diretório da lista crie diretórios com os exercícios: `ex00`, `ex01`, ...

Note que os nomes devem seguir esse padrão, caso contrário o sistema não localizará
as soluções e o participante não pontuará.

Além disso, é necessário que o participante crie uma issue no repositório do
evento com a label `solutions`. O título da issue deve seguir o seguinte padrão:
solutions: \[Nome do Participante\]; e na descrição deve estar o link para o
repositório com as soluções.

Ao finalizar uma lista, o participante deve comentar na issue criada a lista
que concluiu (`shell00`, `shell01`, `c00`, ...), após isso o resultado da correção
do sistema será publicada na mesma issue.
