import random
import math
import datetime

# numero_aleatorio = random.randint(1000, 2000)

# #RANDINT gera apenas números aleatórios
# print(numero_aleatorio)

# # Sorteio de aluno
# alunos = ["Israel", "Adenilson", "Anna", "Wellinton", "Jonathan", "Isabelly", "João Pedro", "Luiz Felipe"]
# sorteado = random.choice(alunos)
# sorteado2 = random.choice(alunos)

# print("Dupla Dinâmica:", sorteado, " - ", sorteado2)


# SQRT >raiz quadrada
numero = 16
raiz = math.sqrt(numero)
print(raiz)

# Elevar um numero
print(math.pow(2,2))

# Trabalhando com datas
agora = datetime.datetime.now()
print(agora.year)

# Solicitar ao usuario um numero de 1 até 5
# Gerar um numero aleatório usando a biblioteca random.randint
# Verificar se o usuário digitou o mesmo valor que o resultado 
# da função randint

numero_usuario = int(input("Digite o numero da sorte de 1 até 5:"))
numero_sorte = random.randint(1, 5)
if numero_usuario == numero_sorte:
    print("Parabéns Fulno , você ganhou um aperto de mão e dois reais")
else:
    print("Errou, tente novamente")