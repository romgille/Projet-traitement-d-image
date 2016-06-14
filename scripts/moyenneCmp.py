from cmpImages import cmpImages
from compHistos import cmpHistos
from cmpSobel import cmpSobel


def moyenneCmp():
    moyenne = (cmpImages + cmpHistos + cmpSobel) / 3
    return moyenne
