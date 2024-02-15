from reseau import Reseau
from pickle import load, dump
from io import BytesIO
import sys
import csv
import os.path
from os import path

fileSave="Save/"+str(sys.argv[1])
fileName=str(sys.argv[2])
nbCouche=int(sys.argv[3])
tauxApp=float(sys.argv[4])
paramSigmoide=float(sys.argv[5])
margeErreur=float(sys.argv[6])
cpt=0

if(path.exists(fileSave)):
    fSave = open(fileSave,'rb')
    reseau = load(fSave)
    reseau.modifierTauxApp(tauxApp)
    reseau.modifierParamSigmoide(paramSigmoide)
    reseau.modifierMargeErreur(margeErreur)
    fSave.close()
    premier=False
else:
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
        if(cpt==10):
            reseau.initierCorrectionBatch(True)
            cpt=0
        else:
            reseau.initierCorrectionBatch(False)
            cpt=cpt+1

fSave = open(fileSave,'wb')

if(fSave):
    reseau = dump(reseau,fSave)
    
fSave.close()