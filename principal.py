import constantes
from random import choice
import random
import time
import funcoes_auxilio

escolhadopc = random.choice(list(constantes.PAISES.keys()))

print("Iniciando o Jogo!")
time.sleep(3)
print("O computador está alocando os navios de guerra do país {0}".format(escolhadopc))
time.sleep(2)
mapapc = funcoes_auxilio.cria_mapa(10)
mapapc = funcoes_auxilio.aloca_navios(mapapc,list(constantes.PAISES[escolhadopc].values()))
mapajg = funcoes_auxilio.cria_mapa(10)
#funcoes_auxilio.printar_mapas(mapapc,mapajg)
print("O computador já está em posição de batalha!")
time.sleep(2)
for w in constantes.PAISES:
    print(" ")
    print ("\u001b[32m","  "+w,"\u001b[0m")
    
    for q in constantes.PAISES[w]:
        espacos = " "*(12-len(q))
        print (q+espacos,':',constantes.PAISES[w][q])

escolhadojg = input("Qual a nação da sua frota?")
print("Você escolheu o país {0}".format(escolhadojg))
print("Agora é sua vez de alocar seus navios de guerra!")
time.sleep(1)
funcoes_auxilio.printar_mapas(mapapc,mapajg)
