'''
 Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

nome = input("Informe seu nome: ")
salario = float(input("Informe seu salário: "))
vendas = float(input("Informe o total de vendas efetuadas por você no mês, em dinheiro: "))

comissao = vendas * 0.15
salario_comp = comissao + salario

print(f"Seu nome: {nome}")
print(f"Seu salário fixo: R$ {salario:.2f}")
print(f"Valor da sua comissão: R$ {comissao:.2f}")
print(f"Seu salário completo (ou seja, salário fixo mais a comissão sobre vendas) é de: R$ {salario_comp:.2f}")






