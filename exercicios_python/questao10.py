'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''
te = int(input("Informe o total de eleitores do município: "))
vb = int(input("Informe o total de votos brancos do município: "))
vn = int(input("Informe o total de votos nulos do município: "))
vv = int(input("Informe o total de votos validos do município: "))

#Cálculos

percentual_brancos = (vb / te) * 100
percentual_nulos = (vn / te) * 100
percentual_validos = (vv / te) * 100

#Prints
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")