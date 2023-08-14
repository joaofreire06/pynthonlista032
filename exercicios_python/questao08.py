'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário
'''
produto = int(input("Informe o preço de custo de um produto: "))
percentual = int(input("Informe o percentual: "))

#Calculos

vt = produto + (produto * percentual/100)

#Prints

print(f"Valor de venda do produto: R${vt:.2f}")
