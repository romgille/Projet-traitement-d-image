from PIL import Image
import sys
from hsv import toHSV
from fonctions import comparaisonHisto
from fonctions import buildHistogram


ims = [Image.open(f) for f in sys.argv[1:]]
for i in range(0, len(ims)-1):
    if ims[i].mode == ims[i+1].mode:
        toHSV(ims[i])
        #Sauvegarder l'image creer dans un dossier HSV
histo1 = buildHistogram(ims[0])
histo2 = buildHistogram(ims[1])
cmpHistoH = comparaisonHisto(histo1[0], histo2[0], 2)
cmpHistoS = comparaisonHisto(histo1[1], histo2[1], 2)
cmpHistoV = comparaisonHisto(histo1[2], histo2[2], 2)
# print "H"
print cmpHistoH
# print "S"
print cmpHistoS
# print "V"
print cmpHistoV
