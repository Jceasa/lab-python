# Verifique se "Python" e "python" são iguais. Depois converta uma string para maiúscula.

word1 = "Python"
word2 = "python"

result = True if word1 == word2 else False

print(f"São iguais: {result}")

word_capital = word1.upper()

print(f"Capital: {word_capital}")