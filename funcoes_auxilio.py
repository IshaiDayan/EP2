def cria_mapa(N):
    matriz = []
    for x in range(N):
       matriz.append([' ']*(N))
    return matriz












def foi_derrotado(matriz):
    for z in matriz:
        for j in z:
            if j == "N":
                return False
    return True



def printar_mapas(matriz1,matriz2):
    print("   A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")
    for lista_idx in range(len(matriz1)):
        linha = ""
        linha+=str(lista_idx+1)
        for elem in range(len(matriz1[lista_idx])):
            if lista_idx == 9 and elem == 9:
                linha+=("  "+(matriz1[lista_idx][elem]))
            else:
                linha+=("   "+(matriz1[lista_idx][elem]))

        linha+=" "+str(lista_idx+1)
        if lista_idx == 9:
            linha+=("  ")
        else:
            linha+=("   ")
        
        linha+=str(lista_idx+1)
        
        for elem in range(len(matriz2[lista_idx])):
            if lista_idx == 9 and elem == 9:
                linha+=("  "+(matriz2[lista_idx][elem]))
            else:
                linha+=("   "+(matriz2[lista_idx][elem]))
        linha+=" "+str(lista_idx+1)

        print(linha)
    print("   A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")

