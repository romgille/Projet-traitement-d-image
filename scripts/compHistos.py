from PIL import Image
import sys
from fonctions import comparaisonHisto3channels
from fonctions import buildHistogram

ims = [Image.open(f) for f in sys.argv[1:]]
for i in range(0, len(ims)-1):
    if(ims[i].mode == ims[i+1].mode):
        histo1 = buildHistogram(ims[0])
        histo2 = buildHistogram(ims[1])
        print comparaisonHisto3channels(histo1, histo2, 2)
    else:
        print "Les deux images ne sont pas du meme type (RGB ou nuance de gris)"
