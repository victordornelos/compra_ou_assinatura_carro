
from help import formata_float_str_moeda
from  help import calcular_pagamento_price, Metodo_pagamento, Tempo, Custo_oportunidade,Manutencao,Depreciacao_real, Valor_mercado, Seguro, Imposto,Obter_valor, Reajuste
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

        return juros,custo_oportunidade,manutencao,depreciacao_real, valor_mercado,seguro,imposto,carro,metodo_pagamento,preco_carro,tempo

    else:

        juros = 0

        custo_oportunidade = Custo_oportunidade(preco_carro,1,tr_real, tempo)

        manutencao = Manutencao(tempo)

        depreciacao_real = Depreciacao_real(preco_carro, tempo, taxa_depreciacao, ipca)

        seguro = Seguro(valor_mercado)

        imposto = Imposto(valor_mercado,tempo)

        return juros, custo_oportunidade,manutencao,depreciacao_real, seguro, imposto,carro, metodo_pagamento,preco_carro,tempo

resultado_compra = Calculadora_compra()
def Calculo_assinatura():
    tempo = resultado_compra[-1]
    assinatura = Obter_valor(msg='Qual o valor da mensalidade da assinatura? ')
    reajuste = Reajuste()
    ipca = 4.5 / 100

    if reajuste == 'sim':
        if tempo == 12:
            ano1 = assinatura * 12
            return ano1

        if reajuste == 24:
            ano1 = assinatura * 12
            ano2 = (assinatura + (1 + ipca)**1) * 12
            return  ano1 + ano2

        if reajuste == 36:
            ano1 = assinatura * 12
            ano2 = (assinatura + (1 + ipca)**1) * 12
            ano3 = (assinatura + (1 + ipca)**2 ) * 12
            return ano1 + ano2 + ano3

        if reajuste == 48:
            ano1 = assinatura * 12
            ano2 = (assinatura + (1 + ipca) ** 1) * 12
            ano3 = (assinatura + (1 + ipca) ** 2) * 12
            ano4 = (assinatura + (1 + ipca) ** 3) * 12
            return ano1 + ano2 + ano3 + ano4

    else:
        return assinatura * tempo
juros, custo_oportunidade, manutencao, depreciacao_real, valor_mercado, seguro, imposto, carro, metodo_pagamento, preco_carro, tempo = Calculadora_compra()

data = {
    'juros': [juros],
    'custo_oportunidade': [custo_oportunidade],
    'manutencao': [manutencao],
    'depreciacao_real': [depreciacao_real],
    'valor_mercado': [valor_mercado],
    'seguro': [seguro],
    'imposto': [imposto],
    'carro': [carro],
    'metodo_pagamento': [metodo_pagamento],
    'preco_carro': [preco_carro],
    'tempo': [tempo]
}

def Saldo():


resultado =
dados = {'Carro':}


