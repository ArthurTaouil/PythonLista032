'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

valorcompra = float(input("Informe o valor total da compra: "))
numprestacoes = float(input("Qual o número de prestações da compra? "))

valor_prestacoes = valorcompra / numprestacoes

print(f"O valor de cada uma das {numprestacoes:.0f} será de R$ {valor_prestacoes:.2f}")