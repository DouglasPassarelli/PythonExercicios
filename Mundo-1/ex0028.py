import random
from time import sleep
num = random.randint(0, 5) #Faz o computador pensar
print('=' * 55)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=' * 55)
num1 = int(input('Em que numero eu pensei? ')) #Faz o jogador tentar adivinhar oque o computador pensou
print('Processando...')
sleep(3) #Faz o computador esperar
if num == num1:
    print('Parabens! Voce conseguiu me vencer')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}'.format(num, num1))

