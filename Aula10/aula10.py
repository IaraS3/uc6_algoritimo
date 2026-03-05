#Abrir arquivo
# open("nota.txt", "w")

#Abrir um arquivo e Digitar informacoes (w - de WRITE)
with open("nota.txt", "w") as nota_aluno:
    nota_aluno.write("Ola galera")

#Ler um arquivo e mostrar no terminal
with open("nota.txt", "r") as leitura_arquivo:
    recebe_texto = leitura_arquivo.read()
    print(recebe_texto)

# ("a"-de append) Adicionar um texto ao final do seu arquivo
with open("nota.txt", "a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto")
