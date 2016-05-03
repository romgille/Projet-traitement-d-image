from PIL import Image
import sys
from fonctions import comparaisonHisto3channels
from fonctions import buildHistogram

ims = [Image.open(f) for f in sys.argv[1:]]
if(ims[0].mode == ims[1].mode):
    histo1 = buildHistogram(ims[0])
    histo2 = buildHistogram(ims[1])
    cmpHisto = comparaisonHisto3channels(histo1, histo2, 2)
    print(cmpHisto, end="")
