from neurone import Neurone
from neuronePremier import NeuronePremier
from couche import Couche
from random import*

class CoucheInitiale(Couche):
    
    # Constructeur
    def __init__(self, listeValeur:list,nbNeurone:int):
        self.listeValeur = listeValeur.copy() # On lui affecte la liste d'entrée du réseau puisqu'il s'agit de la première couche du réseau
        self.liste_neurone = [] # Initialisation de liste vide
        # Création de nb neurones 
        for i in range(nbNeurone):
            # Création d'un neurone premier sans liste
            self.liste_neurone.append(NeuronePremier(self.listeValeur))
            # Pour chaque valeur de la liste d'entrée 
            for j in range(len(self.listeValeur)):
                w=uniform(-0.5,0.5) #Initialisation des poids avec des valeurs aléatoires
                # Initialisation d'un tableau contenant deux cases la première une valeur et la deuxième un poid
                tab=[]
                tab.append(self.listeValeur[j])
                tab.append(w)
                # Ajout du tableau à l'indice correspondant à une entrée du réseau
                self.liste_neurone[i].listeEntree.append(tab)
            
    # Méthode pour initier le calcul de l'erreur par appel de la méthode de calculErreur de chaque neurone
    def propagationErreur(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreur(liste,paramSigmoide)
    
    # Méthode pour initier le calcul de l'erreur Batch par appel de la méthode de calculErreurBatch de chaque neurone
    def propagationErreurBatch(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreurBatch(liste,paramSigmoide)

    # Méthode pour initier la correction du poid par appel de la méthode correctionPoids de chaque neurone
    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
    
    # Méthode pour modifier les entrées de la couche initiale
    def modifierListeValeur(self,listeDonnee:list):
        self.listeValeur=listeDonnee.copy() # Remplacement de la liste des valeurs par la liste en paramètre
        # Réaffectation des entrées à chaque neurone sans changer les poids
        for neur in self.liste_neurone:
            for j in range(len(self.listeValeur)):
                neur.listeEntree[j][0]=self.listeValeur[j]