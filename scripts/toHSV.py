from PIL import Image
import sys
from fonctions import toHSV
from fonctions import comparaisonHistoBhattacharyya
from fonctions import buildHistogram


ims = [Image.open(f) for f in sys.argv[1:]]
for i in range(0, len(ims)-1):
    if ims[i].mode == ims[i+1].mode:
        toHSV(ims[i])
# Mettre les images créées dans un dossier image HSV
histo1 = buildHistogram(ims[0])
histo2 = buildHistogram(ims[1])
# Mettre les histos dans un dossier histoHSV
cH = comparaisonHistoBhattacharyya(histo1[0], histo2[0])
cS = comparaisonHistoBhattacharyya(histo1[1], histo2[1])
cV = comparaisonHistoBhattacharyya(histo1[2], histo2[2])
cmpHistoH = round((cH * 100), 2)
cmpHistoS = round((cS * 100), 2)
cmpHistoV = round((cV * 100), 2)
# print "H"
print(cmpHistoH, end=",")
# print "S"
print(cmpHistoS, end=",")
# print "V"
print(cmpHistoV, end="")
# Ajouter une ligne "Distance de Bhattacharyya en H , en S et en V
# dans le rapport.md"
