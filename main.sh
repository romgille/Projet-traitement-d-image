#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

echo "Fichier,Bhattacharyya,Formes,Hue,Saturation,Value" > csv/valeurs.csv

for i in photos/*
do
  scripts-shell/run.sh photos/original.jpg $i #>> rapport/rapport_particulier/rapport.md
done


#
# read -p "Voulez-vous télécharger 'texlive-base' pour avoir un rapport badass créé juste pour vous? [y/N]" choice
# case "$choice" in
#   y|Y ) sudo apt-get install texlive-base;;
#   * ) echo "Tant pis, vous aurez un rapport général avec nos photos";;
# esac

exit 0
