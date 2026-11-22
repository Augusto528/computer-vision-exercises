import sys
import os
import numpy as np
import cv2
from cv2 import aruco

def main():
    # Pasta com as imagens (pode passar como argumento: python calibracao_charuco.py pasta)
    pasta = sys.argv[1] if len(sys.argv) > 1 else "canon_charuco"

    # Parametros do tabuleiro
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    board = aruco.CharucoBoard_create(9, 7, 0.045, 0.033, aruco_dict)
    params = aruco.DetectorParameters_create()

    # Criação das variáveis que vão receber os pontos esolhidos e seus ID'ss
    allCorners = []
    allIds = []
    imgSize = None

    # Pega todas as imagens da pasta de imagens. Pega com base na extensão do arquivo -> se for .jpg ou .JPG (há um '.lower()' pra deixar as letras de cada nome em minúsculo), ele adiciona a 'imagens'
    imagens = sorted([os.path.join(pasta, f) for f in os.listdir(pasta) if f.lower().endswith(".jpg")])

    checar_orientacoes(imagens)
    
    for nome in imagens:

        img = cv2.imread(nome)

        # Verifica se a imagem está em formato retrato. Caso não esteja no formato correto, rotaciona a imagem para melhorar os resultados
        if img.shape[1] < img.shape[0]:
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        # Deixa a imagem em preto e branco. Como queremos ver somente formas, cores somente atrapalhariam os processos
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        imgSize = gray.shape[::-1]

        # Detecta os marcadores ArUco
        corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=params)

        # Verifica se achou algum corner dentro da imagem
        if len(corners) > 0:

            # Interpola os cantos do tabuleiro ChArUco
            n, charucoCorners, charucoIds = aruco.interpolateCornersCharuco(corners, ids, gray, board)

            # Se encontrar Corners (mais que 3), adiciona nas listas de Corners e de Id's
            if charucoCorners is not None and n > 3:
                allCorners.append(charucoCorners)
                allIds.append(charucoIds)

    print("Number of images where the corners were detected", len(allCorners))

    # Calibracao da camera usando biblioteca
    ret, mtx, dist, rvecs, tvecs = aruco.calibrateCameraCharuco(allCorners, allIds, board, imgSize, None, None)
    
    # Print dos resultados encontrados
    print("Calibration Matrix")
    print(mtx)
    print("Radil distortion coeficients")
    print(dist)
    print("Ret")
    print(ret)


# Função pra ver a quantidade de imagens em modo retrato/paisagem. Não será utilizada na main final, mas ajudou MUITO a melhorar os resultados.
# Imagens em retrato: 46
# Imagens em paisagem: 50
def checar_orientacoes(imagens):
    
    tamanhos = {}
    retrato = 0
    paisagem = 0

    for nome in imagens:
        img = cv2.imread(nome)

        h, w = img.shape[:2]

        tamanho = (w, h)
        tamanhos[tamanho] = tamanhos.get(tamanho, 0) + 1

        if h > w:
            retrato += 1
        else:
            paisagem += 1

    print("Dimensões encontradas:", tamanhos)
    print("Imagens em retrato:", retrato)
    print("Imagens em paisagem:", paisagem)


main()
