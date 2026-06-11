
import click
from src.logic import calcular_impacto, avaliar_necessidade, consultar_clima_e_recomendar, obter_historico_falso

@click.group()
def cli():
    """EcoWardrobe - Ajuda voce a consumir moda de forma consciente!"""
    pass

@cli.command()
@click.option('--pecas', default=1, help='Quantidade de pecas de roupa.')
def impacto(pecas):
    """Calcula o impacto ambiental da compra."""
    agua, co2 = calcular_impacto(pecas)
    click.echo(f"Para produzir {pecas} peca(s) de roupa sao gastos aproximadamente:")
    click.echo(f"- {agua} litros de agua")
    click.echo(f"- {co2}kg de CO2 na atmosfera")

@cli.command()
@click.option('--vezes', default=10, help='Quantas vezes pretende usar a peca.')
def decidir(vezes):
    """Avalia se a compra e realmente necessaria."""
    resultado = avaliar_necessidade(vezes)
    click.echo(resultado)

@cli.command()
def clima():
    """Consulta o clima em tempo real para recomendar o uso consciente."""
    click.echo("Conectando a API de clima externa...")
    recomendacao = consultar_clima_e_recomendar()
    click.echo(recomendacao)

@cli.command()
def historico():
    """Mostra o historico de roupas consultadas no guarda-roupa."""
    click.echo("=== HISTORICO DE CONSULTAS ECOLOGICAS ===")
    
    roupas = obter_historico_falso()
    
    for indice, roupa in enumerate(roupas, start=1):
        click.echo(f"{indice}. {roupa['nome']} | Impacto: {roupa['impacto']} (Gasto de agua: {roupa['agua']}L)")
        
if __name__ == '__main__':
    cli()

