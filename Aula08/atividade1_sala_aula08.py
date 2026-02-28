"""
Crie uma lista vazia chamada compras 
Peça ao usuário para digitar 3 itens
Adicione cada item na lista
Mostre todos os itens da lista ao final 
"""


# Laço de repetição
# Método para manipular lista
# Lista

#Crie uma lista vazia chamada compras
lista_compra =[]

#--NÃO É UMA BOA PRÁTICA DESSA FORMA
# lista_compra[0] = input("Digite o primeiro item da lista: ")
# lista_compra[0] = input("Digite o primeiro item da lista: ")
# lista_compra[0] = input("Digite o primeiro item da lista: ")

#Peça ao usuário para adicionar 3 itens 
for i in range(3):
    item = input("Digite um item: ")
#Adicione cada item na lista
    lista_compra.append(item)

print("Sua lista de compras: ")
#Mostre todos os itens da lista ao final 
for valor in lista_compra:
    print("-",valor)

