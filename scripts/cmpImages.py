from PIL import Image
import sys
from fonctions import compDifImagesGris
from fonctions import compDifImages
from fonctions import diffGris
from fonctions import diff


ims = [Image.open(f) for f in sys.argv[1:]]
for i in range(0, len(ims)-1):
    if(ims[i].mode == ims[i+1].mode):
        if ims[0].mode == "L":
            print compDifImagesGris(diffGris(ims[0], ims[1]))
        if ims[0].mode == "RGB":
            cmpDiffImgs = compDifImages(diff(ims[0], ims[1]))
            print cmpDiffImgs
            if cmpDiffImgs <= 20:
                print "Ces deux images ont moins de 20 % de difference pixel a pixel, on peut donc considerer qu'elles se ressemblent pixel a pixel."
            else:
                print "Ces deux images ont plus de 20% de difference pixel a pixel, on peut donc considerer qu'elles ne se ressemblent pas pixel a pixel."
    else:
        print "Les deux images ne sont pas du meme type (RGB ou nuance de gris)"
