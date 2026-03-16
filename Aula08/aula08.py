"""
dicionario usa {}
listas usa []
exemplo:
"""
#A Lista Inicial : O que é: Cria uma variável chamada notas que armazena uma coleção de elementos.
notas = [10, 8, 5, True, 10, 4 , 7, "Andre"]

#O método .append(): O que faz: Adiciona o novo elemento ao final da lista.
notas.append("SENAC")
print(notas)
#3. O método .insert(): O que faz: Adiciona um elemento em uma posição específica (índice).
notas.insert(0, False)
print(notas)

#uma nova lista: Cria uma lista inicial com três elementos de tipos diferentes: uma String ("Olá Mundo"), un Inteiro (1980) e um Float/Decimal (24.7).
nova_lista = ["Olá Mundo", 1980, 24.7]

#O método .extend():O que faz: Ele percorre a lista notas (que criamos no passo anterior) e anexa cada um dos itens dela ao final da nova_lista.
nova_lista.extend(notas)
print(nova_lista)


#o método remove() o item da lista
notas.remove(10)
print(notas)
notas.remove(True)
print(notas)
notas.remove("SENAC")
print(notas)
notas.remove("Andre")
print(notas)
notas.remove
#o metodo remove e case sensitive
nomes_numeros =  [390, "Adenilson", 19, "Ana", 45, "Iara", 390]

#POP
# nomes_numeros.pop(2)
# print(nomes_numeros)

#CLEAR
# print(nomes_numeros.clear())

#INDEX
print(nomes_numeros.index(390))
print(nomes_numeros)

print(nomes_numeros.count(390))

#SORT
numeros = [34, 45, 67, 89, 43, 44, 26, 58, 66, 33, 90]
numeros.sort()
print(numeros)

# REVERSE
numeros.reverse()
print()

nome = ["Adenilson", "Anna", "Beatriz", "Anne", "Bianca"]
# nome.sort()
# print(nome)
nome.reverse()
print(nome)




