"""
Em um arquivo exercicio_aula05.py você terá que criar um algoritmo utilizando laço de 
repetição e estrutura condicional para criar uma tabuada, seguindo as seguintes regras:
Seu programa precisa receber um número digitado pelo usuário, verifique se esse número é válido, 
se o número for válido então use o laço de repetição para mostrar a tabuada utilizando o número que 
o usuário digitou se o número for inválido então mostrar a mensagem “Número invalido, tente novamente”.
"""

numero = int(input("Digite um número: "))

while numero < 0:
    print("Número inválido, tente novamente")
    numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


"""
DESAFIO 1:Contando de 1 até 10 (marcando os pares)
"""
# # Recebendo um número inteiro
# num1 = int(input("Digite um número inteiro de 1 a 10: "))
# # Verificando se está entre 1 e 10
# while num1 < 1 or num1 > 10:
#     print("Número inválido! Digite apenas de 1 a 10.")
#     num1 = int(input("Digite um número inteiro de 1 a 10: "))
# # Verificando se é par ou ímpar
# if num1 % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

"""
DESAFIO 2: Menu
"""
# while True:
#     print("\nMENU")
#     print("1 - Par ou Ímpar")
#     print("2 - Tabuada")
#     print("3 - Sair")

#     opcao = int(input("Escolha uma opção: "))

#     if opcao == 1:
#         # Par ou Ímpar
#         num = int(input("Digite um número inteiro: "))
#         if num % 2 == 0:
#             print("O número é par.")
#         else:
#             print("O número é ímpar.")

#     if opcao == 2:
#         # Tabuada
#         num = int(input("Digite um número: "))
#         while num < 0:
#             print("Número inválido, tente novamente")
#             num = int(input("Digite um número: "))
#         for i in range(1, 11):
#             print(num, "x", i, "=", num * i)

#     if opcao == 3:
#         # Sair
#         print("Saindo")
#         break

#     if opcao != 1 and opcao != 2 and opcao != 3:
#         print("Opção inválida, tente novamente.")

