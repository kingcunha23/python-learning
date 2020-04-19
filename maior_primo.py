# -*- coding: utf-8 -*-

def éprimo(k):
    divisor = 2
    primo = True
    resto = k % divisor
    while divisor < k and primo :
          if resto == 0:
           primo = False
          resto = k % divisor
          divisor = divisor + 1 
          if primo == True:
           return k
