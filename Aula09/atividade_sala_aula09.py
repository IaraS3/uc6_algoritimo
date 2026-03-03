# O professor digita 5 notas
#Crie uma função que receba as 5 notas de um aluno que calcule e retorne a média
#Crie uma função para receber a média do aluno e retorne se ele está aprovado ou reprovado.
# ________________________________________________________

# Recebe 5 notas
def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    nota5 = float(input("Digite a quinta nota: "))
    
    return (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Verifica aprovação
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Chamar função para calcular média
media_aluno = calcular_media()

# Verificar situação
situacao = verificar_aprovacao(media_aluno)
print("Média:", media_aluno)
print("Situação:", situacao)