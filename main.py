from calculadora_compra import Calculadora_compra
from calculadora_assinatura import Calculo_assinatura
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("dark_background")


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
    saldo = (df['Preço do carro'].values[0] - df['Assinatura'].values[0]) - (
                df['Preço do carro'].values[0] - df['Juros'].values[0] - df['Seguro'].values[0] +
                df['Depreciação real'].values[0] - df['Manutenção'].values[0] - df['Custo de oportunidade'].values[0] -
                df['Impostos'].values[0])
    modulo_saldo = abs(saldo)

    if saldo < 0:
        print('Obrigado por todas informações!')
        print('Calculando o resultando')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        print(f'A melhor opção é comprar o {df['Carro'].values[0]}, com uma economia de  R$ {modulo_saldo:,.2f}')
        print('Este gráfico pode ajudar em perceber quais são os principais custos')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')

        df2 = {'Custos': ['Preço do carro', 'Seguro', 'Depreciação real', 'Manutenção', 'Custo de oportunidade',
                          'Impostos', 'Juros', 'Assinatura'],
               'Valor': [df['Preço do carro'].values[0], df['Seguro'].values[0], abs(df['Depreciação real'].values[0]),
                         df['Manutenção'].values[0], df['Custo de oportunidade'].values[0], df['Impostos'].values[0],
                         df['Juros'].values[0], df['Assinatura'].values[0]]}

        ns.barplot(data=df2, x='Custos', y='Valor', palette='Reds')
        plt.ylabel('R$')
        plt.title(f'Comparativo dos custos do {carro}')
        plt.grid(False)
        plt.show()

        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        print('Obrigado!')
        print('Volte sempre')

    else:
        print('Obrigado por todas informações!')
        print('Calculando o resultando')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        print(f'A melhor opção é assinar o {df['Carro'].values[0]}, com uma economia de R$ {modulo_saldo:,.2f}')
        print('Este gráfico pode ajudar em perceber quais são os principais custos')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')

        df2 = {'Custos': ['Preço do carro', 'Seguro', 'Depreciação real', 'Manutenção', 'Custo de oportunidade',
                          'Impostos', 'Juros', 'Assinatura'],
               'Valor': [df['Preço do carro'].values[0], df['Seguro'].values[0], abs(df['Depreciação real'].values[0]),
                         df['Manutenção'].values[0], df['Custo de oportunidade'].values[0], df['Impostos'].values[0],
                         df['Juros'].values[0], df['Assinatura'].values[0]]}


        sns.barplot(data=df2, x='Custos', y='Valor', palette='Reds')

        plt.ylabel('R$')
        plt.title(f'Comparativo dos custos do {carro}')
        plt.grid(False)
        plt.show()

        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        print('Obrigado!')
        print('Volte sempre')


if __name__ == '__main__':
    main()
