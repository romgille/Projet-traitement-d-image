# Projet-traitement-d-image
Projet de E2 traitement d'image en python

Contributeurs : Romain Gille (romgille), Yannick Ezvan (nonock).

##But du programme

Faire la comparaison entre deux images et dire ce qui se ressemble et ce qui
diffère.

##Critères de ressemblance :

* Comparaison des histogrammes RGB
* Comparaison des images sous le filtre de sobel
* Différence entre les deux images pixel par pixel

##Déroulement du programme

Les images sont cherchés dans le dossier `photos/`.

La photo ayant pour nom `original.jpg` est la photo à laquelle sera comparée
toutes les autres photos présentes dans le dossier.

Un histogramme pour chaque photo dans le dossier `histogramme/`.

Ces histogrammes servent à calculer la distance de Bhattacharyya pour les
différentes photos.

Ensuite, les images sont comparées pixel à pixel sur leurs couleurs.

À partir des photos initiales, on crée ensuite des sobels qui sont stockés dans
le dossier `sobel/` et sont ensuite comparés pixel à pixel pour permettre de
détecter leur différence de formes.

Enfin, tous ces résultats sont lors du déroulement du programme écrites dans le
fichier `rapport/rapport_particulier/rapport.md`. Le programme propose à la fin
de créer un PDF avec ce fichier pour avoir un meilleur rendu.

**La distance de Bhattacharyya** est une mesure de la similarité de deux
distributions de probabilités discrètes. On la calcule après création
d’histogrammes pour chaque image.

**Le filtre de Sobel** permet une détection des contours. Nous comparons
ensuite les deux images créées avec le filtre de Sobel pixel à pixel pour avoir
une comparaison des contours et donc des formes présentes sur la photo.


##Liens photos :
[Originale](http://farm9.static.flickr.com/8329/8086409595_92b9bb908a_b.jpg)
