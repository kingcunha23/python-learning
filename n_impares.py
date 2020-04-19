# -*- coding: utf-8 -*-

n = int(input('Digite um número inteiro: '))
i = 0
y = (n // 10 ** i ) % 10
j = 0
while y != 0:
    
    y = (n // 10 ** i ) % 10
    i = i + 1
    j = j + y

print(j)