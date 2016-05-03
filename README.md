# Projet-traitement-d-image
Projet de E2 traitement d'image en python

Contributeurs : Romain Gille (romgille), Yannick Ezvan (nonock).

##But du programme

Faire la comparaison entre deux images et dire ce qui se ressemble et ce qui diffère.

##Critères de ressemblance :

* Comparaison des histogrammes RGB
* Comparaison des images sous le filtre de sobel
* Différence entre les deux images pixel par pixel

##Déroulement du programme

* Test du nombre d'images passé en arguments
* Création des histogrammes des images concernées
* Comparaison des histogrammes en différents facteurs
* Comparaison de la différence des images
(D'autre à venir)


**Comparer deux images :**

* Colorimétrie (Histogramme) distance de Bhattacharyya
* Position des formes avec filtre de sobel
* Différence pixel par pixel


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

##Liens photos :
[Originale](http://farm9.static.flickr.com/8329/8086409595_92b9bb908a_b.jpg)
