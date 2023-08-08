'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

pesokg = float(input("Quanto você pesa, em quilos? "))
alturam = float(input("Qual é a sua altura, em metros? "))

pesog = pesokg * 1000
alturacm = alturam * 100

print(f"Seu peso, em gramas, é equivalente a {pesog:.0f} e a sua altura, em centímetros, é equivalente a {alturacm:.0f}")