from math import hypot
catetoop = float(input('Informe o comprimento do cateto oposto de um triangulo: '))
catetoad = float(input('Informe o comprimento do cateto adjacente de um triangulo: '))
print('O comprimento da hipotenusa de um triangulo e de {:.2f}'.format(hypot(catetoop, catetoad)))

'''co = float(input('Comprimento do cateto oposto: '))
ca =  float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
