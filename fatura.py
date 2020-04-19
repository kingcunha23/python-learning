# -*- coding: utf-8 -*-

x = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = int(x / 86400)
hora = int((x % 86400) / 3600)
minuto = int(((x % 86400) % 3600) / 60)
segundos = int((((x % 86400) % 3600) % 60)

print(dia,'dias,',hora,'horas,',minuto,'minutos,',segundos,'segundos.')