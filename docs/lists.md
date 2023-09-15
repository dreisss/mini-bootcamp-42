# Listas de Exercícios

As listas de exercícios são listas com diversos problemas para serem resolvidos
utilizando `C` ou `Shell`. Para resolver a lista é permitido utilizar quaisquer
recursos. É permitido utilizar o Google, ChatGPT, etc., além de pedir ajuda dos
seus pares.

### Submissão

Para fazer a submissão das soluções é necessário que os participantes criem um
repositório no Github para armazenar as soluções (não importando o nome). Cada
solução deve ser separada da seguinte maneira:

- Um diretório para cada lista resolvida, por exemplo: `shell00`, `c01`, ...
- Dentro do diretório da lista crie diretórios com os exercícios, por exemplo:
  `ex00`, `ex01`, ...

Assim, teremos o seguinte esquema de pastas:

```
.
├── shell00
│  ├── ex00
│  ├── ex01
│  ├── ex02
│  └── ...
├── c00
│  ├── ex00
│  ├── ex01
│  ├── ex02
│  └── ...
└── ...
```

Note que os nomes devem seguir esse padrão, caso contrário o sistema não localizará
as soluções e o participante não pontuará.

Além disso, é necessário que o participante crie uma issue no repositório do
evento com a label `solutions`. O título da issue deve seguir o seguinte padrão:
solutions: \[Nome do Participante\]; e na descrição deve estar o link para o
repositório com as soluções.

Ao finalizar uma lista, o participante deve comentar na issue criada a lista
que concluiu (`shell00`, `shell01`, `c00`, ...), após isso o resultado da correção
do sistema será publicada na mesma issue. Além disso, o participante deve informar
um avaliador, a fim de chamar outro participante disponível para fazer a revisão
em pares, cujo resultado também será publicado na mesma issue criada anteriormente.

Cada participante pode tentar submeter a mesma lista até 3 vezes. Se houver mais
de 3 tentativas, apenas as 3 primeiras serão consideradas.

### Pontuação

A pontuação atribuída a cada exercício nas listas é baseada em seu número na
lista. Cada exercício vale um ponto, mais um ponto adicional para cada número
subsequente. Veja o exemplo abaixo:

| Exercício | Pontos |
| :-------: | :----: |
|     0     |   1    |
|     1     |   2    |
|    ...    |        |
|     x     | x + 1  |

Isso significa que o primeiro exercício vale 1 ponto, o segundo vale 2 pontos,
o terceiro vale 3 pontos e assim por diante.

É importante observar que apenas os exercícios corretos até a primeira solução
incorreta da lista serão pontuados. Se um exercício anterior estiver incorreto,
todos os exercícios, mesmo os corretos, serão desconsiderados. Veja o exemplo:

| Exercício | Pontos | Está correto? | Contará no total? |
| :-------: | :----: | :-----------: | :---------------: |
|     0     |   1    |      Sim      |        Sim        |
|     1     |   2    |      Sim      |        Sim        |
|     2     |   3    |      Sim      |        Sim        |
|     3     |   4    |      Sim      |        Sim        |
|     4     |   5    |      Não      |        Não        |
|     5     |   6    |      Não      |        Não        |
|     6     |   7    |      Sim      |        Não        |

Neste exemplo, a pontuação total será 1 + 2 + 3 + 4 = 10.

Além disso, se um participante conseguir resolver todos os exercícios da lista
corretamente, ele receberá um bônus de 10 pontos.

Todos participantes terão 3 tentativas para conseguir o máximo de pontos de cada
lista. Caso não consiga ele avançará para a próxima lista com a maior pontuação
que conseguiu.
