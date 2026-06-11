#regras de calculos
import requests

def calcular_impacto(quantidade_pecas):
    """Calcula a estimativa de CO2 e água em valores estimados"""
    litros_agua = quantidade_pecas * 2700
    co2_kg = quantidade_pecas * 15
    return litros_agua, co2_kg


def avaliar_necessidade(vezes_uso_estimado):
    """Regra para um consumo consciente"""
    if vezes_uso_estimado < 30:
        return "ALERTA: Esta compra pode ser desnecessaria e vai acabar parada no seu guarda-roupa."
    else:
        return "Compra consciente, ela ira ser usada no cotidiano."


def consultar_clima_e_recomendar():
    """Consome uma API Pública de Clima (Open-Meteo) na regiao de São Paulo"""
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=-23.5489&longitude=-46.6388&current_weather=true"
        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados["current_weather"]["temperature"]

            if temperatura < 20:
                return f"Temperatura atual: {temperatura}°C. Recomendacao: Prefira usar casacos que voce ja tem no armario!"
            else:
                return f"Temperatura atual: {temperatura}°C. Recomendacao: O clima esta ameno/quente. Use roupas leves!"
        else:
            return "Não foi possivel obter os dados de clima agora."
    except Exception:
        return "Erro de conexao com a API de clima."
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

def obter_historico_falso():
    """
    Função pura que retorna uma lista de dicionários simulando 
    as roupas salvas no guarda-roupa.
    """
    # Dados fakes para testar a estrutura do comando
    historico_roupas = [
        {"nome": "Blusa de Algodão", "impacto": "Baixo", "agua": 200},
        {"nome": "Calça Jeans", "impacto": "Alto", "agua": 8000},
        {"nome": "Casaco de Poliéster", "impacto": "Médio", "agua": 1500}
    ]
    
    return historico_roupas
