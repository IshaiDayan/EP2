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

navios_pc = constantes.PAISES[escolhadopc]
lista_blocos_pc = []
for tipo,qtd in navios_pc.items():
    for i in range(qtd):
        lista_blocos_pc.append(constantes.CONFIGURACAO[tipo])

mapapc = funcoes_auxilio.aloca_navios(mapapc,lista_blocos_pc)

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
time.sleep(1)


navios_jg = constantes.PAISES[escolhadojg]
lista_blocos_jg = []

for tipo,qtd in navios_jg.items():
    for i in range(qtd):
        lista_blocos_pc.append(constantes.CONFIGURACAO[tipo])

        print("Alocar: {0} ({1} blocos)".format(tipo,constantes.CONFIGURACAO[tipo]))

        pode = False
        while pode == False:
            letra = input("Informe a Letra:")
            linha = int(input("Informe a Linha:"))-1
            ori = input("Informe a Orientação:")
            pode = funcoes_auxilio.posicao_suporta(mapajg,constantes.CONFIGURACAO[tipo],linha,int(ord(letra)-ord("A")),ori)
            if not pode:
                print("Local Inválido. Tente novamente")

        mapajg = funcoes_auxilio.aloca_navio_jogador(mapajg,constantes.CONFIGURACAO[tipo],linha,int(ord(letra)-ord("A")),ori)
        print("Navio alocado!")
        funcoes_auxilio.printar_mapas(mapapc,mapajg)
time.sleep(2)
print("Iniciando a Batalha Naval!")
time.sleep(1)
print("Prepare-se...")
time.sleep(2)

comeca = random.choice(["pc","jg"])

funcionando = True
while funcionando == True:
    mapa_pc,mapa_jg,funcionando = funcoes_auxilio.rodada(comeca,mapapc,mapajg,funcionando)
    funcoes_auxilio.printar_mapas(mapapc,mapajg)

print('acabou')
    
        


