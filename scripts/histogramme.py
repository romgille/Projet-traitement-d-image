from PIL import Image
import sys
from variables import histosPath
from fonctions import buildHistogram
from fonctions import drawHistogram

im = Image.open(sys.argv[1])
if(im.mode == "RGB"):
    parts = (sys.argv[1].split("/"))[1].split(".")
    newIm = buildHistogram(im)
    pathHistoFile = "/" + parts[0] + "_histo.jpg"
    drawHistogram(newIm).save(str(histosPath) + pathHistoFile)
else:
    print ""