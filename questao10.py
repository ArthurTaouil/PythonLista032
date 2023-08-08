'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

eleitores = float(input("Qual o total de eleitores? "))
votos_brancos = float(input("Quantos votos brancos tiveram? "))
votos_nulos = float(input("Quantos votos nulos tiveram? "))
votos_validos = float(input("Quantos votos válidos tiveram? "))

percentual_votos_brancos = ([eleitores - votos_nulos - votos_validos] / eleitores) * 100




print(percentual_votos_brancos)