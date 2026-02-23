# Operadores aritmeticas

"""
Sempre apresentar o resultado após cada etapa finalizada
"""

# somar 3 nmeros
num = 12
num2 = 20
num3 = 300
resultado_soma = (num+num2+num3)

# após somar 3 numeros vamos subtrair 15
subtração = 15
resultado_subtração = (resultado_soma - subtração)


# após a etapa acima, vamor multiplicar o resultado por 8
multiplicar_por = 8
resultado_multiplicação = (resultado_subtração * multiplicar_por)


# em seguida dividir o resultado por 100
divisor = 100
resultado_final = (resultado_multiplicação / divisor)

print("A soma dos 3 números é", str (resultado_soma))

print("Subtraindo 15 , o resultado é", str (resultado_subtração))

print("Multiplicando por 8 , o resultado é",str (resultado_multiplicação))

print("Dividindo por 100 , o resultado é", str(resultado_final))

# ou para usa a variavel aso ocorra mudança nos dados
print("A soma dos números é", str (resultado_soma))

print("Subtraindo", str (resultado_subtração) , "o resultado é", str (resultado_subtração))

print("Multiplicando por", str (multiplicar_por) , "o resultado é",str (resultado_multiplicação))

print("Dividindo por", str (divisor) ," o resultado é", str(resultado_final))

#___________________________________________________________________________

# queremos somar 3 numeros

print(20 + 10 + 30) #60
# após somar 3 números , vamos subtrair 15

print(20 + 20 - 15)
# após a etapa acima , vamos multiplicar o resultado por 8
print(30 + 10 - 15 * 8)

# em seguida dividir o resultado por 100
print(30 + 10 - 15 * 8 / 100)

"""
5 == 2 #false
 
5 == 5 #true
 
5 === "5" #
int   srting
"""

print(5 == 3) #false

print(5 == 8) #false

print(89 >= 45) #true
#maior ou igual

print(564 <= 235) #false
#menor ou igual

print(456 <= 456 or 12 == 12)#true

print()

# tem cracha = FALSE
#        E / and       ===FALSE 
# tem blusa = TRUE
#AS DUAS COMPARAÇÕESPRECISAM RETORNAR VERDADE, PARA QUE O RESULTADO SEJA VERDADE

#******************************

# tem cracha = FALSE
#        OU / or        ===VERDADEIRO
# tem blusa = TRUE
#APENAS UMA DAS COMPARAÇÕES PRECISAM RETORNAR VERDADEIRO, PARA QUE O RESULTADO FINAL TAMBEM SEJA VERDADEIRO.

##VERDADEIRO AND VERDADEIRO != FALSE
##VERDADEIRO AND FALSE != TRUE