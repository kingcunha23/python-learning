# -*- coding: utf-8 -*-

n = int(input('Digite um número inteiro: '))
i = 0
algarismo = 0
soma = 0

while i < (n // 10 ** (i - 1)):
    
    algarismo = (n // 10 ** i) % 10
    i = i + 1
    soma = soma + algarismo

print(soma)