#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

rm -v rapport.md

for i in photos/*
do
  echo "Comparaison de la photo originale avec $i"
  ./run.sh photos/original.jpg $i >> rapport.md
done

if which pandoc == "pandoc not found"
then
  echo "Vous n'avez pas pandoc, vous pouvez regarder le résultat dans le fichier rapport.md"
else
  echo "Vous avez pandoc ! On va convertir rapport.md en PDF"
  echo "Création du rapport en PDF"
  pandoc rapport.md -V geometry:margin=1in -o rapport.pdf
fi

exit 0
