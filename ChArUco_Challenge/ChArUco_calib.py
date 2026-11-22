import sys
import os
import numpy as np
import cv2
from cv2 import aruco

# Pasta com as imagens (pode passar como argumento: python calibracao_charuco.py pasta)
pasta = sys.argv[1] if len(sys.argv) > 1 else "canon_charuco"

# Parametros do tabuleiro
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
board = aruco.CharucoBoard_create(9, 7, 0.045, 0.033, aruco_dict)
params = aruco.DetectorParameters_create()

allCorners = []
allIds = []
imgSize = None

imagens = sorted([os.path.join(pasta, f) for f in os.listdir(pasta) if f.lower().endswith(".jpg")])

for nome in imagens:
    img = cv2.imread(nome)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgSize = gray.shape[::-1]

    # detecta os marcadores ArUco
    corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=params)

    if len(corners) > 0:
        # interpola os cantos do tabuleiro ChArUco
        n, charucoCorners, charucoIds = aruco.interpolateCornersCharuco(corners, ids, gray, board)
        if charucoCorners is not None and n > 3:
            allCorners.append(charucoCorners)
            allIds.append(charucoIds)

print("Number of images where the corners were detected", len(allCorners))

# Calibracao da camera
ret, mtx, dist, rvecs, tvecs = aruco.calibrateCameraCharuco(
    allCorners, allIds, board, imgSize, None, None)

print("Calibration Matrix")
print(mtx)
print("Radil distortion coeficients")
print(dist)
print("Ret")
print(ret)
