# -*- coding: utf-8 -*-

xa = float(input('Digite a cordenada x do ponto a: '))
ya = float(input('Digite a cordenada y do ponto a: '))
xb = float(input('Digite a cordenada x do ponto b: '))
yb = float(input('Digite a cordenada y do ponto b: '))

d = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

if d >= 10 :
    
    print('longe')
    
else:
    
    print('perto')