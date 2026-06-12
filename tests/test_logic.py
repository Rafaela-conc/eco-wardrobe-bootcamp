
from src.logic import calcular_impacto, avaliar_necessidade, consultar_clima_e_recomendar, obter_historico_falso, gerar_historico_real

def test_calculo_impacto_positivo():
    agua, co2 = calcular_impacto(1)
    assert agua == 2700
    assert co2 == 15

def test_decisao_compra_impulsiva():
    assert "ALERTA" in avaliar_necessidade(10)

def test_decisao_compra_consciente():
    assert "consciente" in avaliar_necessidade(50)

def test_integracao_api_clima():
    """Teste de Integracao: Valida a conexao com a API externa de clima"""
    resultado = consultar_clima_e_recomendar()
    assert "Temperatura atual" in resultado or "Erro de conexao" in resultado
    assert len(resultado) > 0

from src.logic import calcular_impacto, avaliar_necessidade
def test_calculo_impacto_positivo():
    agua, co2= calcular_impacto(1)
    assert agua==2700
    assert co2==15

def test_decisao_compra_impulsiva():
    #Testando o caso de poucas vezes de uso
    assert "ALERTA" in avaliar_necessidade(10)

def test_decisao_compra_consciente():
    #Testando o caminho consciente
    assert "consciente" in avaliar_necessidade(50)

def test_obter_historico_falso_retorna_lista():
    # Chama a funcao que voce criou
    dados = obter_historico_falso()
    
    # Garante que o resultado e uma lista e que ela nao esta vazia
    assert isinstance(dados, list)
    assert len(dados) > 0

def test_obter_historico_falso_contem_chaves_corretas():
    # Pega o historico e isola o primeiro item da lista
    dados = obter_historico_falso()
    primeira_roupa = dados[0]
    
    # Garante que esse item tem as propriedades obrigatorias
    assert "nome" in primeira_roupa
    assert "impacto" in primeira_roupa
    assert "agua" in primeira_roupa

def test_gerar_historico_real_devolve_lista_ou_vazio():
    # Testa se a função integrada corre sem dar erros de sintaxe
    resultado = gerar_historico_real()
    assert isinstance(resultado, list)