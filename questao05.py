'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

a = float(input("Insira um numero: "))
b = float(input("Insira outro numero: "))

soma = a + b
sub1 = a - b
sub2 = b - a
mult = a * b
div = a / b
div_resto = a % b

print(f"Valor da soma dos dois números: {soma}")
print(f"Valor da subtração do primeiro pelo segundo número: {sub1}")
print(f"Valor da subtração do segundo pelo primeiro número: {sub2}")
print(f"Valor da multiplicação dos dois números: {mult}")
print(f"Valor da divisão do primeiro pelo segundo número: {div}")
print(f"Valor do resto da divisão do primeiro pelo segundo número: {div_resto}")