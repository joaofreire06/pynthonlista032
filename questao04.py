'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros
'''
import math

peso = float(input("Seu peso :"))
alt = float(input("Sua altura"))


imc = peso / math.pow(alt,2)
print("Valor da massa corporal",imc)