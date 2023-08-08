'''
 Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetro
'''

peso = float(input("Qual seu peso ?"))
alt = float(input("Qual sua altura ?"))
gramas = peso * 1000
cent = alt * 100

print("Seu peso em gramas é",gramas,"e sua altura em cm é",cent)