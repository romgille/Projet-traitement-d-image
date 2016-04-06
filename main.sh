#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

echo "Nom,Bhattacharyya,Formes" > valeurs.csv

for i in photos/*
do
  echo "Comparaison de la photo originale avec $i"
  ./run.sh photos/original.jpg $i >> rapport.md
done

exit 0
