# Crie um código que pergunte ao usuário seu nome e sua idade. Em seguida verifique se a
# idade é maior ou menor que 18, exiba da seguinte forma: Fulano é maior de 18 e tem XX Anos ou Fulano
# não é maior de 18 e tem XX Anos.

name = input("Digite o seu nome: ")
age = int(input("Digite a sua idade: "))

if age >= 18:
    print(f"{name} é maior de 18 e tem {age} anos.")
else:
    print(f"{name} é menor de 18 e tem {age} anos.")

