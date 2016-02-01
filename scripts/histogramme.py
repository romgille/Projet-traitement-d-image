import Image
import sys
import os
from pathlib import Path

p = Path('.')
histosPath = os.path.abspath("./histogrammes")
photosPath = os.path.abspath("./photos")
scriptsPath = os.path.abspath("./scripts")


def buildHistogram(im):
    pix = im.load()
    R = [0]*256
    G = [0]*256
    B = [0]*256
    for i in range(0, im.size[0]):
        for j in range(0, im.size[1]):
            val = pix[i, j]
            R[val[0]] += 1
            G[val[1]] += 1
            B[val[2]] += 1
    histo = (R, G, B)
    return histo


def maxValeur(histo):
    maxV = 0
    for j in range(0, 3):
        for i in range(0, 256):
            if maxV < histo[j][i]:
                maxV = histo[j][i]
    return maxV


def drawBin(im, startx, endx, value, maxV, channel):
    pix = im.load()
    #calculer la hauteur H de la barre en fonction de value, max et im.size[1]
    hauteur = (value * im.size[1]) / maxV
    # pour tous les pixels dans la zone delimitee par startx et endx en largeur
        #et 0 et H en hauteur
            #mettre le canal "channel" de ce pixel a 255
    for i in range(startx, endx):
        for j in range(511, 513-hauteur, -1):
                val = list(pix[i, j])
                val[channel] = 255
                pix[i, j] = tuple(val)


def drawHistogram(histo):
    #creer image histogramme de 512x512 en RGB
    newIm = Image.new("RGB", (512, 512))
    val = 0
    val1 = 0
    val2 = 0
    #faire l'appel a drawBin qui va bien
    for j in range(0, 256):
        drawBin(newIm, val, val+1, histo[0][j], maxValeur(histo), 0)
        val += 2
    for j in range(0, 256):
        drawBin(newIm, val1, val1+1, histo[1][j], maxValeur(histo), 1)
        val1 += 2
    for j in range(0, 256):
        drawBin(newIm, val2, val2+1, histo[2][j], maxValeur(histo), 2)
        val2 += 2
    return newIm


im = Image.open(sys.argv[1])
drawHistogram(buildHistogram(im)).save(histosPath + "/histo.jpg")
print(p)
