from reseau import Reseau
from pickle import load, dump
from io import BytesIO
import sys
import csv

fileName=str(sys.argv[1])
fileName=str(sys.argv[1])
nbCouche=int(sys.argv[2])
tauxApp=float(sys.argv[3])
paramSigmoide=float(sys.argv[4])
margeErreur=float(sys.argv[5])
premier=True

with open(fileName, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        for i in range(len(row)):
            row[i]=float(row[i])
        valAtt=row[0]
        del row[0]
        if(premier):
            reseau=Reseau(row,nbCouche,tauxApp,valAtt,paramSigmoide,margeErreur)
            premier=False
            reseau.afficherRéseau()
        else:
            reseau.modifierListeDeDonnee(row)
            reseau.modifierValAtt(valAtt)
        reseau.afficherListeDonnee()
        reseau.initierCalcul()
        reseau.initierCorrection()



