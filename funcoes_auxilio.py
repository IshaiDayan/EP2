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
            