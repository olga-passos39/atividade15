# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)