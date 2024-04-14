def Obter_valor(msg):
    while True:
        try:
            valor = float(input(f'{msg}'))
            return valor
        except ValueError:
            print("Por favor, insira um valor válido.")

def calcular_pagamento_price(financiamento, taxa, tempo):
    taxa = (taxa/ 100) + 0.25/100
    saldo_inicial = financiamento * 1.0038
    valor_parcela = saldo_inicial * (taxa / (1 - (1 + taxa) ** (-tempo)))
    parcelas = []
    for a in range(tempo):
        juros = saldo_inicial * taxa
        amortizacao = valor_parcela - juros
        saldo_devedor = saldo_inicial - amortizacao
        saldo_inicial = saldo_devedor
        parcelas.append(float(valor_parcela))
        juros_total= sum(parcelas) - (financiamento)
    return juros_total

def Metodo_pagamento():
    while True:
        metodo_pagamento = input('Deseja financiar o carro? (sim ou não):')
        if metodo_pagamento in ['sim','não']:
            return metodo_pagamento
        else:
            print("Por favor, escolha uma opção válida: sim ou não")
def Tempo():
    while True:
        tempo = input('Qual é o tempo deseja ficar com o carro? (12, 24, 36 ou 48 meses): ')
        if tempo in ['12', '24', '36', '48']:
            return int(tempo)
        else:
            print("Por favor, escolha um prazo válido: 12, 24, 36 ou 48 meses.")


def Custo_oportunidade(preco,entrada,taxa, tempo):
    capital = preco * entrada
    montante = capital * (1 + taxa) ** (tempo/12)
    rendimento = montante - capital
    if tempo == 12:
        rendimento_liquido = rendimento * (1-(17.5/100))
        return rendimento_liquido
    else:
        rendimento_liquido = rendimento * (1 - (15 / 100))
        return rendimento_liquido

def Manutencao(tempo):
    if tempo == 12:
        ano1 = Obter_valor(msg='Qual é o custo de manutenção durante o primeiro ano? '
                           'lembre-se varia conforme quilometragem: ')
        return ano1
    if tempo == 24:
        pneu = Obter_valor(msg='Qual é o custo do pneu? Se não trocou o custo deve ser 0: ')

        ano1 = Obter_valor(msg='Qual é o custo de manutenção durante o primeiro ano? '
                           'lembre-se varia conforme quilometragem: ')
        ano2 = Obter_valor(msg='Qual é o custo de manutenção durante o segundo ano? ')
        return pneu + ano1 + ano2

    if tempo == 36:
        pneu = Obter_valor(msg='Qual é o custo do pneu? Se não trocou o custo deve ser 0: ')

        ano1 = Obter_valor(msg='Qual é o custo de manutenção durante o primeiro ano? '
                               'lembre-se varia conforme quilometragem: ')
        ano2 = Obter_valor(msg='Qual é o custo de manutenção durante o segundo ano? ')

        ano3 = Obter_valor(msg='Qual é o custo de manutenção durante o terceiro ano? ')

        return pneu + ano1 + ano2 + ano3
    else:
        pneu = Obter_valor(msg='Qual é o custo do pneu? Se não trocou o custo deve ser 0: ')

        ano1 = Obter_valor(msg='Qual é o custo de manutenção durante o primeiro ano? '
                               'lembre-se varia conforme quilometragem: ')
        ano2 = Obter_valor(msg='Qual é o custo de manutenção durante o segundo ano? ')

        ano3 = Obter_valor(msg='Qual é o custo de manutenção durante o terceiro ano? ')

        ano4 = Obter_valor(msg='Qual é o custo de manutenção durante o quarto ano? ')

        return pneu + ano1 + ano2 + ano3 + ano4

def Depreciacao_real(preco, tempo, taxa, ipca):
    tempo = int(tempo / 12)
    depreciacao_real = ( preco * (1 - (((1 + taxa / 100) * (1 + ipca / 100)) -1) *100) ** tempo - preco)
    return depreciacao_real

def Valor_mercado(preco, tempo, taxa):
    valores_mercado = []
    tempo = int(tempo/ 12 )
    for ano in range(1, tempo + 1):
        valor_atual = preco * (1 - taxa) ** (ano - 1)
        valores_mercado.append(valor_atual)

    return valores_mercado

def Seguro(lista):
    taxa = 5.8 /100
    seguro = sum(lista) * taxa
    return seguro

def Imposto (lista,tempo):
    tempo = int(tempo / 12)
    taxa = Obter_valor(msg='Qual é a taxa de IPVA do Estado? ') / 100
    duda = Obter_valor(msg='Qual é o custo do licenciamento anual do Estado? ')
    emplacamento = Obter_valor(msg='Qual é o valor do emplacamento de seu Estado? ')
    duda_primeira = Obter_valor(msg='Qual é o valor do duda de primeira licença de seu Estado? ')
    soma = (taxa * (sum(lista))) + (duda * tempo) + emplacamento + duda_primeira

    return soma

def Reajuste():
    while True:
        reajuste = input('O serviço de assinatura tem reajuste com a inflação? (sim ou não):')
        if reajuste in ['sim','não']:
            return reajuste
        else:
            print("Por favor, escolha uma opção válida: sim ou não")
