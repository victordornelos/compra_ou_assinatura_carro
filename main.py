from calculadora_compra import Calculadora_compra
from calculadora_assinatura import Calculo_assinatura
from help import formata_float_str_moeda
import pandas as pd
def main():
    juros, custo_oportunidade, manutencao, depreciacao_real, valor_mercado, seguro, imposto, carro, metodo_pagamento, preco_carro, tempo = Calculadora_compra()

    valor_assinatura = Calculo_assinatura(tempo)

    data = {
        'Carro': [carro],
        'Preço do carro': [preco_carro],
        'Tempo': [tempo],
        'Seguro': [seguro],
        'Depreciação real': [depreciacao_real],
        'Manutenção': [manutencao],
        'Custo de oportunidade': [custo_oportunidade],
        'Impostos': [imposto],
        'Método de pagamento': [metodo_pagamento],
        'Juros': [juros],
        'Assinatura': [valor_assinatura]
    }
    df = pd.DataFrame(data)
    print(df['Preço do carro'])
    saldo = (df['Preço do carro'] - df['Assinatura']) - (df['Preço do carro'] - df['Juros'] - df['Seguro'] + df['Depreciação real'] - df['Manutenção'] - df['Custo de oportunidade'] - df['Impostos'])
    modulo_saldo = abs(saldo)
    print(saldo)

    if saldo < 0:
        print(f'A melhor opção é comprar o {df['Carro']}, com uma economia de  R$ {modulo_saldo}')
    else:
        print(f'A melhor opção é assinar o {df['Carro']}, com uma economia de R$ {saldo}')



if __name__ =='__main__':
    main()