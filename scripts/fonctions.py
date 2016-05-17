from PIL import Image
from math import sqrt
from math import log


def comparaisonHistoBhattacharyya(histoA, histoB):
    hA = normHisto(histoA)
    hB = normHisto(histoB)
    distance = 0.
    for i in range(0, 255):
        distance += (hA[i] * hB[i]) ** 0.5
    newDistance = -log(distance)
    return newDistance


def comparaisonHisto3channels(histoA, histoB, factor):
    resultsBatta = []
    moyenneBatta = 0
    for c in range(3):
        resultBatta = comparaisonHistoBhattacharyya(histoA[c], histoB[c])
        resultsBatta.append(resultBatta)
    for i in range(0, 3):
        moyenneBatta += resultsBatta[i]
    moyenneBatta /= 3.
    return round((moyenneBatta * 100), 2)


def buildHistogram(im):
    pix = im.load()
    if (im.mode == "RGB"):
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
    elif im.mode == "HSV":
        H = [0]*360
        S = [0]*100
        V = [0]*100
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                val = pix[i, j]
                H[val[0]] += 1
                S[val[1]] += 1
                V[val[2]] += 1
        histo = (H, S, V)
        return histo
    else:
        print("Votre image n'est pas en RGB ou en HSV")


def maxValeur(histo):
    maxV = 0
    for j in range(0, 3):
        for i in range(0, 256):
            if maxV < histo[j][i]:
                maxV = histo[j][i]
    return maxV


def drawBin(im, startx, endx, value, maxV, channel):
    pix = im.load()
    hauteur = (value * im.size[1]) / maxV
    for i in range(startx, endx):
        for j in range(511, 513-hauteur, -1):
                val = list(pix[i, j])
                val[channel] = 255
                pix[i, j] = tuple(val)


def drawHistogram(histo):
    newIm = Image.new("RGB", (512, 512))
    val = 0
    val1 = 0
    val2 = 0
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


def toGray(im):
    if im.mode == "RGB":
        gray = Image.new("L", im.size)
        pix = im.load()
        gpix = gray.load()
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                val = pix[i, j]
                gpix[i, j] = int((val[0]+val[1]+val[2])/3)
        return gray
    else:
        return im


def sobel(im):
    pix = im.load()
    result = Image.new("L", im.size)
    rpix = result.load()
    for i in range(1, im.size[0] - 1):
        for j in range(1, im.size[1] - 1):
            a = -pix[i - 1, j - 1] - 2*pix[i - 1, j] - pix[i - 1, j + 1]
            b = pix[i + 1, j - 1] + 2*pix[i + 1, j] + pix[i + 1, j + 1]
            c = -pix[i - 1, j - 1] - 2*pix[i, j - 1] - pix[i + 1, j - 1]
            d = pix[i + 1, j + 1] + 2*pix[i, j + 1] + pix[i + 1, j + 1]
            gX = a + b
            gY = c + d
            g = int(sqrt((gX*gX)+(gY*gY)).real)
            rpix[i, j] = g
    return result


def normalize(images):
    w = []
    h = []
    for i in images:
        w.append(i.size[0])
        h.append(i.size[1])
    w.sort()
    h.sort()
    if w[0] == w[-1] and h[0] == h[-1]:
        return images
    else:
        newImages = []
        for i in images:
            if i.mode == "L":
                newImages.append(cropGris(i, 0, 0, w[0], h[0]))
            if i.mode == "RGB":
                newImages.append(crop(i, 0, 0, w[0], h[0]))
        newImagesT = tuple(newImages)
        return newImagesT


def normHisto(histo):
    r = []
    s = 0.0
    for h in histo:
        s += h
    for h in histo:
        r.append(h/s)
    return r


def compDifImagesGris(im):
    pix = im.load()
    comp = 0.
    taille = im.size[0]*im.size[1]
    prcentge = 0
    for x in range(0, im.size[0]):
        s = 0
        for y in range(0, im.size[1]):
            s = pix[x, y]
            if 0 <= s <= 15:
                comp = comp + 0
            else:
                comp = comp + 1
    prcentge = (comp/taille)*100
    prcentge = round(prcentge, 2)
    return prcentge


def diffGris(A, B):
    a, b = normalize([A, B])
    pixa = a.load()
    pixb = b.load()
    newIm = Image.new("L", a.size)
    pix1 = newIm.load()
    for i in range(0, newIm.size[0]):
        for j in range(0, newIm.size[1]):
            val1 = pixa[i, j]
            val2 = pixb[i, j]
            val = abs(int(val1) - int(val2))
            pix1[i, j] = val
    return newIm


def crop(im, x, y, w, h):
    pix = im.load()
    newIm = Image.new("RGB", (w, h))
    pix1 = newIm.load()
    for i in range(x, x+w):
        for j in range(y, y + h):
            pix1[i-x, j-y] = pix[i, j]
    return newIm


def cropGris(im, x, y, w, h):
    pix = im.load()
    newIm = Image.new("L", (w, h))
    pix1 = newIm.load()
    for i in range(x, x+w):
        for j in range(y, y + h):
            pix1[i-x, j-y] = pix[i, j]
    return newIm


def toHSV(im):
    hsv = Image.new("RGB", im.size)
    pix = im.load()
    hsvPix = hsv.load()
    epsilon = 0.00001
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b = pix[x, y]
            r, g, b = [v/255.0 for v in (r, g, b)]
            cmax = max(r, g, b)
            cmin = min(r, g, b)
            delta = cmax-cmin
            h = 0
            if delta > 0:
                if cmax >= r-epsilon and cmax <= r+epsilon:
                    v = (g-b)/delta
                    h = 60*(v-6*(int(v)/6))
                elif cmax >= g-epsilon and cmax <= g+epsilon:
                    h = 60*(((b-r)/delta) + 2)
                else:
                    h = 60*(((r-g)/delta) + 4)
            s = 0
            if cmax > 0:
                s = delta/cmax
            v = cmax
            hsvPix[x, y] = (int(h*2.55/3.6), int(s*255), int(v*255))
    return hsv
