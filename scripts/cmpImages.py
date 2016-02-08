import Image
import sys
from fonctions import compDifImagesGris
from fonctions import compDifImages
from fonctions import diffGris
from fonctions import diff


ims = [Image.open(f) for f in sys.argv[1:]]
if ims[0].mode == "L":
    compDifImagesGris(diffGris(ims[0], ims[1]))
if ims[0].mode == "RGB":
    compDifImages(diff(ims[0], ims[1]))
