from neurone import Neurone
from neuronePremier import NeuronePremier
import couche
from random import*

# La classe couche

class Couche:      
    def __init__(self , couche:couche, nbNeurone:int):
        self.preCouche = couche
        self.liste_neurone=[]
        for i in range(nbNeurone):
            dict={}
            if type(self.preCouche.liste_neurone)==list:
                for j in self.preCouche.liste_neurone :
                    dict[j]=round(uniform(-1,1),2) #Initialisation des poids avec des valeurs aléatoires
                self.liste_neurone.append(Neurone(dict))

    def afficherListe(self) :
        itNeu=0
        if type(self.liste_neurone)==list:
            for x in self.liste_neurone:
                itNeu=itNeu+1
                print("Neurone "+str(itNeu))
                x.afficherListe()

    def initierCalcul(self,paramSigmoide) :
        for x in self.liste_neurone:
            x.calculSigmoide(paramSigmoide)

    def propagationErreur(self,liste:list,paramSigmoide:float):
        for neur in self.liste_neurone:
            neur.calculErreur(liste,paramSigmoide)
        self.preCouche.propagationErreur(self.liste_neurone,paramSigmoide)
        
    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp)