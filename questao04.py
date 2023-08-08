'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''
import math

peso = float(input("Quanto você pesa, em quilos? "))
altura = float(input("Qual é a sua altura, em metros? "))

imc = peso / math.pow(altura,2)

print(f"Seu IMC é {imc:.2f}")