import numpy as np
import random
from PIL import Image

stranaX = 512
stranaY = 512
sirkaArray = np.tile(
    np.linspace(0.0, 1.0, stranaX).reshape((1, stranaX, 1)),
    (stranaY, 1, 3),
)
vyskaArray = np.tile(
    np.linspace(0.0, 1.0, stranaY).reshape((stranaY, 1, 1)),
    (1, stranaX, 3),
)

def kolikJeStranaY():
    return vyskaArray
def kolikJeStranaX():
    return sirkaArray
def generujBarvu():
    return np.tile(
        np.array([random.random(), random.random(), random.random()]).reshape((1, 1, 3)),
        (stranaY, stranaX, 1),
    )
funkceNaVyber = [(0,generujBarvu),(0,kolikJeStranaX),(0,kolikJeStranaY),(1,np.cos),(1,np.sin),(1,np.tan),(2,np.add),(2,np.subtract),(2,np.multiply),(2,np.divide)]
minimalniHloubka = 2
maximalniHloubka = 10

def opravNeplatneHodnoty(matice):
    matice[matice == np.inf] = 100000
    matice[matice == -np.inf] = -100000
    matice[matice == 0] = 0.0001
    return matice

def Generuj(hloubka = 0):
    funkce = [fce for fce in funkceNaVyber 
              if(fce[0]>0 and hloubka < maximalniHloubka) 
              or (fce[0] == 0 and hloubka >= minimalniHloubka)]
    nArgs,dalsiFunkce = random.choice(funkce)
    args = [Generuj(hloubka + 1) for x in range(nArgs)]
    return opravNeplatneHodnoty(dalsiFunkce(*args))

obrazek = Generuj()
# Ukradeny z googlu
obrazekPrevedenej = np.uint8(np.rint(obrazek.clip(0.0, 1.0) * 255.0))
Image.fromarray(obrazekPrevedenej).save("C:\\Users\\Lalok\\OneDrive\\Desktop\\vysledek.bmp")
