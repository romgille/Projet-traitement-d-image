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
    read -p "Voulez-vous créer le PDF (y/n)?" choice
        case "$choice" in
            y|Y ) echo "Création du pdf";
                  pandoc rapport/rapport_particulier/rapport.md -V geometry:margin=1in -o Rapport.pdf;;

            n|N ) echo "Ok pas de soucis";;
            * ) echo "Répondez par 'y' ou 'n'";;
        esac
else
    echo "pandoc n'est pas installé, le PDF ne pourra pas être créé. Vous pouvez l'installer via le paquet 'pandoc'"
fi;

exit 0
