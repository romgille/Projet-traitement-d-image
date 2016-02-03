import Image
import sys
import variables
import fonctions

im = Image.open(sys.argv[1])
fonctions.drawHistogram(fonctions.buildHistogram(im)).save(str(variables.histosPath) + "/histo.jpg")
