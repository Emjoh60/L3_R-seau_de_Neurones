from neurone import Neurone
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
                    dict[j]=uniform(0,2) #Initialisation des poids avec des valeurs aléatoires
                    dict[j] = round(dict[j], 2)
                self.liste_neurone.append(Neurone(dict))

    def afficherListe(self) :
        itNeu=0
        if type(self.liste_neurone)==list:
            for x in self.liste_neurone:
                itNeu=itNeu+1
                print("Neurone "+str(itNeu))
                x.afficherListe()

    def initierCalcul(self) :
        for x in self.liste_neurone:
            x.calculSigmoide()

    def propagationErreur(self,liste:list):
        for neur in self.liste_neurone:
            neur.calculErreur(liste)
        self.preCouche.propagationErreur(self.liste_neurone)
        
    def propagationErreurCorrection(self,coeffApp:float):
        for neurPrec in self.liste_neurone:
            neurPrec.correctionPoids(coeffApp)
        self.preCouche.propagationErreurCorrection(coeffApp)