from neurone import Neurone
from neuronePremier import NeuronePremier
import couche
from random import*

class Couche:      
    
    # Constructeur
    def __init__(self , couche:couche, nbNeurone:int):
        self.preCouche = couche # On lui affecte la couche précédente afin de pouvoir remonter dans le réseau de neurone à partir de la couche finale
        self.liste_neurone=[] # Initialisation de liste vide
        # Création de nb neurones 
        for i in range(nbNeurone):
            dict={} # Initialisation d'un dictionnaire vide (tableau associatif)
            if type(self.preCouche.liste_neurone)==list: # Vérification du type
                # Pour chaque neurone de la couche précédente 
                for j in self.preCouche.liste_neurone :
                    dict[j]=uniform(-0.5,0.5) #Initialisation des poids avec des valeurs aléatoires à l'index du neurone
                self.liste_neurone.append(Neurone(dict)) # Ajout du neurone nouvellement créer dans la liste de neurone

    # Méthode pour afficher la liste de neurone
    def afficherListe(self) :
        itNeu=0
        if type(self.liste_neurone)==list:
            for x in self.liste_neurone:
                itNeu=itNeu+1
                print("     Neurone "+str(itNeu))
                x.afficherListe() # Appel de la méthode afficherListe de chaque neurone

    # fonction pour initier le calcul de la Sigmoide par appel la méthode de calculSgmoide de neurone
    def initierCalcul(self,paramSigmoide) :
        for x in self.liste_neurone:
            x.calculSigmoide(paramSigmoide)

    # Méthode pour initier le calcul de l'erreur par appel de la méthode de calculErreur de chaque neurone
    def propagationErreur(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreur(liste,paramSigmoide)
        self.preCouche.propagationErreur(self.liste_neurone,paramSigmoide) # Propagation de la correction d'erreur dans la couche précédente
    
    # Méthode pour initier le calcul de l'erreur Batch par appel de la méthode de calculErreurBatch de chaque neurone    
    def propagationErreurBatch(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreurBatch(liste,paramSigmoide)
        self.preCouche.propagationErreurBatch(self.liste_neurone,paramSigmoide) # Propagation du calcul de l'erreur dans la couche précédente
    
    # Méthode pour initier la correction du poid par appel de la méthode correctionPoids de chaque neurone
    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp) # Propagation de la correction d'erreur dans la couche précédente