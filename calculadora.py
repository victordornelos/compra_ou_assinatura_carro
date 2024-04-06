
from help import formata_float_str_moeda
from  help import calcular_pagamento_price, Metodo_pagamento, Tempo, Custo_oportunidade
def Calculadora():

    print('--------------------------------------')
    print('Bem-vindo a calculadora de oportunidade')
    print('--------------------------------------')
    carro = str(input('Qual modelo do carro? '))
    preco_carro = float(input('Qual o preço de compra do carro? '))
    tempo = Tempo()
    metodo_pagamento = Metodo_pagamento()
    ipca = 4.5 / 100
    cdi = 11.04 / 100
    tr_real = (((1+cdi/100)/(1+ipca/100))-1)*100 # taxa de retorno real
    taxa_depreciacao = 8 / 100

    if metodo_pagamento == 'sim':

        percentual = float(input('Quantos porcentos de entrada? ')) / 100
        taxa_de_juros = float(input('Quantos valor da taxa de juros em porcentagem? '))
        valor_principal = preco_carro * (1 - percentual)
        juros = calcular_pagamento_price(valor_principal, taxa_de_juros,tempo)
        custo_oportunidade = Custo_oportunidade(preco_carro,percentual,tr_real,tempo)
        return juros,custo_oportunidade

    else:
        juros = 0
        custo_oportunidade = Custo_oportunidade(preco_carro,1,tr_real, tempo)
        return juros, custo_oportunidade


resultado = Calculadora()
print("Resultado:", resultado)






