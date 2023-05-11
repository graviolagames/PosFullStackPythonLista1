# Crie um código que receba um número digitado pelo usuário e verifique se esse valor é
# positivo, negativo ou igual a zero. A saída deve ser: 
# "Valor Positivo", "Valor Negativo" ou "Igual a Zero".

num = float(input("Digite um número: "))

if num > 0:
    print("Valor Positivo")
elif num < 0:
    print("Valor Negativo")
else:
    print("Igual a Zero")
