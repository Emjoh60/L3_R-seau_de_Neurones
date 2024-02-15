from neurone import Neurone
from neuronePremier import NeuronePremier
from couche import Couche
from random import*

class CoucheInitiale(Couche):
    def __init__(self, listeValeur:list,nbNeurone:int):
        self.listeValeur = listeValeur.copy()
        self.liste_neurone = []
        for i in range(nbNeurone):
            self.liste_neurone.append(NeuronePremier(self.listeValeur))
            for j in range(len(self.listeValeur)):
                w=round(uniform(-1,1),2) #Initialisation des poids avec des valeurs aléatoires
                tab=[]
                tab.append(self.listeValeur[j])
                tab.append(w)
                self.liste_neurone[i].listeEntree.append(tab)
            
    def propagationErreur(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreur(liste,paramSigmoide)
    
    def propagationErreurBatch(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreurBatch(liste,paramSigmoide)

    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
    
    def modifierListeValeur(self,listeDonnee:list):
        self.listeValeur=listeDonnee.copy()
        for neur in self.liste_neurone:
            for j in range(len(self.listeValeur)):
                neur.listeEntree[j][0]=self.listeValeur[j]