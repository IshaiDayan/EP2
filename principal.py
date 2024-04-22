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
# alocar navios do comp
print("O computador já está em posição de batalha!")
time.sleep(1)
for w in constantes.PAISES:
    print (w)
    for q in constantes.PAISES[w]:
        print (q,':',constantes.PAISES[w][q])
input("Qual a nação da sua frota?")

mapapc = funcoes_auxilio.cria_mapa(10)
mapajg = funcoes_auxilio.cria_mapa(10)

funcoes_auxilio.printar_mapas(mapapc,mapajg)
