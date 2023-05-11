# Crie um código que solicite a entrada de um número de meses que a pessoa deseja fazer
# controle alimentar e quantos quilos ela deseja perder e imprima a tabela de peso projetado perdidos mês
# a mês para visualização da pessoa:
# Exemplo: Caso o usuário informe que deseja emagrecer em 3 meses, sendo 12kg que ele busca emagrecer
# (informado acima), ou seja, iremos imprimir 3 linhas de 4KG.
# Mês 1 você irá perder 4KG
# Mês 2 você irá perder 4KG
# Mês 3 você irá perder 4KG
# Saídas:
# Número de meses com valor correto do valor de quilos.

months = int(input("Digite o número de meses que deseja fazer controle alimentar: "))
kgms = int(input("Digite quantos quilos deseja perder: "))

if months<= 0 or kgms <= 0:
    print("Valor inválido para meses ou quilos. Tente novamente.")
else:
    kgm_by_month = kgms / months
    for month in range(1, months+1):
        print(f"Mês {month} você irá perder {kgm_by_month:.2f}KG")
