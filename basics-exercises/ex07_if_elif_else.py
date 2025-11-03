# Leia uma nota (0-100) e imprima: "Aprovado" (>=70), "Recuperação" (50-69), "Reprovado" (<50).

nota = 100

if nota >= 70:
    print("Aprovado")
elif nota >= 50 and nota <= 69:
    print("Recuperação")
elif nota < 50:
    print("Reprovado")