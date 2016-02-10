#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

for i in photos/*
do
  echo "Comparaison de la photo originale avec $i"
  ./run.sh photos/original.jpg $i >> rapport.md
done

#echo "Création du rapport en pdf"
#pandoc rapport.md -V geometry:margin=1in -o rapport.pdf

echo "Suppression du markdown de rapport"
rm rapport.md

exit 0
