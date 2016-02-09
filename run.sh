#!/bin/bash

if test $# == 2
then
  if test -f $1
  then
    if test -f $2
    then
      echo ""
      echo "Traitement des images en cours"
      echo ""
    else
      echo "Votre deuxième fichier à comparer n'existe pas"
      exit 0
    fi
  else
    echo "Votre premier fichier à comparer n'existe pas"
    exit 0
  fi
else
     echo "Vous ne pouvez comparer que deux images"
     exit 0

fi

## --- HISTOGRAMMES ---
## Supprimer tous les histogrammes créés précedemment
#echo "Suppression des histogrammes et sobels précédents :"
#rm histogrammes/* -rv
#rm sobel/* -rv

for args in $@
do
  
  # Créer les histogrammes des images concernés
  python scripts/histogramme.py $args
  echo ""
  echo "Histogramme de $args créé dans histogrammes/"
  echo ""

done

  # Comparer les histogrammes
  echo "Distance de Bhattacharyya :"
  python scripts/compHistos.py $1 $2

# --- COMPARAISON COULEUR PIXELS ---
# Compare le nombre de pixels différents dans les images
echo ""
echo "Différence pixel à pixel :"
python scripts/cmpImages.py $1 $2

# --- COMPARAISON SOBEL ---
# Compare le nombre de pixels différents dans les images en sobel
echo ""
echo "Sobel de $1 créé dans sobel/"
echo "Sobel de $2 créé dans sobel/"
echo ""
echo "Différence pixel à pixel en sobel :"
python scripts/cmpSobel.py $1 $2

exit 0
