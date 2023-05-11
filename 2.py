
# Crie a solução para a seguinte situação:
# “Registre um conjunto de 5 de temperaturas, e informe ao final:
# a menor temperaturas das informadas,
# a média das temperaturas que forem maiores que 0 e menores que 20, e;
# a quantidade de temperaturas negativas e positivas”
# ATENÇÃO! NÃO É UM VETOR! Pode usar se souber.
# Valores de entrada: 10.12, -3.55, -10.55, 11.44 , 22.22.
# Saídas:
#  A menor temperatura é -10.55.
#  A média das temperaturas entre 0 e 20 é 10,78
#  São 2 temperaturas negativas e 3 positivas.


#Usa uma lista para armazenar as temperaturas:
temp = [10.12, -3.55, -10.55, 11.44, 22.22]

lower_temp = temp[0]
temp_btw_0_20 = []
negative_temp = []
positive_temp = []

for t in temp:
    if t < lower_temp:
        lower_temp = t
    if t <  0:
        negative_temp.append(t)
    else:
        positive_temp.append(t)
        if t < 20:
            temp_btw_0_20.append(t)
print(f"A menor temperatura é: {lower_temp}")
len_btw_0_20 = len(temp_btw_0_20)
if len_btw_0_20 == 0:
    print("Não há temperaturas entre 0 e 20 graus.")
else:
    mean = sum(temp_btw_0_20)/len_btw_0_20
    print(f"A média das temperaturas entre 0 e 20 é: {mean}")

print("São", len(negative_temp), "temperaturas negativas e", len(positive_temp), "positivas.")
