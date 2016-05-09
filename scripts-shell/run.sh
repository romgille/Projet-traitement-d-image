#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

if test $# == 2
then
  if test -f $1
  then
    A=$1
    if test -f $2
    B=$2
    then
      #echo ""
      #echo "\\newpage"
      echo ""
      echo "#Comparaison de $A et $B"
      echo ""
    else
      echo "#Votre deuxième fichier à comparer n'existe pas"
      exit 0
    fi
  else
    echo "#Votre premier fichier à comparer n'existe pas"
    exit 0
  fi
else
     echo "#Vous ne pouvez comparer que deux images"
     exit 0

fi

## --- HISTOGRAMMES ---
## Supprimer tous les histogrammes créés précedemment
#echo "Suppression des histogrammes et sobels précédents :"
#rm histogrammes/* -rv
#rm sobel/* -rv

#for args in $@
#do

  # Créer les histogrammes des images concernés
 # python scripts/histogramme.py $args

#done

echo -n $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/compHistos.py $1 $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/cmpSobel.py $1 $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/toHSV.py $1 $2 >> csv/valeurs.csv
echo >> csv/valeurs.csv

# # Comparer les histogrammes
# echo "## Distance de Bhattacharyya (en %):"
# python scripts/compHistos.py $1 $2
#
# # --- COMPARAISON COULEUR PIXELS ---
# # Compare le nombre de pixels différents dans les images
# echo ""
# echo "## Différence pixel à pixel (en %):"
# python scripts/cmpImages.py $1 $2
#
#
# # --- COMPARAISON SOBEL ---
# # Compare le nombre de pixels différents dans les images en sobel
# echo ""
# echo "## Différence pixel à pixel en sobel (en %):"
# python scripts/cmpSobel.py $1 $2
