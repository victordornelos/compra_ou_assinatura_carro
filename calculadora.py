
from help import formata_float_str_moeda
from  help import calcular_pagamento_price, Metodo_pagamento, Tempo
def Calculadora():
    print('--------------------------------------')
    print('Bem-vindo a calculadora de oportunidade')
    print('--------------------------------------')
    carro = str(input('Qual modelo do carro? '))
    preco_carro = float(input('Qual o preço de compra do carro? '))
    tempo = Tempo()
    metodo_pagamento = Metodo_pagamento()

    if metodo_pagamento == 'sim':
        percentual = float(input('Quantos porcentos de entrada? ')) / 100
        taxa_de_juros = float(input('Quantos valor da taxa de juros em porcentagem? '))
        valor_principal = preco_carro * (1 - percentual)
        juros = calcular_pagamento_price(valor_principal, taxa_de_juros,tempo)
        return juros
    else:
        juros = 0
        return juros



resultado = Calculadora()
print("Resultado:", resultado)






