#Bixar a extensao View para abrir as colunas


import pandas as pd # O pd e um apelido que damos para a biblioteca , podemos chamar o apelido no codigo , inves de digitar pandas

nome = str(input(f"Digite seu nome: "))
idade = str(input(f"Digite sua idade: "))  #usamos a idade comoum texto , porque nao vamos fazer calculos matematicos
altura = float(input("Digite sua altura: "))
#Dicionario , para o diferencia ro dicionario de uma lista é dicionarios usamos {} e lista usamos []
#Criação de um dicionario para receber os dados digitados pelo usuario

dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}
#DataFrame e a criação de um excel no formato que o Pandas entende para trabalhar com dados
excel = pd.DataFrame(dados)

# to _excel() > serve para criar uma nova planilhas , pegar os dados digitados pelo usuario em formato DataFrame e gravar na planilha criada

# excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)

# Loc / Numero da linha / coluna
# Ler o Excel
leitura_excel = pd.read_excel("Aula12\cadastro_aluno.xlsx")
nova_linha = len(leitura_excel) #conta quantas linhas tem no excel e cria novas linhas conforme necessidade.

leitura_excel.loc[nova_linha,"nome"] = dados["nome"]
leitura_excel.loc[nova_linha,"idade"] = dados["idade"]
leitura_excel.loc[nova_linha,"altura"] = dados["altura"]

leitura_excel.to_excel("Aula12\cadastro_aluno.xlsx", index=False)