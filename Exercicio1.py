
# Crie a solução em para a seguinte situação:
# ATENÇÃO! NÃO É UM VETOR! Pode usar se souber.
# “Utilizando um laço de repetição que irá percorrer os valores de 1 até 12 representando os meses do
# ano, realize a soma de todos os valores que forem menores que o mês atual, informe também qual
# o próximo mês e verificar se o mês atual é par ou impar”.
# Valores de entrada: 1,2,3,4,5,6,7,8,9,10,11,12
# Mês atual: 6
# Saídas:
# A soma dos valores menores que o mês atual é igual a 15.
# O próximo mês é 7.
# O mês atual é par

current_month = 6
sum = 0

#Considera cada mês do ano
for month in range (1,13):
        if month < current_month:
            sum += month

#Imprima os resultados
print(f"A soma dos valores menores que o mês atual é igual a {sum}.")
print(f"O próximo mês é {current_month + 1}.")
print("O mês atual é", "par" if current_month % 2 == 0 else "impar", ".")