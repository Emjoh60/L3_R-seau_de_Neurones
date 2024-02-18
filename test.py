from reseau import Reseau
from pickle import load, dump
from io import BytesIO
import sys
import csv

fileSave="Save/"+str(sys.argv[1]) # Nom du fichier de sauvegarde
fileName=str(sys.argv[2]) # Nom du fichier contenant les données

fSave = open(fileSave,'rb') # Ouverture du fichier contenant l'intelligence artificielle que l'on souhaite entrainer

if(fSave):
    reseau = load(fSave) # Récupération du réseau de neurone 
    reseau.afficherRéseau() # Afficher le réseau
else:
    print("ERROR : Fichier introuvable\n") # Dans le cas où le fichier n'existe pas on renvoie un msg d'erreur

fSave.close() # Fermeture du fichier 

# Test du programme dur différent jeux de données contenu dans le fichier csv
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

