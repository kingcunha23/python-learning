# -*- coding: utf-8 -*-

n = int(input('Digite um número inteiro: '))
divisor = 2
primo = True
resto = n % divisor

while divisor < n and primo :
    
      if resto == 0:
          primo = False
      resto = n % divisor
      divisor = divisor + 1
      
      
if primo:
          
          print('primo')
          
else:
          
          print('não primo')