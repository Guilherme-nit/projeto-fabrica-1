nome = input("Digite o nome do aluno:")

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

Nota = (nota1 + nota2 + nota3+ nota4) / 4

if Nota >= 7.0:
    print("Aprovado!")
elif Nota >= 5.0 and Nota < 7.0:
    print("Recuperação!")
else:
    print("Reprovado!")

print(Nota)