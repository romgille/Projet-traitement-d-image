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
drawHistogram(newIm).save(str(histosPath) + pathHistoFile)
=======
fonctions.drawHistogram(newIm).save(str(variables.histosPath) + pathHistoFile)

>>>>>>> 86d793f7685a0b3aa4f0911d65b46cddcd3dcf98
