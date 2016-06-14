import Image
import sys
import variables
import fonctions

im = Image.open(sys.argv[1])
parts = (sys.argv[1].split("/"))[1].split(".")
pathHistoFile = "/" + parts[0] + "_histo.jpg"
newIm = fonctions.buildHistogram(im)
fonctions.drawHistogram(newIm).save(str(variables.histosPath) + pathHistoFile)
