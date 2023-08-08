'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como a resposta o valor com o
acréscimo dos 10% da gorjeta do garçom
'''

conta = float(input("Qual foi o valor da conta? "))
acrescimo = (conta * 0.1) + conta

print(f"O valor da conta com a gorjeta de 10% do garçom foi de R$ {acrescimo}")