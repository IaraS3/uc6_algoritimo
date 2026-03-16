"""
Crie uma lista com 4 nomes
Peça ao usuário um nome para remover
Se o nome existir, remova
Se não, mostre uma mensagem dizendo "nome não encontrado"
Mostre a lista final
"""

# Crie uma lista com 4 nomes
lista_nomes = ["Ana", "Carlos", "Mariana", "João"]

# Peça ao usuário um nome para remover
nome_remover = input("Digite um nome para remover: ")

# Se o nome existir, remova
if nome_remover in lista_nomes:
    lista_nomes.remove(nome_remover)
    print("Nome removido.")
else:
    print("Nome não encontrado")

# Mostre a lista final
print("\nLista final:")
for nome in lista_nomes:
    print("-", nome)