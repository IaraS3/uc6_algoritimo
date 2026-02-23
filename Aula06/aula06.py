""" para que apareça somente determinados caracteres de um texto cada caractere é considerado um numeral sempre iniciando por 0 exemplo
SENAC
01234
"""
texto = "SENAC"
print(texto[0])
print(texto[3])
print(texto[-1])
 
"""
Caso eu coloque -numeral ele vem do final para o primeiro
"""

# FUNCAO len() : serve para contar todos os caracteres de uma vez.
texto2="Olá"
print(len(texto2))

# FUNCAO MAI/MIN
texto3="Olá mundinho"
print(texto3.upper())

texto4= "OLA MUNDAO"
print(texto4.lower())

print(texto3.capitalize())

print(texto3.title())

texto5= "Python"
"""
PYTHON
012345  ---IGNORA O ULTIMO QUE TA CHAMANDO, POR ISSO MARCA O ANTEPENULTIMO DA NUMERAÇAO
"""
print(texto5[0:3])
print(texto5[0:4])
print(texto5[0:5])

# REPLACE
texto6= "Hoje é aula da Heloisa"
novo_texto= texto6.replace("da Heloisa", "do Miltinho")
print(novo_texto)

# ESPACO EM BRANCO
texto7 = " Olá Mundo "
print(texto7.strip()) #Remove espaço da direita e esquerda.
print(texto7.lstrip()) #Remove espaço da esquerda.
print(texto7.rstrip()) #Remove espaço da direita.

#________________________________________________________________
# METODO EM STRINGS
# Case sensitive = Sensivel a letras maiusculas e minuscula
texto8 = "Pulei carnaval, mas hoje estou estudando."
print("carnaval" in texto8)

# FIND
# Case sensitive = Sensivel a letras maiusculas e minuscula
print(texto8.find("estudando")) # 31
print(texto8[31]) # e

# COUNT
# Case sensitive = Sensivel a letras maiusculas e minuscula
print(texto8.count("a"))

# START / END - SWITH
# Case sensitive = Sensivel a letras maiusculas e minuscula
texto9 = "Eu amo Java"
print(texto9.startswith("Eu"))
print(texto9.endswith("va"))