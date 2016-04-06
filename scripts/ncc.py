import Image
import sys
import math


def get_average(im):
    val = 0.0
    pix = im.load()
    w, h = im.size
    for j in range(h):
        for i in range(w):
            val += pix[i, j]
    return val/(w*h)


def ncc(I, T):
    Im = get_average(I)
    Tm = get_average(T)
    num = 0.0
    den = 0.0
    denI = 0.0
    denT = 0.0
    pT = T.load()
    pI = I.load()
    w, h = I.size
    for y in range(h):
        for x in range(w):
            i = pI[x, y] - Im
            t = pT[x, y] - Tm
            num += i*t
            denI += i**2
            denT += t**2
    return num/math.sqrt(denI*denT)


def normalizeImages(imlist):
    minS = [float("inf"), float("inf")]
    maxS = [0, 0]
    for i in imlist:
        s = i.size
        for d in range(0, 2):
            if minS[d] > s[d]:
                minS[d] = s[d]
            if maxS[d] < s[d]:
                maxS[d] = s[d]
    if minS[0] == maxS[0] and minS[1] == maxS[1]:
        return imlist
    return [i.resize(minS) for i in imlist]


if __name__ == "__main__":
    im1 = Image.open(sys.argv[1]).convert("L")
    im2 = Image.open(sys.argv[2]).convert("L")
    im, im2 = normalizeImages((im1, im2))

    print(ncc(im, im2))
