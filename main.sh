#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

echo "Fichier,Bhattacharyya,Formes,Hue,Saturation,Value" > valeurs.csv

for i in photos/*
do
  echo "Comparaison de la photo originale avec $i"
  ./run.sh photos/original.jpg $i >> rapport.md
done


#
# read -p "Voulez-vous télécharger 'texlive-base' pour avoir un rapport badass créé juste pour vous? [y/N]" choice
# case "$choice" in
#   y|Y ) sudo apt-get install texlive-base;;
#   * ) echo "Tant pis, vous aurez un rapport général avec nos photos";;
# esac

exit 0
