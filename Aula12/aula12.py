import pandas as pd  # O pd é um apelido que damos para a biblioteca, podemos chamar o apelido no código, em vez de digitar pandas

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")  # usamos a idade como texto, pois não faremos cálculos matemáticos
altura = float(input("Digite sua altura: "))

# Criação de um dicionário para receber os dados digitados pelo usuário
dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}

# DataFrame é a criação de uma tabela que o Pandas entende para trabalhar com dados
excel = pd.DataFrame(dados)

# Ler o Excel existente
leitura_excel = pd.read_excel("Aula12/cadastro_alunos.xlsx")  # Ajustei o nome do arquivo para consistente
nova_linha = len(leitura_excel)  # Conta quantas linhas tem no Excel e cria novas linhas conforme necessidade

# Adicionar os novos dados na nova linha
leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

# Salvar de volta no Excel
leitura_excel.to_excel("Aula12/cadastro_alunos.xlsx", index=False)