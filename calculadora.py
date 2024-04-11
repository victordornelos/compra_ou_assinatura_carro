
from help import formata_float_str_moeda
from  help import calcular_pagamento_price, Metodo_pagamento, Tempo, Custo_oportunidade,Manutencao,Depreciacao_real, Valor_mercado, Seguro, Imposto,Obter_valor
def Calculadora_compra():
    print('--------------------------------------')
    print('Bem-vindo a calculadora de oportunidade')
    print('--------------------------------------')
    carro = str(input('Qual modelo do carro? '))
    preco_carro = Obter_valor(msg='Qual o preço do carro? ')
    tempo = Tempo()
    metodo_pagamento = Metodo_pagamento()
    ipca = 4.5 / 100
    cdi = 11.04 / 100
    tr_real = (((1+cdi/100)/(1+ipca/100))-1)*100 # taxa de retorno real
    taxa_depreciacao = 8 / 100

    if metodo_pagamento == 'sim':

        percentual = Obter_valor(msg='Quanto porcentos de entrada ? ') / 100
        taxa_de_juros = Obter_valor(msg='Quantos valor da taxa de juros em porcentagem? ') / 100
        valor_principal = preco_carro * (1 - percentual)
        juros = calcular_pagamento_price(valor_principal, taxa_de_juros,tempo)

        custo_oportunidade = Custo_oportunidade(preco_carro,percentual,tr_real,tempo)

        manutencao = Manutencao(tempo)

        depreciacao_real = Depreciacao_real(preco_carro,tempo,taxa_depreciacao,ipca)

        valor_mercado = Valor_mercado(preco_carro,tempo,taxa_depreciacao)

        seguro = Seguro(valor_mercado)

        imposto = Imposto(valor_mercado,tempo)

        return juros,custo_oportunidade,manutencao,depreciacao_real, valor_mercado,seguro,imposto,carro,metodo_pagamento

    else:

        juros = 0

        custo_oportunidade = Custo_oportunidade(preco_carro,1,tr_real, tempo)

        manutencao = Manutencao(tempo)

        depreciacao_real = Depreciacao_real(preco_carro, tempo, taxa_depreciacao, ipca)

        seguro = Seguro(valor_mercado)

        imposto = Imposto(valor_mercado,tempo)

        return juros, custo_oportunidade,manutencao,depreciacao_real, seguro, imposto,carro, metodo_pagamento

print(Calculadora_compra())


