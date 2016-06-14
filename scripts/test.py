from PIL import Image
import sys
import json


def ImgToJson():
    img = Image.open("original.jpg")
    pix = img.load()
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            print(pix[i][j])
    dic = {'name': "original.jpg"}#, 'load': [pix]}
    with open("json.json", 'w') as outfile:
        json.dump(dic, outfile)

ImgToJson()
