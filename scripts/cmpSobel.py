from PIL import Image
import sys
from fonctions import compDifImagesGris
from fonctions import diffGris
from fonctions import sobel
from fonctions import toGray
from variables import sobelPath

ims = [Image.open(f) for f in sys.argv[1:]]

for i in range(0, 2):
    ims[i] = sobel(toGray(ims[i]))
    parts = (sys.argv[i + 1].split("/"))[1].split(".")
    pathSobelFile = "/" + parts[0] + "_sobel.jpg"
    ims[i].save(str(sobelPath) + pathSobelFile)

if ims[0].mode == "L":
    cmpDifImgsGris = compDifImagesGris(diffGris(ims[0], ims[1]))
    print(cmpDifImgsGris)
    if cmpDifImgsGris <= 30:
        print("Ces deux images ont moins de 30 % de difference en terme de formes, on peut donc considerer qu'elles se ressemblent au niveau formes.")
    else:
        print("Ces deux images ont plus de 30 % de difference en terme de formes, on peut donc considerer qu'elles ne se ressemblent pas au niveau formes.")
