from neurone import Neurone
from neuronePremier import NeuronePremier
from couche import Couche
from random import*

class CoucheFinale(Couche):     
    # Constructeur 
    def __init__(self , couche:Couche):
        self.preCouche = couche # On lui affecte la couche précédente afin de pouvoir remonter dans le réseau de neurone à partir de la couche finale
        dict={} # Initialisation d'un dictionnaire vide (tableau associatif)
        # Pour chaque neurone de la couche précédente
        for j in self.preCouche.liste_neurone :
            dict[j]=uniform(-0.5,0.5) #Initialisation des poids avec des valeurs aléatoires
        self.neurone=(Neurone(dict)) # Etant donné qu'il y a qu'un seul neurone la couche final n'a qu'un seul attribut neurone 

    # Méthode pour afficher la liste de neurone
    def afficherListe(self) :
        print("     Neurone final")
        self.neurone.afficherListe()

    # fonction pour initier le calcul de la Sigmoide par appel la méthode de calculSgmoide de neurone
    def initierCalcul(self,paramSigmoide:float) :
        self.neurone.calculSigmoide(paramSigmoide)
    
    # Méthode pour initier le calcul de l'erreur par appel de la méthode de calculErreur du neurone
    def propagationErreur(self,valAtt:float,paramSigmoide:float):
        self.neurone.calculErreurAttendue(valAtt)
        liste=[]
        liste.append(self.neurone)
        self.preCouche.propagationErreur(liste,paramSigmoide) # Propagation de la correction d'erreur dans la couche précédente

    # Méthode pour initier le calcul de l'erreur Batch par appel de la méthode de calculErreurBatch du neurone
    def propagationErreurBatch(self,valAtt:float,paramSigmoide:float):
        self.neurone.calculErreurAttendue(valAtt)
        liste=[]
        liste.append(self.neurone)
        self.preCouche.propagationErreurBatch(liste,paramSigmoide) # Propagation du calcul de l'erreur dans la couche précédente

    # Méthode pour initier la correction du poid par appel de la méthode correctionPoids du neurone
    def propagationErreurCorrection(self,coeffApp:float):
        self.neurone.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp) # Propagation de la correction d'erreur dans la couche précédente
