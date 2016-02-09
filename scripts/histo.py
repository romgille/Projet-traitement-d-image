import Image
import sys
import math

def buildHisto(im):
    if im.mode == "RGB":
        h = []
        for i in im.split():
            h.append(i.histogram())
        return h
    else:
        return im.histogram()

def normHisto(histo):
    r = []
    s = 0.0
    for h in histo:
        s += h
    for h in histo:
        r.append(h/s)
    return r



#return distance between two histograms of gray images
def bhattacharyyaCoeff(histoA, histoB):
    hA = normHisto(histoA)
    hB = normHisto(histoB)
    distance = 0.0
    for i in range(0, 255):
        distance += math.sqrt(hA[i] * hB[i])
    print(distance)
    if distance > 1:
        return 1
    return distance
    

#return distance between two histograms of gray images
def bhattacharyya(histoA, histoB):
    return -math.log(bhattacharyyaCoeff(histoA, histoB))


#return distance between two histograms of gray images
def hellinger(histoA, histoB):
    return math.sqrt(1-bhattacharyyaCoeff(histoA, histoB))


#return distance between two histograms of RGB images
def bhattacharyya3channels(histoA, histoB):
    distances = []
    for c in range(3):
        distances.append(bhattacharyya(histoA[c],histoB[c]))
    return distances


#return distance between two histograms of RGB images
def hellinger3channels(histoA, histoB):
    distances = []
    for c in range(3):
        distances.append(hellinger(histoA[c],histoB[c]))
    return distances

#resize all images to the same size
def normalizeImages(imlist):
    minS = [float("inf"),float("inf")]
    maxS = [0,0]
    for i in imlist:
        s = i.size
        for d in range(0,2):
            if minS[d] > s[d]:minS[d] = s[d]
            if maxS[d] < s[d]:maxS[d] = s[d]
    if minS[0] == maxS[0] and minS[1] == maxS[1]:
        return imlist
    return [i.resize(minS) for i in imlist]



if __name__ == "__main__":
    im1 = Image.open(sys.argv[1])
    im2 = Image.open(sys.argv[2])
    im,im2 = normalizeImages((im1,im2))
    h1 = buildHisto(im1)
    h2 = buildHisto(im2)
    print(bhattacharyya3channels(h1, h2))
    print(hellinger3channels(h1, h2))