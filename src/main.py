#Ponto de entrada (CLI)
import click
from logic import calcular_impacto, avaliar_necessidade

@click.group()
def cli():
    """Eco Wardrobe: Ajuda voce consumir a moda de uma maneira consciente"""
    pass
@cli.command()
@click.option('--pecas', default=1, help='Quantidade de pecas compradas no ano.')
def impacto(pecas):
    agua, co2=calcular_impacto(pecas)
    click.echo(f"Seu guarda-roupa consumiu aproximadamente. {agua}L de agua e gerou {co2}kg de CO2.")

@cli.command()
@click.argument('usos', type=int)
def decidir(usos):
    resultado=avaliar_necessidade(usos)
    click.echo(resultado)

if __name__=='__main__':
    cli()