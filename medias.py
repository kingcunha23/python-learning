# -*- coding: utf-8 -*-

nome = input('Digite o nome do cliente: ')
vencimento = int(input('Digite o dia de vencimento: '))
mes = input('Digite o mês de vencimento: ')
fatura = float(input('Digite o valor da fatura: '))

print('Olá,',nome)
print('A sua fatura com vencimento em',vencimento,'de',mes,'no valor de R$ %.2f está fechada.' % fatura)