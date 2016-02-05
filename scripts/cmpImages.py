import Image
import sys
import variables
import fonctions

ims = [Image.open(f) for f in sys.argv[1:]]

fonctions.compDifImages(fonctions.diff(ims[0],ims[1]))
