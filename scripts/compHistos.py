from PIL import Image
import sys
from fonctions import comparaisonHisto3channels
from fonctions import buildHistogram

ims = [Image.open(f) for f in sys.argv[1:]]
<<<<<<< HEAD
for i in range(0, len(ims)-1):
    if(ims[i].mode == ims[i+1].mode):
        histo1 = buildHistogram(ims[0])
        histo2 = buildHistogram(ims[1])
        cmpHisto = comparaisonHisto3channels(histo1, histo2, 2)
        print(cmpHisto)
        if cmpHisto <= 10:
            print("Ces deux images ont moins de 10 % de difference en terme de couleurs, on peut donc considerer qu'elles se ressemblent au niveau couleur.")
        else:
            print("Ces deux images ont plus de 10 % de difference en terme de couleurs, on peut donc considerer qu'elles ne se ressemblent pas au niveau couleur.")
    else:
        print("Les deux images ne sont pas du meme type (RGB ou nuance de gris)")
=======
if(ims[0].mode == ims[1].mode):
    histo1 = buildHistogram(ims[0])
    histo2 = buildHistogram(ims[1])
    cmpHisto = comparaisonHisto3channels(histo1, histo2, 2)
    print(cmpHisto, end="")
>>>>>>> 458dc6b21a8ef21a5b0ab793b77153439c20e715
