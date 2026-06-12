# Importa as funções que criamos no arquivo database.py
from database import listar_roupas, cadastrar_roupa

print("🔄 Testando conexão com o MySQL na nuvem...")

# 1. Tenta listar o que já está no banco (deve trazer a jaqueta do Workbench)
roupas_salvas = listar_roupas()

print(f"\n📦 Sucesso! Encontramos {len(roupas_salvas)} roupa(s) no banco:")
for roupa in roupas_salvas:
    print(f"- {roupa['nome']} | Tamanho: {roupa['tamanho']} | Preço: R${roupa['preco']}")

# 2. Vamos tentar cadastrar uma NOVA roupa direto pelo Python!
print("\n👗 Tentando cadastrar uma nova peça pelo Python...")
novo_id = cadastrar_roupa(
    nome="Vestido Florido Verão",
    categoria="Vestido",
    tamanho="M",
    preco=59.90,
    descricao="Vestido leve, estampa de girassol, usado uma vez."
)

if novo_id:
    print(f"✅ Cadastrado com sucesso! ID da nova peça: {novo_id}")
else:
    print("❌ Erro ao cadastrar peça.")