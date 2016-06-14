#         valG = []
#         valB = []
#         for y in range(0, im.size[1]):
#             valR = pix[x, y][0]
#             valG = pix[x, y][1]
#             valB = pix[x, y][2]
#             if 0 <= valR <= 32 and 0 <= valG <= 32 and 0 <= valB <= 32:
#                 comp = comp + 0
#             else:
#                 comp = comp + 1
#     prcentge = (comp/taille)*100
#     prcentge = round(prcentge, 2)
#     return prcentge

# def comparaisonImage3channels(im1, im2, facteur):
#     newIm1, newIm2 = normalize([im1, im2])
#     histo1 = buildHistogram(newIm1)
#     histo2 = buildHistogram(newIm2)
#     return comparaisonHisto3channels(histo1, histo2, facteur)

# def comparaisonImage3channels2(im1, im2, facteur):
#     newIm1, newIm2 = normalize([im1, im2])
#     histo1 = buildHistogram(newIm1)
#     histo2 = buildHistogram(newIm2)
#     return comparaisonHisto3channels2(histo1, histo2, facteur)

# def drawPixel(im, x, y, color):
#     pix = im.load()
#     pix[x, y] = color
#
#
# def drawHLine(im, y, color):
#     pix = im.load()
#     for i in range(0, im.size[1], 1):
#         pix[i, y] = color
#
#
# def drawVLine(im, x, color):
#     pix = im.load()
#     for i in range(0, im.size[0], 1):
#         pix[x, i] = color
#
#
# def drawRectangle(im, x, y, w, h, color):
#     pix = im.load()
#     for i in range(x, x+w):
#         for j in range(y, y+h):
#             pix[i, j] = color
#
#
# def increaseValues(im, dec):
#     pix = im.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = pix[i, j]
#             pix[i, j] = (val[0] + dec, val[1] + dec, val[2] + dec)
#
#
# def reverseChannels(im):
#     pix = im.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = pix[i, j]
#             pix[i, j] = (val[2], val[1], val[0])
#
#
# def inverseValues(im):
#     pix = im.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = pix[i, j]
#             pix[i, j] = (255-val[0], 255-val[1], 255-val[2])
#
#
# def buildLookUpTable(start, stop):
#     lut = []
#     for i in range(0, 256):
#         Pi = (i/255.)   # Pourcentage avancement
#         startpi = (1-Pi)
#         lut.append((int(round(start[0]*startpi)) + int(round(stop[0]*Pi)),
#                     int(round(start[1]*startpi)) + int(round(stop[1]*Pi)),
#                     int(round(start[2]*startpi)) + int(round(stop[2]*Pi))))
#     # print(lut)
#     return lut
#
#
# def applyLookUpTable(im, lut):
#     newIm = Image.new("RGB", (im.size[0], im.size[1]))
#     pix = im.load()
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = list(pix[i, j])
#             pix1[i, j] = lut[val[0]]
#     return newIm
#
#
# def vFlip(im):
#     pix = im.load()
#     newIm = Image.new("RGB", (im.size[0], im.size[1]))
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             pix1[im.size[0]-1-i, im.size[1]-1-j] = pix[i, j]
#     return newIm
#
#
# def hFlip(im):
#     pix = im.load()
#     newIm = Image.new("RGB", (im.size[0], im.size[1]))
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             x = fabs(i - im.size[0]-1)
#             if x > im.size[0] - 1:
#                 x = im.size[0] - 1
#             pix1[x, j] = pix[i, j]
#     return newIm
#
#
# def rotate(im):
#     pix = im.load()
#     newIm = Image.new("RGB", (im.size[1], im.size[0]))
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = pix[i, j]
#             pix1[im.size[1]-1-j, im.size[0]-1-i] = val
#     return newIm
#
#
# def translate(im, dec):
#     pix = im.load()
#     newIm = Image.new("RGB", (im.size[0], im.size[1]))
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             decI = i + dec[0]
#             decJ = j + dec[1]
#             if(decI > newIm.size[0]):
#                 decI = decI - newIm.size[0]
#             if(decJ > newIm.size[1]):
#                 decJ = decJ - newIm.size[1]
#             if(decI < newIm.size[0] and decJ < newIm.size[1]):
#                 pix1[decI, decJ] = pix[i, j]
#     return newIm
#
#
# def zoom(im, factor):
#     pix = im.load()
#     newIm = Image.new("RGB", (im.size[0] * factor, im.size[1] * factor))
#     pix1 = newIm.load()
#     for i in range(0, im.size[0]*factor):
#         for j in range(0, im.size[1]*factor):
#             pix1[i, j] = pix[i/factor, j/factor]
#     return newIm
#
#
# def zoomAndCrop(im, factor):
#     newIm = zoom(im, factor)
#     newIm2 = crop(newIm, (newIm.size[0]-im.size[0])/2,
#                         (newIm.size[1]-im.size[1])/2, im.size[0], im.size[1])
#     return newIm2
#
#
# def blur(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             somme = 0
#             count = 0
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     val = pix[k, l]
#                     somme = somme + val
#                     count += 1
#             rpix[i, j] = somme/count
#     return result
#
#
# def dilate(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             maxV = 0
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     val = pix[k, l]
#                     if(maxV < val):
#                         maxV = val
#             rpix[i, j] = maxV
#     return result
#
#
# def erode(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             minV = 255
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     val = pix[k, l]
#                     if(minV > val):
#                         minV = val
#             rpix[i, j] = minV
#     return result
#
#
# def median(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = []
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     val.append(pix[k, l])
#                 val.sort()
#             rpix[i, j] = val[len(val)//2]
#     return result
#
#
# def maxFilter(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(0, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = []
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     if(k == i) and (l == j):
#                         continue
#                     val.append(pix[k, l])
#                 val.sort()
#             if pix[i, j] > val[-1]:
#                 rpix[i, j] = val[-1]
#             else:
#                 rpix[i, j] = pix[i, j]
#     return result
#
#
# def minFilter(im, radius):
#     pix = im.load()
#     result = Image.new("L", im.size)
#     rpix = result.load()
#     for i in range(1, im.size[0]):
#         for j in range(0, im.size[1]):
#             val = []
#             for k in range(i - radius, i + radius+1):
#                 for l in range(j - radius, j + radius+1):
#                     kOut = (k < 0) or (k > im.size[0] - 1)
#                     lOut = (l < 0) or (l > im.size[1] - 1)
#                     if kOut or lOut:
#                         continue
#                     if(k == i) and (l == j):
#                         continue
#                     val.append(pix[k, l])
#                 val.sort()
#             if pix[i, j] < val[0]:
#                 rpix[i, j] = val[0]
#             else:
#                 rpix[i, j] = pix[i, j]
#     return result
#
#
# def add(a, b):
#     newA, newB = normalize([a, b])
#     pixA = newA.load()
#     pixB = newB.load()
#     newImage = Image.new("RGB", a.size)
#     pix = newImage.load()
#     for i in range(0, newImage.size[0]):
#         for j in range(0, newImage.size[1]):
#             valA = pixA[i, j]
#             valB = pixB[i, j]
#             pix[i, j] = (valA[0] + valB[0],
#                          valA[1] + valB[1],
#                          valA[2] + valB[2])
#     return newImage
#
#
# def product(a, b):
#     newA, newB = normalize([a, b])
#     pixA = newA.load()
#     pixB = newB.load()
#     type(pixA)
#     newImage = Image.new("RGB", a.size)
#     pix = newImage.load()
#     for i in range(0, newImage.size[0]):
#         for j in range(0, newImage.size[1]):
#             valA = pixA[i, j]
#             valB = pixB[i, j]
#             pix[i, j] = ((valA[0] * valB[0])/255,
#                          (valA[1] * valB[1])/255,
#                          (valA[2] * valB[2])/255)
#     return newImage
#
#
# def copy(a, b, m):
#     newA, newB, newM = normalize([a, b, m])
#     pixA = newA.load()
#     pixB = newB.load()
#     pixM = newM.load()
#     newImage = Image.new("RGB", a.size)
#     pix = newImage.load()
#     for i in range(0, newImage.size[0]):
#         for j in range(0, newImage.size[1]):
#             if pixM[i, j] == (0, 0, 0):
#                 pix[i, j] = pixB[i, j]
#             else:
#                 pix[i, j] = pixA[i, j]
#     return newImage
#
#
# def max(images):
#     imgs = normalize(images)
#     newImage = Image.new("RGB", imgs[0].size)
#     pix = newImage.load()
#     for x in range(0, newImage.size[0]):
#         for y in range(0, newImage.size[1]):
#             valR = []
#             valG = []
#             valB = []
#             for i in imgs:
#                 newPix = i.load()
#                 valR.append(newPix[x, y][0])
#                 valG.append(newPix[x, y][1])
#                 valB.append(newPix[x, y][2])
#             valR.sort()
#             valG.sort()
#             valB.sort()
#             pix[x, y] = (valR[-1], valG[-1], valB[-1])
#     return newImage
#
#
# def min(images):
#     imgs = normalize(images)
#     newImage = Image.new("RGB", imgs[0].size)
#     pix = newImage.load()
#     for x in range(0, newImage.size[0]):
#         for y in range(0, newImage.size[1]):
#             valR = []
#             valG = []
#             valB = []
#             for i in imgs:
#                 newPix = i.load()
#                 valR.append(newPix[x, y][0])
#                 valG.append(newPix[x, y][1])
#                 valB.append(newPix[x, y][2])
#             valR.sort()
#             valG.sort()
#             valB.sort()
#             pix[x, y] = (valR[0], valG[0], valB[0])
#     return newImage
#
#
# def mediane(images):
#     imgs = normalize(images)
#     newImage = Image.new("RGB", imgs[0].size)
#     pix = newImage.load()
#     for x in range(0, newImage.size[0]):
#         for y in range(0, newImage.size[1]):
#             valR = []
#             valG = []
#             valB = []
#             for i in imgs:
#                 newPix = i.load()
#                 valR.append(newPix[x, y][0])
#                 valG.append(newPix[x, y][1])
#                 valB.append(newPix[x, y][2])
#             valR.sort()
#             valG.sort()
#             valB.sort()
#             pix[x, y] = (valR[len(valR)/2],
#                          valG[len(valG)/2],
#                          valB[len(valB)/2])
#     return newImage
#
#
# def avg(images):
#     imgs = normalize(images)
#     newImage = Image.new("RGB", imgs[0].size)
#     pix = newImage.load()
#     for x in range(0, newImage.size[0]):
#         for y in range(0, newImage.size[1]):
#             valR = []
#             valG = []
#             valB = []
#             for i in imgs:
#                 newPix = i.load()
#                 valR.append(newPix[x, y][0])
#                 valG.append(newPix[x, y][1])
#                 valB.append(newPix[x, y][2])
#             r = 0
#             g = 0
#             b = 0
#             for j in range(0, len(valR)-1):
#                 r += valR[j]
#                 g += valG[j]
#                 b += valB[j]
#             pix[x, y] = (r/len(valR), g/len(valG), b/len(valB))
#     return newImage
#
#
# def comparaisonHistoFactor(histoA, histoB, factor):
#     # print histoA
#     hA = normHisto(histoA)
#     hB = normHisto(histoB)
#     distance = 0.
#     for i in range(0, 255):
#         distance += ((fabs(hA[i] - hB[i]))**factor)/len(hA)
#     return distance
#
#
# def comparaisonHisto3channels2(histoA, histoB, factor):
#     result = []
#     finale = 0.
#     for c in range(3):
#         result.append(comparaisonHistoFactor(histoA[c], histoB[c], factor))
#     for i in range(0, 3):
#         finale += result[i]
#     return round((finale * 100.), 2)


# def comparaisonHistoBhattacharyyaHSV(histoA, histoB):
#     hA = normHisto(histoA)
#     hB = normHisto(histoB)
#     distance = 0.
#     for i in range(0, 255):
#         distance += (hA[i] * hB[i]) ** 0.5
#     newDistance = -log(distance)
#     return round((newDistance * 100), 2)

# def toRGB(im):
#     rgb = Image.new("RGB", im.size)
#     pix = im.load()
#     rgbPix = rgb.load()
#     epsilon = 0.00001
#     for Y in range(im.size[1]):
#         for X in range(im.size[0]):
#             h,s,v = pix[X,Y]
#             h*= 3.6/2.55
#             s = s/255.0
#             v = v/255.0
#             c = v*s
#             val = h/60.0
#             x = c*(1.0- abs((val-2*(int(val)/2)) - 1.0))
#             m = v-c
#             r,g,b = c,x,0
#             if 60<=h and h<120:  r,g,b = x,c,0
#             elif 120<=h and h<180:  r,g,b = 0,c,x
#             elif 180<=h and h<240:  r,g,b = 0,x,c
#             elif 240<=h and h<300:  r,g,b = x,0,c
#             elif 300<=h :  r,g,b = c,0,x
#             r,g,b = [int((p+m)*255) for p in (r,g,b) ]
#             rgbPix[X,Y] = r,g,b
#     return rgb

# def diff(a, b):
#     newA, newB = normalize([a, b])
#     pixA = newA.load()
#     pixB = newB.load()
#     type(pixA)
#     newImage = Image.new("RGB", newA.size)
#     pix = newImage.load()
#     for i in range(0, newImage.size[0]):
#         for j in range(0, newImage.size[1]):
#             valA = pixA[i, j]
#             valB = pixB[i, j]
#             pix[i, j] = (abs(valA[0] - valB[0]),
#                          abs(valA[1] - valB[1]),
#                          abs(valA[2] - valB[2]))
#     return newImage

# def compDifImages(im):
#     pix = im.load()
#     comp = 0.
#     taille = im.size[0]*im.size[1]
#     prcentge = 0.
#     for x in range(0, im.size[0]):
#         valR = []
