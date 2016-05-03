import csv
from variables import csvPath

with open(str(csvPath) + "/" + 'valeurs.csv', 'r') as f:
    r = csv.reader(f)
    l = list(r)

    file = open(str(csvPath) + "/" + 'moyenne.csv', 'w')
    file.write("Fichier,Moyenne" + "\n")
for i in range(1, len(l)):
    file.write(l[i][0] + "," + str((float(l[i][1]) + float(l[i][2]))/2) + "\n")
file.close()
