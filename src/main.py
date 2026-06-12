import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import listar_roupas, cadastrar_roupa

import click
from src.logic import calcular_impacto, avaliar_necessidade, consultar_clima_e_recomendar, gerar_historico_real

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
@click.option('--nome', prompt='Nome da roupa', help='Nome ou tipo da peça.')
@click.option('--categoria', prompt='Categoria', help='Ex: Camiseta, Calça, Vestido.')
@click.option('--tamanho', prompt='Tamanho (P, M, G)', help='Tamanho da peça.')
@click.option('--preco', prompt='Preço (R$)', type=float, help='Preço da peça.')
@click.option('--descricao', prompt='Descrição', help='Detalhes da peça.')
def cadastrar(nome, categoria, tamanho, preco, descricao):
    """Cadastra uma nova roupa direto no MySQL da Aiven (Equivalente ao POST)."""
    try:
        click.echo("🔄 Conectando ao MySQL na nuvem para salvar a peça...")

        # Chama a função que seu colega criou no database.py
        novo_id = cadastrar_roupa(nome, categoria, tamanho, preco, descricao)

        if novo_id:
            click.echo(f"✅ Cadastrado com sucesso! ID da nova peça no banco: {novo_id}")
        else:
            click.echo("❌ Erro ao cadastrar peça no banco de dados.")

    except Exception as e:
        click.echo(f"Ocorreu um erro interno: {str(e)}")


@cli.command()
def listar():
    """Busca e exibe todas as roupas salvas na nuvem (Equivalente ao GET)."""
    try:
        click.echo("🔄 Buscando roupas na nuvem da Aiven...")

        # Chama a função que faz o SELECT * FROM roupas
        roupas_salvas = listar_roupas()

        if not roupas_salvas:
            click.echo("Nenhuma roupa encontrada no banco de dados.")
            return

        click.echo(f"Sucesso! Encontramos {len(roupas_salvas)} roupa(s) no banco:\n")

        # Exibe cada roupa bonitinha no terminal
        for roupa in roupas_salvas:
            click.echo(
                f"🆔 ID: {roupa['id']} | 👕 {roupa['nome']} | 📦 Cat: {roupa['categoria']} | 📏 Tam: {roupa['tamanho']} | 💰 R$ {roupa['preco']}")
            click.echo(f"📝 Descrição: {roupa['descricao']}")
            click.echo("-" * 50)

    except Exception as e:
        click.echo(f"Erro ao buscar dados no MySQL: {str(e)}")

@cli.command()
def historico():
    """Exibe o relatório ecológico do teu guarda-roupa baseado na base de dados."""
    try:
        click.echo(" A ligar à base de dados na nuvem da Aiven...")
        dados = gerar_historico_real()

        if not dados:
            click.echo("🧳 O teu guarda-roupa ecológico ainda está vazio!")
            return

        agua_total = sum(item['agua'] for item in dados)
        co2_total = sum(item['co2'] for item in dados)

        click.echo("\n === O TEU HISTÓRICO ECOLÓGICO REAL ===")
        for item in dados:
            click.echo(f"👕 Peça: {item['nome']} | 🌱 Impacto: {item['impacto']} | 💧 {item['agua']}L")

        click.echo("-------------------------------------------")
        click.echo(f"Total de Peças Avaliadas: {len(dados)}")
        click.echo(f"Pegada Hídrica Total Acumulada: {agua_total} litros")
        click.echo(f"Emissões de CO2 Totais Acumuladas: {co2_total} kg")
        click.echo("===========================================\n")

    except Exception as e:
        click.echo(f" Erro ao carregar o histórico: {str(e)}")

if __name__ == '__main__':
    cli()