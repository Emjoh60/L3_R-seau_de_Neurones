from reseau import Reseau
from pickle import load, dump
from io import BytesIO
import sys
import csv
import os.path
from os import path

try:
    fileSave="Save/"+str(sys.argv[1]) # Nom du fichier de sauvegarde
    fileName=str(sys.argv[2]) # Nom du fichier contenant les données
    nbCouche=int(sys.argv[3]) # Nombre de couche
    tauxApp=float(sys.argv[4]) # Taux d'apprentissage
    paramSigmoide=float(sys.argv[5]) # Paramètre de la Sigmoide
    margeErreur=float(sys.argv[6]) # Marge d'erreur
    cpt=0
except:
    print("ERREUR DE SAISIE !\nFormat attendu :python3 apprentissage.py FileSave DataFile NombreCouche TauxApprentissage ParamSigmoide MargeErreur")
    exit(1)

# Si le fichier existe alors on l'ouvre et on modifie ces paramètres
if(path.exists(fileSave)):
    fSave = open(fileSave,'rb')
    reseau = load(fSave)
    reseau.modifierTauxApp(tauxApp)
    reseau.modifierParamSigmoide(paramSigmoide)
    reseau.modifierMargeErreur(margeErreur)
    fSave.close()
    premier=False
# Sinon on créera un réseau de neurone
else:
    premier=True

with open(fileName, 'r') as file:   # Lecture de chaque du fichier csv
    reader = csv.reader(file, delimiter=';')    # séparation des données par des ";"
    for row in reader:
        for i in range(len(row)):
            row[i]=float(row[i])
        valAtt=row[0]
        del row[0]
        # Si aucun réseau n'existait auparavant on le crée
        if(premier):
            reseau=Reseau(row,nbCouche,tauxApp,valAtt,paramSigmoide,margeErreur)
            premier=False
            reseau.afficherRéseau()
        # Sinon on modifie les valeurs
        else:
            reseau.modifierListeDeDonnee(row)
            reseau.modifierValAtt(valAtt)
        # Calcul des valeurs de sortie et correction de celle ci
        reseau.afficherListeDonnee()
        reseau.initierCalcul()
        reseau.initierCorrection()

fSave = open(fileSave,'wb')

# serialization
if(fSave):
    reseau = dump(reseau,fSave)
    
fSave.close()