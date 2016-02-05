#!/bin/bash

if test $# == 2
then
     echo "Traitement des images en cours"
else
     echo "Vous ne pouvez comparer que deux images"
     exit 0

fi

# --- HISTOGRAMMES ---
# Supprimer tous les histogrammes créés précedemment
rm histogrammes/* -rv

for args in $@
do
  
  # Créer les histogrammes des images concernés
  python scripts/histogramme.py $args
  echo "Histogramme de $args créé"

done

# --- COMPARAISON COULEUR PIXELS ---
# Compare le nombre de pixels différents dans les images
python scripts/cmpImages.py $1 $2

exit 0