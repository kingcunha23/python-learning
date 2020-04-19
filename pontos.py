# -*- coding: utf-8 -*-

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c

raiz1 = (- b + delta ** 0.5) / (2 * a)
raiz2 = (- b - delta ** 0.5) / (2 * a)

if delta > 0 and raiz1 > raiz2 :
    
    print('as raízes da equação são',raiz2,'e',raiz1)

else:
    
    if delta > 0 and raiz2 > raiz1 :
        
        print('as raízes da equação são',raiz1,'e',raiz2)
        
    else:
        
        if delta == 0 :
            
            print('a raiz desta equação é',raiz1)
            
        else:
            
            print('esta equação não possui raízes reais')