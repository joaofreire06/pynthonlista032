'''
 Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''
nome = input("Qual seu nome?")
sal_fixo = int(input("Seu salário fixo :"))
vendas = int(input("Quantas vendas você fez?"))
comi = (vendas + vendas / 100 * 15)
sal_com = sal_fixo + comi

print(nome,"seu salario fixo",sal_fixo,"sua comissão é",comi,"seu salario mais comissão",sal_com,)


