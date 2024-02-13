from neurone import Neurone
from couche import Couche
from random import*

class CoucheFinale(Couche):      
    def __init__(self , couche:Couche):
        self.preCouche = couche
        dict={}
        for j in self.preCouche.liste_neurone :
            dict[j]=uniform(0,2) #Initialisation des poids avec des valeurs aléatoires
            dict[j] = round(dict[j], 2)
        self.neurone=(Neurone(dict))

    def afficherListe(self) :
        print("Neurone final")
        self.neurone.afficherListe()

    def initierCalcul(self) :
        self.neurone.calculSigmoide()

    def propagationErreur(self,valAtt:float):
        self.neurone.calculErreurAttendue(valAtt)
        liste=[]
        liste.append(self.neurone)
        self.preCouche.propagationErreur(liste)

    def propagationErreurCorrection(self,coeffApp:float):
        self.neurone.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp)
