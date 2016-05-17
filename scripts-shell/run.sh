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
      echo -e "\n"
      echo "Comparaison de $A et $B"
      echo ""
    else
      echo "Votre deuxième fichier à comparer n'existe pas"
      exit 0
    fi
  else
    echo "Votre premier fichier à comparer n'existe pas"
    exit 0
  fi
else
     echo "Vous ne pouvez comparer que deux images"
     exit 0

fi
(scripts-shell/progressBar.sh 10) &

(echo -n $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/compHistos.py $1 $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/cmpSobel.py $1 $2 >> csv/valeurs.csv
echo -n "," >> csv/valeurs.csv
python3 scripts/toHSV.py $1 $2 >> csv/valeurs.csv
echo >> csv/valeurs.csv)
