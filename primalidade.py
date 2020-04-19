# -*- coding: utf-8 -*-

def is_primo(n = ""):
    if (n == ""):
        n = int(input('Digite um valor inteiro: '))
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
    return is_primo()

is_primo()
