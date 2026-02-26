# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# cidade = input("Digite sua cidade: ")

# pessoa = {
#     "nome": nome,
#     "idade": idade,
#     "cidade": cidade
# }

# print(pessoa)
# #_________________________________


#Criar dicionário com dados digitados pelo usuario
aluno = {
    "nome_aluno": input("Digite o nome do aluno: "),
    "nota1": int(input("Digite a nota 1: ")),
    "nota2": int(input("Digite a nota 2: ")),
    "nota3": int(input("Digite a nota 3: ")),
    "nota4": int(input("Digite a nota 4: ")),
    "nota5": int(input("Digite a nota 5: "))
}

#mostrar o dicionario
print(aluno)

#calcular a média usando as chaves do dicionário
media = (
    aluno["nota1"] +
    aluno["nota2"] +
    aluno["nota3"] +
    aluno["nota4"] +
    aluno["nota5"]
) / 5

#mostrar a média
print("Média:", media)
