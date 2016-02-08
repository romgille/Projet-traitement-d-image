import Image
import sys
import fonctions

ims = [Image.open(f) for f in sys.argv[1:]]
if ims[0].mode == "L":
    fonctions.compDifImagesGris(fonctions.diffGris(ims[0], ims[1]))
if ims[0].mode == "RGB":
    fonctions.compDifImages(fonctions.diff(ims[0], ims[1]))
