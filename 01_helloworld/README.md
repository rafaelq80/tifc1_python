# Projeto 1 — Hello World

> Exiba a sua primeira mensagem na tela.

| | |
|---|---|
| **Tema** | Saída de dados |
| **Nível** | Iniciante |
| **O que você vai praticar** | Escrever e executar o seu primeiro programa em Python |

---

## Contexto

*Hello, World!* é a tradição de quem começa em programação: o primeiro programa de qualquer pessoa exibe essa mensagem na tela. Ele mostra que o ambiente está funcionando e que você já consegue fazer o computador "falar".

Neste projeto, o seu programa cumpre esse ritual.

---

## O que o programa deve fazer

1. Exibir na tela, e apenas ela, a mensagem abaixo.

## Modelo da mensagem

```
Hello, World!
```

## Exemplo

O programa não pede nenhuma informação ao usuário. Ao ser executado, a saída deve ser:

```
Hello, World!
```

---

## Pontos de atenção

- **O programa não recebe nenhuma entrada.** Não use `input()`.
- **O texto precisa ficar idêntico ao modelo**: mesmas palavras, vírgula, ponto de exclamação, espaços e letras maiúsculas e minúsculas.
- **Não exiba mais nada além da mensagem.** Nenhum texto extra antes ou depois.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais. Qualquer diferença no texto, por menor que seja, conta como erro.

---

# Projeto Extra — Poema do Python

> Faça o Python recitar um poema para você.

| | |
|---|---|
| **Tema** | Módulos e `import` |
| **Nível** | Iniciante |
| **O que você vai praticar** | Importar um módulo e entender que `import` pode executar código |

---

## Contexto

O Python guarda um segredo: o *Zen do Python*, escrito por Tim Peters, é um pequeno poema com os princípios que guiam a linguagem. Ele não precisa ser digitado. Basta importar o módulo certo e o poema aparece.

Neste projeto, você descobre que um `import` não só "traz" ferramentas para o seu programa: às vezes ele também faz algo na hora.

---

## O que o programa deve fazer

1. Importar o módulo `this`.
2. Deixar que o próprio módulo exiba o poema na tela.

```python
import this
```

## Saída esperada

Ao executar o programa, a saída deve ser exatamente:

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Tradução

Para ajudar na leitura, segue uma tradução do poema. Ela é só para consulta: o programa continua exibindo o texto em inglês, e é isso que o teste confere.

```
O Zen do Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aninhado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver uma — e de preferência apenas uma — maneira óbvia de fazer isso.
Embora essa maneira possa não ser óbvia a princípio, a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca seja muitas vezes melhor que *agora mesmo*.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia — vamos fazer mais deles!
```

---

## Pontos de atenção

- **O programa não recebe nenhuma entrada.** Não use `input()`.
- **Não copie o poema para dentro do seu código.** Quem exibe o texto é o módulo `this`; o seu programa só precisa importá-lo.
- **Não use `print()`.** Nada além do `import` é necessário.
- **O texto exibido precisa ficar idêntico ao poema acima**, inclusive a linha em branco depois do título. Como é o módulo que imprime, basta não alterar nada.
- **O poema aparece uma única vez**, na primeira importação do módulo. Importar `this` de novo no mesmo programa não exibe o texto outra vez.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais. Qualquer diferença no texto, por menor que seja, conta como erro.