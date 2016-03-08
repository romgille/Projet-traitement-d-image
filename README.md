# Projet-traitement-d-image
Projet de E2 traitement d'image en python

Contributeurs : Romain Gille (romgille), Yannick Ezvan (nonock).

##But du programme

Faire la comparaison entre deux images et dire si elles se ressembles

##Critères de ressemblance :

* Comparaison des histogrammes RGB                              20%
* Comparaison des histogrammes de luminosités                   20%
* Comparaison des images sous le filtre de sobel                20%
* Comparaison des histogrammes L                                20%
* Différence entre les deux images puis voir si noir partout    20%

##Déroulement du programme

* Test du nombre d'images passé en arguments
* Création des histogrammes des images concernées
* Comparaison des histogrammes en différents facteurs
* Comparaison de la différence des images
(D'autre à venir)


**Comparer deux images :**

* Colorimétrie (Histogramme)
* Luminosité (30% R + 60% G + 10% B)
* Position du sujet (règle des tiers)


# How To

Clone the repository :

`git clone https://github.com/romgille/Projet-traitement-d-image.git`

Put the picture you want to compare in 'photos' folder, the 'original.jpg'
must be the source picture you want to compare the others with.

## For all the pictures in your "photos" folder :

Run the script :

`./main.sh`

if it does not work, change the mod of the file :

`chmod +x main.sh`

and try to run the script again.

## If you want to choose your pictures to compare :

Run the script :

`./run.sh photos/your-picture1.jpg photos/your-picture2.jpg`

if it does not work, change the mod of the file :

`chmod +x run.sh`

and try to run the script again.
