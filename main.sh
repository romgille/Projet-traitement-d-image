#!/bin/bash

set -euo pipefail
IFS=$'\n\t'


rm -fv rapport/rapport_particulier/rapport.md
touch rapport/rapport_particulier/rapport.md

for i in photos/*; do
  echo "Comparaison de la photo originale avec $i"
  ./run.sh photos/original.jpg $i >> rapport/rapport_particulier/rapport.md
done

set +e
which pandoc > /dev/null 2>&1
code=$?
set -e
if [ $code -eq 0 ]; then
    echo "Création du pdf"
    pandoc rapport/rapport_particulier/rapport.md -V geometry:margin=1in -o Rapport.pdf
else
    echo "pandoc n'est pas installé, vous pouvez l'installer via le paquet 'pandoc'"
fi;

exit 0
