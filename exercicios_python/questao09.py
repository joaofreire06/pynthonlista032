'''
 Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''


idadea = int(input("Informe sua idade em anos: "))
idadem = int(input("Informe sua idade em meses: "))
idaded = int(input("Informe sua idade em dias: "))

#Calculos

id = 365 * idadea
id2 = 30 * idadem
itd = id + id2 + idaded

#Prints

print(f"O valor de sua idade em dias: {itd}")