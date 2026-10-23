import subprocess
import sys

# Função auxiliar - use em todos os testes abaixo!
def preparar_e_verificar(lista_entradas, lista_saidas):
    # Prepara as variáveis
    texto_entrada = '\n'.join(lista_entradas)
    dados_entrada = texto_entrada.encode('utf-8')
    saida_esperada = '\n'.join(lista_saidas)

    # Obtém a saída real a partir das entradas
    # sys.executable usa o mesmo Python do pytest; -X utf8 evita problemas de acentos no Windows
    resultado = subprocess.run(
        [sys.executable, '-X', 'utf8', 'main.py'],
        input=dados_entrada,
        stdout=subprocess.PIPE
    )
    saida_bytes = resultado.stdout.strip()
    saida_texto = saida_bytes.decode("utf-8")

    # Testa se a saída esperada está na saída real
    assert saida_esperada in saida_texto

# Teste 1
def test_tomate():
    # Entradas
    entradas = [
        'tomate',
        'tomate',
        'tomate',
        'lista_de_compras'
    ]

    # Saídas
    saidas = [
        "['tomate', 'tomate', 'tomate']"
    ]

    # Testa se a entrada resulta na saída
    preparar_e_verificar(entradas, saidas)

# Teste 2
def test_pizza():
    # Entradas
    entradas = [
        'Pizza',
        'Macarrão',
        'Batata frita',
        'lista_de_compras'
    ]

    # Saídas
    saidas = [
        "['Pizza', 'Macarrão', 'Batata frita']"
    ]

    # Testa se a entrada resulta na saída
    preparar_e_verificar(entradas, saidas)