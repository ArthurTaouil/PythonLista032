'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

custo_produto = float(input("Informe o custo de compra do produto: "))
acrescimo_venda = float(input("Informe o percentual do acréscimo que o produto receberá antes de ser vendido, em decimal (exemplo: se o valor do percentual é 12%, insira 0.12): "))

valor_venda = (custo_produto * acrescimo_venda) + custo_produto

print(f"O valor da venda será de R$ {valor_venda:.2f}")