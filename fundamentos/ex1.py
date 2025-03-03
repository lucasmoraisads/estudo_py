# # Primeiro exercicio
# nome = input("Digite seu nome: ")
# sobreNome = input("Digite seu sobre nome: ")

# nomeCompleto = (f"{nome} {sobreNome}")

# print(nomeCompleto)

# exercicio 2

# texto = "Python e muito interresante para aprender"
# palavra = texto.split()
# textoInvertido = " ".join(palavra[::-1])
# print(textoInvertido)

# exercicio 3

texto1 = "arara"
texto2 = "python"

#remover espaço em brabco
texto1Format = texto1.lower().replace(" ", "")
texto2Format = texto2.lower().replace(" ", "")

# verifica de o texto original e igual ao reverso

palindromo = texto1Format == texto1[::-1]
palindromo2 = texto2Format == texto2[::-1]

print(palindromo)
print(palindromo2)
