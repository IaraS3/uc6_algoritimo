# Exercicio 1: Crie um algoritmo que leia dois números inteiros e verifique qual é maior e qual é o menor e imprima o resultado no terminal.
# Exemplo: se numero1 = 4 for maior que numero2 = 2 então imprima no terminal a mensagem “numero1 é maior que número2” se for menor imprima que a numero1 é menor.
# Faça o uso de variaveis e input.

"""
#Lendo dois números inteiros
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#Verificando qual é maior ou menor
if numero1 > numero2:
    print("numero1 é maior que numero2")
elif numero1 < numero2:
    print("numero1 é menor que numero2")
else:
    print("numero1 é igual a numero2")
"""

# Estações do ano
# Crie um algoritmo onde o usuário digita um número de 1 até 12 e retorne em tela qual é o mês correspondente a ele:
# Exemplo de entrada: 4
# Exemplo de saída: Abril

"""
#Lendo o número do usuário
numero = int(input("Digite um número de 1 a 12: "))

#Verificando o mês correspondente
if numero == 1:
    print("Janeiro")
elif numero == 2:
    print("Fevereiro")
elif numero == 3:
    print("Março")
elif numero == 4:
    print("Abril")
elif numero == 5:
    print("Maio")
elif numero == 6:
    print("Junho")
elif numero == 7:
    print("Julho")
elif numero == 8:
    print("Agosto")
elif numero == 9:
    print("Setembro")
elif numero == 10:
    print("Outubro")
elif numero == 11:
    print("Novembro")
elif numero == 12:
    print("Dezembro")
else:
    print("Número inválido! Digite um número de 1 a 12.")
"""

#Crie um programa em Python que receba um número inteiro do usuário e determine: “É par ou é ímpar?”
# O programa deve exibir na tela se o número informado é par ou ímpar.
# num1 % 2 = 0 (par)

"""
#Recebendo um número inteiro do usuário
num1 = int(input("Digite um número inteiro: "))

#Verificando se é par ou ímpar
if num1 % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
"""