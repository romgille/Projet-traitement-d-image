#!/bin/bash

# Supprimer tous les histogrammes créés précedemment
rm histogrammes/* -rv

for args in $@
do
  
  # Créer les histogrammes des images concernés
  python scripts/histogramme.py $args
  echo "Histogramme de $args créé"

  

done
