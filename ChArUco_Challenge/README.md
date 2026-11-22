<!-- # Calibração de Câmera com Tabuleiro ChArUco

Programa em Python que estima os parâmetros intrínsecos de uma câmera (matriz da câmera e coeficientes de distorção) a partir de fotos de um tabuleiro ChArUco, usando OpenCV.

## Descrição

O ChArUco combina um tabuleiro de xadrez com marcadores ArUco. Como as medidas reais do tabuleiro são conhecidas, o OpenCV compara a posição esperada dos cantos com a posição em que aparecem em cada foto e calcula os parâmetros da câmera.

O programa:

1. Define o tabuleiro e o dicionário de marcadores.
2. Lê cada imagem da pasta e detecta os marcadores ArUco.
3. Interpola os cantos do tabuleiro a partir dos marcadores.
4. Calibra a câmera com todos os cantos detectados.
5. Imprime a matriz da câmera, os coeficientes de distorção e o erro de reprojeção.

## Parâmetros do tabuleiro

| Parâmetro | Valor |
|---|---|
| Tipo do tabuleiro | 9 x 7 |
| Tamanho do quadrado | 4,5 cm (0,045 m) |
| Tamanho do marcador | 3,3 cm (0,033 m) |
| Dicionário ArUco | `aruco.DICT_4X4_50` |
| Resolução das imagens | 640 x 480 |

## Estrutura de arquivos

```
.
├── ChArUco_calib.py
├── README.md
└── canon_charuco/
    ├── IMG_1570.JPG
    ├── IMG_1575.JPG
    └── ... (97 imagens)
```

## Requisitos

- Python 3.8 ou mais novo
- OpenCV com o módulo contrib (`opencv-contrib-python`)

O código usa as funções clássicas do módulo `aruco` (`Dictionary_get`, `CharucoBoard_create`, `interpolateCornersCharuco`, `calibrateCameraCharuco`), que existem no OpenCV 4.x até a 4.6. Nas versões 4.7 ou mais novas essas funções foram removidas ou mudaram de nome. Foi testado com a versão **4.6.0.66**.

## Instalação das bibliotecas

Recomenda-se um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install opencv-contrib-python==4.6.0.66 "numpy<2"
```

Para conferir a instalação:

```bash
python -c "import cv2; print(cv2.__version__)"
```

## Como executar

Coloque as imagens na pasta `canon_charuco` (ao lado do script) e rode:

```bash
python ChArUco_calib.py
```

Para usar outra pasta de imagens, passe o caminho como argumento:

```bash
python ChArUco_calib.py caminho/para/a/pasta
```

## Saída esperada

O programa imprime, nesta ordem:

```
Number of images where the corners were detected <número de imagens>
Calibration Matrix
[[fx  0 cx]
 [ 0 fy cy]
 [ 0  0  1]]
Radil distortion coeficients
[[k1 k2 p1 p2 k3]]
Ret
<erro de reprojeção>
```

- **Calibration Matrix**: distâncias focais (`fx`, `fy`) e ponto principal (`cx`, `cy`), em pixels.
- **Distortion coefficients**: distorção radial (`k1`, `k2`, `k3`) e tangencial (`p1`, `p2`).
- **Ret**: erro médio de reprojeção, em pixels. Quanto menor, melhor.

## Resultado obtido

Execução com as 97 imagens fornecidas (OpenCV 4.6.0.66):

| Item | Valor |
|---|---|
| Imagens com cantos detectados | 97 |
| fx / fy | ~503,8 / ~505,8 |
| cx / cy | ~275,6 / ~269,2 |
| Ret | ~1,06 |

Os valores de referência fornecidos no desafio são diferentes (fx ≈ fy ≈ 459,6, cx ≈ 320,4, cy ≈ 240,6, Ret ≈ 0,40). Não foi possível reproduzi-los com estas imagens e as funções do tutorial.

## Referências

- [Tutorial de calibração ArUco/ChArUco (OpenCV)](https://docs.opencv.org/4.x/da/d13/tutorial_aruco_calibration.html)
- [Calibração ChArUco (mecaruco2)](https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html) -->




# Calibração de Câmera com Tabuleiro ChArUco

Programa em Python que estima os parâmetros intrínsecos de uma câmera (matriz da câmera e coeficientes de distorção) a partir de fotos de um tabuleiro ChArUco, usando OpenCV.

## Descrição

O ChArUco combina um tabuleiro de xadrez com marcadores ArUco. Como as medidas reais do tabuleiro são conhecidas, o OpenCV compara a posição esperada dos cantos com a posição em que aparecem em cada foto e calcula os parâmetros da câmera.

O programa:

1. Define o tabuleiro e o dicionário de marcadores.
2. Lê cada imagem da pasta e detecta os marcadores ArUco.
3. Interpola os cantos do tabuleiro a partir dos marcadores.
4. Calibra a câmera com todos os cantos detectados.
5. Imprime a matriz da câmera, os coeficientes de distorção e o erro de reprojeção.

## Parâmetros do tabuleiro

| Parâmetro | Valor |
|---|---|
| Tipo do tabuleiro | 9 x 7 |
| Tamanho do quadrado | 4,5 cm (0,045 m) |
| Tamanho do marcador | 3,3 cm (0,033 m) |
| Dicionário ArUco | `aruco.DICT_4X4_50` |
| Resolução das imagens | 640 x 480 |

## Estrutura de arquivos

```
.
├── .gitignore
├── ChArUco_calib.py
├── README.md
├── requirements.txt
└── canon_charuco/
    ├── IMG_1570.JPG
    ├── IMG_1575.JPG
    └── ... (97 imagens)
```

## Requisitos

- Python 3.8 ou mais novo
- OpenCV com o módulo contrib (`opencv-contrib-python`)

O código usa as funções clássicas do módulo `aruco` (`Dictionary_get`, `CharucoBoard_create`, `interpolateCornersCharuco`, `calibrateCameraCharuco`), que existem no OpenCV 4.x até a 4.6. Nas versões 4.7 ou mais novas essas funções foram removidas ou mudaram de nome. Foi testado com a versão **4.6.0.66**.

## Instalação das bibliotecas

Recomenda-se utilizar Python 3.10 e um ambiente virtual exclusivo para o projeto.

Crie o ambiente virtual na pasta do projeto:

```powershell
py -3.10 -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Com o ambiente ativado, atualize o pip:

```powershell
python -m pip install --upgrade pip
```

Instale as dependências:

```powershell
pip install numpy==1.26.4
pip install opencv-contrib-python==4.6.0.66
```

Para conferir a instalação:

```powershell
python -c "import cv2, numpy; print('OpenCV:', cv2.__version__); print('NumPy:', numpy.__version__); print('ArUco disponível:', hasattr(cv2, 'aruco'))"
```

Para executar o projeto em outras sessões, basta ativar novamente o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Como executar

Coloque as imagens na pasta `canon_charuco` (ao lado do script) e rode:

```bash
python ChArUco_calib.py
```

Para usar outra pasta de imagens, passe o caminho como argumento:

```bash
python ChArUco_calib.py caminho/para/a/pasta
```

## Saída esperada

O programa imprime, nesta ordem:

```
Number of images where the corners were detected <número de imagens>
Calibration Matrix
[[fx  0 cx]
 [ 0 fy cy]
 [ 0  0  1]]
Radil distortion coeficients
[[k1 k2 p1 p2 k3]]
Ret
<erro de reprojeção>
```

- **Calibration Matrix**: distâncias focais (`fx`, `fy`) e ponto principal (`cx`, `cy`), em pixels.
- **Distortion coefficients**: distorção radial (`k1`, `k2`, `k3`) e tangencial (`p1`, `p2`).
- **Ret**: erro médio de reprojeção, em pixels. Quanto menor, melhor.

## Resultado obtido

Execução com as 97 imagens fornecidas (OpenCV 4.6.0.66):

| Item | Valor |
|---|---|
| Imagens com cantos detectados | 97 |
| fx / fy | ~503,8 / ~505,8 |
| cx / cy | ~275,6 / ~269,2 |
| Ret | ~1,06 |

Os valores de referência fornecidos no desafio são diferentes (fx ≈ fy ≈ 459,6, cx ≈ 320,4, cy ≈ 240,6, Ret ≈ 0,40). Não foi possível reproduzi-los com estas imagens e as funções do tutorial.

## Referências

- [Tutorial de calibração ArUco/ChArUco (OpenCV)](https://docs.opencv.org/4.x/da/d13/tutorial_aruco_calibration.html)
- [Calibração ChArUco (mecaruco2)](https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html)