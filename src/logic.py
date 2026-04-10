#regras de calculos
def calcular_impacto (quantidade_pecas) :
    """calcula a estimativa de co2 e agua baseada em valores estimados"""
    litros_agua= quantidade_pecas *2700 #estimativa de qtd gasta de agua em uma camisa
    co2_kg= quantidade_pecas * 15 #pegada de carbono
    return litros_agua, co2_kg

def avaliar_necessidade(vezes_uso_estimado):
    """regra que se usar a peca menos de 30 vezes nao vale a pena comprar a peca"""
    if vezes_uso_estimado <30:
         return "ALERTA: Esta compra pode ser desnecessaria e vai acabar parada no seu guarda-roupa"
    else:
        return "Compra consciente, ela ira ser usada no cotiadiano"

