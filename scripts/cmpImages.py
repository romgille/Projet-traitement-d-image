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
            print compDifImages(diff(ims[0], ims[1]))
    else:
        print "Les deux images ne sont pas du meme type (RGB ou nuance de gris)"
