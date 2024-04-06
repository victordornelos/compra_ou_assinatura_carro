def formata_float_str_moeda(valor: float)-> str:
    return f'R$ {valor:,.2f}'

def calcular_pagamento_price(financiamento, taxa, tempo):
    taxa = (taxa/ 100) + 0.25/100
    saldo_inicial = financiamento * 1.0038
    valor_parcela = saldo_inicial * (taxa / (1 - ((1 + taxa) ** (-tempo))))
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
        tempo = input('Quanto tempo deseja ficar com o carro? (12, 24, 36 ou 48 meses): ')
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
