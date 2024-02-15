from reseau import Reseau
from pickle import load, dump
from io import BytesIO
import sys
import csv

fileSave="Save/"+str(sys.argv[1])
fileName=str(sys.argv[2])

fSave = open(fileSave,'rb')

if(fSave):
    reseau = load(fSave)
    reseau.afficherRéseau()
else:
    print("ERROR : Fichier introuvable\n")

fSave.close()

with open(fileName, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        for i in range(len(row)):
            row[i]=float(row[i])
        valAtt=row[0]
        del row[0]
        reseau.modifierListeDeDonnee(row)
        reseau.modifierValAtt(valAtt)
        reseau.initierCalcul()
        reseau.afficherListeDonnee()
        print("Valeur attendue : "+str(valAtt)+" Resultat : "+str((reseau.coucheFinale.neurone.getValeur())))

