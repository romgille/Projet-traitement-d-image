import Image
import sys
from variables import histosPath
from fonctions import buildHistogram
from fonctions import drawHistogram

im = Image.open(sys.argv[1])
parts = (sys.argv[1].split("/"))[1].split(".")
newIm = buildHistogram(im)
pathHistoFile = "/" + parts[0] + "_histo.jpg"
<<<<<<< HEAD
fonctions.drawHistogram(newIm).save(str(variables.histosPath) + pathHistoFile)

=======
drawHistogram(newIm).save(str(histosPath) + pathHistoFile)
>>>>>>> 85e15118f45aaee2a1d70d8b2f82665ab4ef1347
