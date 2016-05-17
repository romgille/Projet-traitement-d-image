from PIL import Image
import sys
from fonctions import comparaisonHisto3channels
from fonctions import buildHistogram
# from fonctions import drawHistogram
# from variables import histosPath


def histogramme(x):
    im = Image.open(sys.argv[x])
    if(im.mode == "RGB"):
        # parts = (sys.argv[x].split("/"))[1].split(".")
        newIm = buildHistogram(im)
        # pathHistoFile = "/" + parts[0] + "_histo.jpg"
        # drawHistogram(newIm).save(str(histosPath) + pathHistoFile)
        return newIm
    else:
        return ""

cmpHisto = comparaisonHisto3channels(histogramme(1), histogramme(2), 2)
print(cmpHisto, end="")
