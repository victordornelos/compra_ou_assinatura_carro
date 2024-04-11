from help import  Obter_valor
from help import Reajuste
def Calculo_assinatura(tempo):
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