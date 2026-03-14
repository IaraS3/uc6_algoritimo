# Data da entrega: 15/03/2025

# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens
# ________________________________
# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""
# ________________________________
# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])
# ________________________________
# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":
]
"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""
# ________________________________

# Criar um menu para selecao
while True:
    print("Menu")
    print("1 - Consultar por ID")
    print("2 - Consultar por nome")
    print("3 - Lista de personagens")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        #Consultar por ID
        





# Menu
# """
# # while True:
# #     print("\nMENU")
# #     print("1 - Par ou Ímpar")
# #     print("2 - Tabuada")
# #     print("3 - Sair")

# #     opcao = int(input("Escolha uma opção: "))

# #     if opcao == 1:
# #         # Par ou Ímpar
# #         num = int(input("Digite um número inteiro: "))
# #         if num % 2 == 0:
# #             print("O número é par.")
# #         else:
# #             print("O número é ímpar.")

# #     if opcao == 2:
# #         # Tabuada
# #         num = int(input("Digite um número: "))
# #         while num < 0:
# #             print("Número inválido, tente novamente")
# #             num = int(input("Digite um número: "))
# #         for i in range(1, 11):
# #             print(num, "x", i, "=", num * i)

# #     if opcao == 3:
# #         # Sair
# #         print("Saindo")
# #         break

# #     if opcao != 1 and opcao != 2 and opcao != 3:
# #         print("Opção inválida, tente novamente.")


# ______________________________________________
# import requests

# while True:
#     print("\n--- MENU DE SELEÇÃO ---")
#     print("1 - Consultar por ID")
#     print("2 - Consultar por nome")
#     print("3 - Lista de personagens")
#     print("3- Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         id_escolhido = input("Digite o ID do personagem: ")
#         url = f"https://rickandmortyapi.com/api/character/{id_escolhido}"
#         resposta = requests.get(url)

#         if resposta.status_code == 200:
#             mais_info = resposta.json()
#             print(f"\n--- Personagem Encontrado ---")
#             print("Nome: ", mais_info["name"])
#             print("Status: ", mais_info["status"])
#             print("Especie: ", mais_info["species"])
#             print("Genero: ", mais_info["gender"])
#             print("Localização: ", mais_info["location"])
#             print("------------------------------------")
#         else:
#             print("ID não encontrado!")
#     elif opcao =="2":