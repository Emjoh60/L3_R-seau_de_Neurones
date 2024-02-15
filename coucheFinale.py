from neurone import Neurone
from neuronePremier import NeuronePremier
from couche import Couche
from random import*

class CoucheFinale(Couche):      
    def __init__(self , couche:Couche):
        self.preCouche = couche
        dict={}
        for j in self.preCouche.liste_neurone :
            dict[j]=round(uniform(-1,1),2) #Initialisation des poids avec des valeurs aléatoires
        self.neurone=(Neurone(dict))

    def afficherListe(self) :
        print("Neurone final")
        self.neurone.afficherListe()

    def initierCalcul(self,paramSigmoide:float) :
        self.neurone.calculSigmoide(paramSigmoide)

    def propagationErreur(self,valAtt:float,paramSigmoide:float):
        self.neurone.calculErreurAttendue(valAtt)
        liste=[]
        liste.append(self.neurone)
        self.preCouche.propagationErreur(liste,paramSigmoide)

    def propagationErreurBatch(self,valAtt:float,paramSigmoide:float):
        self.neurone.calculErreurAttendue(valAtt)
        liste=[]
        liste.append(self.neurone)
        self.preCouche.propagationErreurBatch(liste,paramSigmoide)

    def propagationErreurCorrection(self,coeffApp:float):
        self.neurone.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp)
