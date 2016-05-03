from PIL import Image
import sys
from fonctions import compDifImagesGris
from fonctions import compDifImages
from fonctions import diffGris
from fonctions import diff


ims = [Image.open(f) for f in sys.argv[1:]]
if(ims[0].mode == ims[1].mode):
    if ims[0].mode == "L":
        print(compDifImagesGris(diffGris(ims[0], ims[1])), end="")
    if ims[0].mode == "RGB":
        cmpDiffImgs = compDifImages(diff(ims[0], ims[1]))
        print(cmpDiffImgs, end='')
