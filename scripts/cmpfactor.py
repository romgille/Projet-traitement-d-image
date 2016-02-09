from PIL import Image
import sys
from fonctions import comparaisonImage3channels2

ims = [Image.open(f) for f in sys.argv[1:]]
if ims[0].mode == "RGB":
    comparaisonImage3channels2(ims[0], ims[1], 0.5)
