nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

with open("cadastros.txt", "a") as adicionar_novo_texto:
    adicionar_novo_texto.write(nome + " - " + idade + "\n")