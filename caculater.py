operacao = input("Digite a operacao desejada (soma, sub, mult, div, exp): ")
numero1 = float(input("Digite o primeiro número: "))  # Use float para permitir números decimais
numero2 = float(input("Digite o segundo número: "))  # Use float para permitir números decimais

if operacao == "soma":
    resultado = numero1 + numero2
elif operacao == "sub":
    resultado = numero1 - numero2
elif operacao == "mult":
    resultado = numero1 * numero2
elif operacao == "div":
    resultado = numero1 / numero2
elif operacao == "exp":
    resultado = numero1 ** numero2
else:
    resultado = "Operação não suportada"

print("O resultado da operação é:", resultado)