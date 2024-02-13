from neurone import Neurone
from couche import Couche
from random import*

class CoucheInitiale(Couche):
    def __init__(self, listeValeur:list,nbNeurone:int):
        self.listeValeur = listeValeur.copy()
        self.liste_neurone = []
        for i in range(nbNeurone):
            dict={}
            for j in self.listeValeur :
                dict[j]=uniform(0,2) #Initialisation des poids avec des valeurs aléatoires
                dict[j] = round(dict[j], 2)
            self.liste_neurone.append(Neurone(dict))

    def propagationErreur(self,liste:list):
        for neur in self.liste_neurone:
            neur.calculErreur(liste)

    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
            
