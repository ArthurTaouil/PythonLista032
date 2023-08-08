'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia
'''

horas = int(input("Informe as horas atuais: "))
minutos = int(input("Informe os minutos atuais: "))

horasmin = horas * 60
minstotal = horasmin + minutos

print(f"Horas e minutos atuais: {horas}:{minutos}h")
print(f"Se passaram {minstotal} minutos desde Meia-Noite")
