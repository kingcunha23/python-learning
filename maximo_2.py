# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:19:32 2020

@author: jpcun
"""
n = 1
k = int(input('Número: '))
i = 2
l = 0
primo = True

while i < k and primo:
    if n == 0:
        primo = False
    n = k % i
    i = i + 1
    

if primo == True:
    print('primo')
else:
    print('não primo')