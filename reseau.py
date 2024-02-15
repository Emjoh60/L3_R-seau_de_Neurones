from couche import Couche
from coucheFinale import CoucheFinale
from coucheInitiale import CoucheInitiale

class Reseau:
    def __init__(self, listeDonnee:list, nbCouche:int,tauxApp:float,valAtt:float,paramSigmoid:float,margeErreur:float):
        self.valAttendue=valAtt
        self.tauxApprentissage=tauxApp
        self.paramSigmoide=paramSigmoid
        self.margeErreur=margeErreur
        self.listeDonnee = listeDonnee.copy()
        self.listeCouche=[]
        self.coucheInitiale=CoucheInitiale(self.listeDonnee, nbCouche)
        for i in range(0,nbCouche-1):
            if(i==0):
                self.listeCouche.append(Couche(self.coucheInitiale, nbCouche-i-1))
            else:
                self.listeCouche.append(Couche(self.listeCouche[i-1], nbCouche-i))
        if(nbCouche<2):
            self.coucheFinale=CoucheFinale(self.coucheInitiale)
        else:
            self.coucheFinale=CoucheFinale(self.listeCouche[nbCouche-2])

    def modifierListeDeDonnee(self, listeDonnee:list):
        self.listeDonnee = listeDonnee.copy()
        self.coucheInitiale.modifierListeValeur(self.listeDonnee)

    def modifierTauxApp(self, tauxApp:float):
        self.tauxApprentissage = tauxApp

    def modifierValAtt(self, valAtt:float):
        self.valAttendue = valAtt

    def modifierParamSigmoide(self, paramSigmoide:float):
        self.paramSigmoide=paramSigmoide

    def modifierMargeErreur(self, margeErreur:float):
        self.margeErreur=margeErreur

    def getErreur(self):
        return self.coucheFinale.neurone.getErreur()
        
    def afficherListeDonnee(self) :
        itInt=0
        for x in self.listeDonnee :
            itInt=itInt+1
            print("Entrée "+str(itInt)+" : "+str(x))

    def afficherRéseau(self) :
        print("Affichage des entrées : ")
        self.afficherListeDonnee()
        print("Affichage de la couche initiale")
        self.coucheInitiale.afficherListe()
        it=0
        for cou in self.listeCouche:
            print("Affichage de la couche "+str(it))
            cou.afficherListe()
            it=it+1
        print("Affichage de la couche final")
        self.coucheFinale.afficherListe()

    def initierCalcul(self):
        self.coucheInitiale.initierCalcul(self.paramSigmoide)
        for x in self.listeCouche:
            x.initierCalcul(self.paramSigmoide)
        self.coucheFinale.initierCalcul(self.paramSigmoide)
        print("Résultat : "+str(self.coucheFinale.neurone.getValeur()))

    def initierCorrection(self):
        self.coucheFinale.propagationErreur(self.valAttendue,self.paramSigmoide)
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur())+" Marge : "+str(self.margeErreur))
        if(self.coucheFinale.neurone.getValeur()>(self.valAttendue+self.margeErreur) or self.coucheFinale.neurone.getValeur()<(self.valAttendue-self.margeErreur)):
            print("Correction")
            self.coucheFinale.propagationErreurCorrection(self.tauxApprentissage)

    def initierCorrectionBatch(self,correct:bool):
        self.coucheFinale.propagationErreur(self.valAttendue,self.paramSigmoide)
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur())+" Marge : "+str(self.margeErreur))
        if(correct):
            print("Correction")
            self.coucheFinale.propagationErreurCorrection(self.tauxApprentissage)