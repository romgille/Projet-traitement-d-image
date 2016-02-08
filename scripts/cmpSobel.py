from PIL import Image
import sys
from fonctions import compDifImagesGris
from fonctions import compDifImages
from fonctions import diffGris
from fonctions import diff
from fonctions import sobel
from fonctions import toGray

ims = [Image.open(f) for f in sys.argv[1:]]
ims[0] = sobel(toGray(ims[0]))
ims[1] = sobel(toGray(ims[1]))
if ims[0].mode == "L":
    compDifImagesGris(diffGris(ims[0], ims[1]))
