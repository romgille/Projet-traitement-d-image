# Projet-traitement-d-image
Projet de E2 traitement d'image en python

Contributeurs : Romain Gille (romgille), Yannick Ezvan (nonock).

**But du programme**

Faire la comparaison entre deux images et dire si elles se ressembles

**Critères de ressemblance :**

* Comparaison des histogrammes RGB                              20%
* Comparaison des histogrammes de luminosités                   20%
* Comparaison des images sous le filtre de sobel                20%
* Comparaison des histogrammes L                                20%
* Différence entre les deux images puis voir si noir partout    20%

**Déroulement du programme**

* Test du nombre d'images passé en arguments
* Création des histogrammes des images concernées
* Comparaison de la différence des images
(D'autre à venir)



Comparer deux images :
* Colorimétrie (Histogramme)
* Luminosité (30% R + 60% G + 10% B)
* Position du sujet (règle des tiers)


# How To

Clone the repository :

`git clone https://github.com/romgille/Projet-traitement-d-image.git`

Run the script :

`./run.sh path/to/file/picture-to-compare1.jpg path/to/file/picture-to-compare2.jpg`

You can try with the picture on `photos/` folder

if it does not work :

`chmod +x run.sh`

and try to run the script again.
