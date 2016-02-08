from PIL import Image
import sys
from fonctions import comparaisonHisto

ims = [Image.open(f) for f in sys.argv[1:]]
print("Comparaison histogrammes en racine carre :")
comparaisonHisto(ims[0], ims[1], 0.5)
print
print("Comparaison histogrammes en facteur 1 :")
comparaisonHisto(ims[0], ims[1], 1)
print
print("Comparaison histogrammes en puissance de 2 :")
comparaisonHisto(ims[0], ims[1], 2)
print
