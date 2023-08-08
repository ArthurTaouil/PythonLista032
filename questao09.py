'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias
'''

idade_anos = int(input("Quantos anos de idade você tem? "))
idade_meses = int(input("Quantos meses de idade você tem? "))
idade_dias = int(input("Quantos dias de idade você tem? "))

idade_dias_total = (idade_anos * 365) + (idade_meses * 30) + (idade_dias * 1)

print(f"Você tem {idade_anos} anos, {idade_meses} meses e {idade_dias} de idade.")
print(f"Apenas em dias, você tem {idade_dias_total} dias de idade.")