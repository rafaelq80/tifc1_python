import subprocess
import sys

# Função auxiliar - use em todos os testes abaixo!
def preparar_e_verificar(lista_entradas, lista_saidas):
    # Prepara as variáveis
    texto_entrada = '\n'.join(lista_entradas)
    dados_entrada = texto_entrada.encode('utf-8')
    saida_esperada = '\n'.join(lista_saidas)

    # Obtém a saída real a partir das entradas
    resultado = subprocess.run([sys.executable, '-X', 'utf8', 'main.py'], input=dados_entrada, stdout=subprocess.PIPE)
    saida_bytes = resultado.stdout.strip()
    saida_texto = saida_bytes.decode("utf-8")

    # Testa se a saída esperada está na saída real
    assert saida_esperada in saida_texto

# Teste 1
def test_sentimento_sobrecarregada():
    entradas = ['a', 'b', 'c', 'd', 'e', 'f', 'sobrecarregada']
    saidas = ['Ao final do dia, sente-se sobrecarregada, mas tem a determinação de concluir a jornada.']
    preparar_e_verificar(entradas, saidas)

# Teste 2
def test_comida_pizza_batata():
    entradas = ['a', 'b', 'c', 'd', 'pizza', 'batata frita', 'g']
    saidas = ['No almoço, comeu pizza e batata frita enquanto revisava as suas anotações.']
    preparar_e_verificar(entradas, saidas)

# Teste 3
def test_comida_salada_frango():
    entradas = ['a', 'b', 'c', 'd', 'salada', 'frango', 'g']
    saidas = ['No almoço, comeu salada e frango enquanto revisava as suas anotações.']
    preparar_e_verificar(entradas, saidas)

# Teste 4
def test_tomate_tomate_tomate():
    entradas = ['tomate'] * 7
    saidas = [
        'tomate começou hoje o seu primeiro curso na Generation Brasil. '
        'Está cursando a formação em tomate. '
        'Achou a sua turma muito tomate mas o instrutor era, no mínimo, tomate. '
        'No almoço, comeu tomate e tomate enquanto revisava as suas anotações. '
        'Ao final do dia, sente-se tomate, mas tem a determinação de concluir a jornada.'
    ]
    preparar_e_verificar(entradas, saidas)

# Teste 5
def test_profissao_programador():
    entradas = ['a', 'Programador', 'c', 'd', 'e', 'f', 'g']
    saidas = ['Está cursando a formação em Programador.']
    preparar_e_verificar(entradas, saidas)

# Teste 6
def test_profissao_desenvolvedor():
    entradas = ['a', 'Desenvolvedor', 'c', 'd', 'e', 'f', 'g']
    saidas = ['Está cursando a formação em Desenvolvedor.']
    preparar_e_verificar(entradas, saidas)

# Teste 7
def test_profissao_analista_de_dados():
    entradas = ['a', 'Analista de Dados', 'c', 'd', 'e', 'f', 'g']
    saidas = ['Está cursando a formação em Analista de Dados.']
    preparar_e_verificar(entradas, saidas)

# Teste 8
def test_nome_pedro():
    entradas = ['Pedro', 'b', 'c', 'd', 'e', 'f', 'g']
    saidas = ['Pedro começou hoje o seu primeiro curso na Generation Brasil.']
    preparar_e_verificar(entradas, saidas)

# Teste 9
def test_nome_joao():
    entradas = ['João', 'b', 'c', 'd', 'e', 'f', 'g']
    saidas = ['João começou hoje o seu primeiro curso na Generation Brasil.']
    preparar_e_verificar(entradas, saidas)

# Teste 10
def test_adjetivos_quieta_barulhento():
    entradas = ['a', 'b', 'quieta', 'barulhento', 'e', 'f', 'g']
    saidas = ['Achou a sua turma muito quieta mas o instrutor era, no mínimo, barulhento.']
    preparar_e_verificar(entradas, saidas)

# Teste 11
def test_adjetivos_divertida_engracado():
    entradas = ['a', 'b', 'divertida', 'engraçado', 'e', 'f', 'g']
    saidas = ['Achou a sua turma muito divertida mas o instrutor era, no mínimo, engraçado.']
    preparar_e_verificar(entradas, saidas)