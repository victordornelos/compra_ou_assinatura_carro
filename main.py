from calculadora_compra import Calculadora_compra
from calculadora_assinatura import Calculo_assinatura
import pandas as pd
def main():
    juros, custo_oportunidade, manutencao, depreciacao_real, valor_mercado, seguro, imposto, carro, metodo_pagamento, preco_carro, tempo = Calculadora_compra()

    valor_assinatura = Calculo_assinatura(tempo)
    data = {
        'Carro': [carro],
        'Preco do carro': [preco_carro],
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
    print(df)


if __name__ =='__main__':
    main()