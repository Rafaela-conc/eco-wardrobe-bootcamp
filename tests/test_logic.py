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
