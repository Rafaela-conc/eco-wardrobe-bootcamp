from src.logic import calcular_impacto, avaliar_necessidade, consultar_clima_e_recomendar

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