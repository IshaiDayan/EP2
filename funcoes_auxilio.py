import random
import constantes

def cria_mapa(N):
    matriz = []
    for x in range(N):
       matriz.append([' ']*(N))
    return matriz

def posicao_suporta(mapa,blocos,linha,coluna,vh):
    if vh == "h":
        if (coluna)+blocos > len(mapa[linha]):
            return False
    else:
        if (linha)+blocos > len(mapa):
            return False

    for i in range(blocos):
        if vh == "h":
            if mapa[linha][coluna+i] == "N":
                return False
        else:
            if mapa[linha+i][coluna] == "N":
                return False
    
    return True

def aloca_navios(mapa,listablocos):
    for i in range(len(listablocos)):

        pode = False
        while pode == False:
            linha = random.randint(0, (len(mapa)-1))
            coluna = random.randint(0, (len(mapa)-1))
            orientacao = random.choice(['h', 'v'])
            pode = posicao_suporta(mapa,listablocos[i],linha,coluna,orientacao)

        mapa = aloca_navio_jogador(mapa,listablocos[i],linha,coluna,orientacao)

    return mapa

def aloca_navio_jogador(mapa,navio,linha,coluna,orientacao):
    for x in range(navio):
        if orientacao == "h":
            mapa[linha][coluna+x] = "N"
        else:
            mapa[linha+x][coluna] = "N"
    return mapa

def foi_derrotado(matriz):
    for z in matriz:
        for j in z:
            if j == "N":
                return False
    return True



def printar_mapas(matriz_pc,matriz_jg):
    print("           Mapa do Computador                                  Seu Mapa")            
    print("   A   B   C   D   E   F   G   H   I   J          A   B   C   D   E   F   G   H   I   J")
    for lista_idx in range(len(matriz_pc)):
        linha = ""
        linha+=str(lista_idx+1)
        for elem in range(len(matriz_pc[lista_idx])):
            if matriz_pc[lista_idx][elem] == "X":
                if lista_idx == 9 and elem == 9:
                    linha+=("  "+(matriz_pc[lista_idx][elem]))
                else:
                    linha+=("   "+(matriz_pc[lista_idx][elem]))
            else:
                if lista_idx == 9 and elem == 9:
                    linha+=("  "+(" "))
                else:
                    linha+=("   "+(" "))

        linha+=" "+str(lista_idx+1)
        if lista_idx == 9:
            linha+=("  ")
        else:
            linha+=("   ")
        
        linha+=str(lista_idx+1)
        
        for elem in range(len(matriz_jg[lista_idx])):
            if lista_idx == 9 and elem == 9:
                linha+=("  "+(matriz_jg[lista_idx][elem]))
            else:
                linha+=("   "+(matriz_jg[lista_idx][elem]))
        linha+=" "+str(lista_idx+1)

        print(linha)
    print("   A   B   C   D   E   F   G   H   I   J          A   B   C   D   E   F   G   H   I   J")

import time
def rodada(comeca,mapa_pc,mapa_jg):
    if comeca == "pc":
        novo = False
        while novo == False:
            ataqueLinha = random.choice(0,len(mapa_jg)-1)
            ataqueColuna = random.choice(0,len(mapa_jg)-1)
            novo = mapa_jg[ataqueLinha][ataqueColuna] == "N" or  mapa_jg[ataqueLinha][ataqueColuna] == " "
            if mapa_jg[ataqueLinha][ataqueColuna] == "N":
                mapa_jg[ataqueLinha][ataqueColuna] = "X"
            elif mapa_jg[ataqueLinha][ataqueColuna] == " ":
                mapa_jg[ataqueLinha][ataqueColuna] = "A"
        
        print("Agora é sua vez!")
        time.sleep(1)
        novo = False
        while novo == False:
            linha = int(input("Qual linha você quer atacar?"))
            coluna = ord(input("Qual coluna você quer atacar?"))-ord("A")
            novo = mapa_pc[linha][coluna] == "N" or  mapa_pc[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_pc[linha][coluna] == "N":
            mapa_pc[linha][coluna] == "X"
        elif mapa_pc[linha][coluna] == " ":
            mapa_pc[linha][coluna] == "A"


    else:
        print("Sua vez!")
        time.sleep(1)
        novo = False
        while novo == False:
            linha = int(input("Qual linha você quer atacar?"))
            coluna = ord(input("Qual coluna você quer atacar?"))-ord("A")
            novo = mapa_pc[linha][coluna] == "N" or  mapa_pc[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_pc[linha][coluna] == "N":
            mapa_pc[linha][coluna] == "X"
        elif mapa_pc[linha][coluna] == " ":
            mapa_pc[linha][coluna] == "A"
        

        novo = False
        while novo == False:
            ataqueLinha = random.choice(0,len(mapa_jg)-1)
            ataqueColuna = random.choice(0,len(mapa_jg)-1)
            novo = mapa_jg[ataqueLinha][ataqueColuna] == "N" or  mapa_jg[ataqueLinha][ataqueColuna] == " "
            if mapa_jg[ataqueLinha][ataqueColuna] == "N":
                mapa_jg[ataqueLinha][ataqueColuna] = "X"
            elif mapa_jg[ataqueLinha][ataqueColuna] == " ":
                mapa_jg[ataqueLinha][ataqueColuna] = "A"

    return mapa_pc,mapa_jg


