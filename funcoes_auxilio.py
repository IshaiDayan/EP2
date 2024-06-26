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
    print(" ")
    print("           Mapa do Computador                                  Seu Mapa")            
    print("    A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")
    for lista_idx in range(len(matriz_pc)):
        linha = ""
        linha+=str(lista_idx+1)
        for elem in range(len(matriz_pc[lista_idx])):
            if matriz_pc[lista_idx][elem] == "X":
                if lista_idx == 9 and elem == 0:
                    linha+=("  "+"\u001b[31m"+(matriz_pc[lista_idx][elem])+"\u001b[0m")
                   
                else:
                    linha+=("   "+"\u001b[31m"+(matriz_pc[lista_idx][elem])+"\u001b[0m")

            elif matriz_pc[lista_idx][elem] == "A":
                if lista_idx == 9 and elem == 0:
                    linha+=("  "+"\u001b[34m"+(matriz_pc[lista_idx][elem])+"\u001b[0m")
                   
                else:
                    linha+=("   "+"\u001b[34m"+(matriz_pc[lista_idx][elem])+"\u001b[0m")
                   
            else:
                if lista_idx == 9 and elem == 0:
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
            if matriz_jg[lista_idx][elem] == "X":
                if lista_idx == 9 and elem == 0:
                    linha+=("  "+"\u001b[31m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[31m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
            elif matriz_jg[lista_idx][elem] == "A":
                if lista_idx == 9 and elem == 0:
                    linha+=("  "+"\u001b[34m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[34m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
            else:
                if lista_idx == 9 and elem == 0:
                    linha+=("  "+"\u001b[32m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[32m"+(matriz_jg[lista_idx][elem])+"\u001b[0m")
                
        linha+=" "+str(lista_idx+1)

        print(linha)
    print("    A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")
    print(" ")

import time
def rodada(comeca,mapa_pc,mapa_jg,funcionando):
    if comeca == "pc":
        print("Computador Jogando...")
        novo = False
        while novo == False:
            ataqueLinha = random.randint(0,len(mapa_jg)-1)
            ataqueColuna = random.randint(0,len(mapa_jg)-1)
            novo = mapa_jg[ataqueLinha][ataqueColuna] == "N" or  mapa_jg[ataqueLinha][ataqueColuna] == " "
            if mapa_jg[ataqueLinha][ataqueColuna] == "N":
                mapa_jg[ataqueLinha][ataqueColuna] = "X"
                print("BOOOOOOM!!! O computador acertou um navio!")
            elif mapa_jg[ataqueLinha][ataqueColuna] == " ":
                mapa_jg[ataqueLinha][ataqueColuna] = "A"
                print("ERROOOU! O tiro caiu na água!")

        funcionando_jg = Checar_se_acabou(funcionando,mapa_jg)
        
        time.sleep(2)
        print("Agora é sua vez!")
        time.sleep(1)
        novo = False
        while novo == False:
            coluna = input("Qual coluna você quer atacar?").upper()
            if coluna not in constantes.Letras:
                print("Coluna Invalida. Tente novamente.")
                continue
            linha = input("Qual linha você quer atacar?")
            if linha.isnumeric() and int(linha) <= 10 and int(linha) >= 1:
                pass
            
            else:
                print("Linha Invalida. Tente novamente.")
                continue

            linha = int(linha)-1
            coluna = ord(coluna)-ord("A")
            novo = mapa_pc[linha][coluna] == "N" or  mapa_pc[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_pc[linha][coluna] == "N":
            mapa_pc[linha][coluna] = "X"
            print("BOOOOOOM!!! Você acertou um navio!")
        elif mapa_pc[linha][coluna] == " ":
            mapa_pc[linha][coluna] = "A"
            print("ERROOOU! O tiro caiu na água!")

        funcionando_pc = Checar_se_acabou(funcionando,mapa_pc)
        time.sleep(2)
    else:
        print("Sua vez!")
        time.sleep(1)
        novo = False
        while novo == False:
            coluna = input("Qual coluna você quer atacar?").upper()
            if coluna not in constantes.Letras:
                print("Coluna Invalida. Tente novamente.")
                continue
            linha = input("Qual linha você quer atacar?")
            if linha.isnumeric() and int(linha) <= 10 and int(linha) >= 1:
                pass
            
            else:
                print("Linha Invalida. Tente novamente.")
                continue
            linha = int(linha)-1
            coluna = ord(coluna)-ord("A")
            novo = mapa_pc[linha][coluna] == "N" or  mapa_pc[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_pc[linha][coluna] == "N":
            mapa_pc[linha][coluna] = "X"
            print("BOOOOOOM!!! Você acertou um navio!")
        elif mapa_pc[linha][coluna] == " ":
            mapa_pc[linha][coluna] = "A"
            print("ERROOOU! O tiro caiu na água!")
        
        funcionando_pc = Checar_se_acabou(funcionando,mapa_pc)
        time.sleep(2)
        novo = False
        print("Computador Jogando...")
        while novo == False:
            ataqueLinha = random.randint(0,len(mapa_jg)-1)
            ataqueColuna = random.randint(0,len(mapa_jg)-1)
            novo = mapa_jg[ataqueLinha][ataqueColuna] == "N" or  mapa_jg[ataqueLinha][ataqueColuna] == " "
            if mapa_jg[ataqueLinha][ataqueColuna] == "N":
                mapa_jg[ataqueLinha][ataqueColuna] = "X"
                print("BOOOOOOM!!! O computador acertou um navio!")
            elif mapa_jg[ataqueLinha][ataqueColuna] == " ":
                mapa_jg[ataqueLinha][ataqueColuna] = "A"
                print("ERROOOU! O tiro caiu na água!")

        
        time.sleep(2)
        
        funcionando_jg = Checar_se_acabou(funcionando,mapa_jg)
    
    funcionando = funcionando_jg and funcionando_pc
    return mapa_pc,mapa_jg,funcionando


def Checar_se_acabou(funcionando,mapa):
    for linha in mapa:
            if "N" in linha:
                funcionando = True
                return funcionando
            else:
                funcionando = False
    
    return funcionando
