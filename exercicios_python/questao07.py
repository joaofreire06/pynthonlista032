'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

valor_compra = float(input("Informe valor total da compra: "))
num_prestacoes = float(input("Qual o numero de prestações da compra ?"))

valor_prestacoes = valor_compra / num_prestacoes

print(f"O valor de cada uma das {num_prestacoes:.0f} será de R$ {valor_prestacoes:.2f}")