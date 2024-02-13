from couche import Couche
from coucheFinale import CoucheFinale
from coucheInitiale import CoucheInitiale

class Reseau:
    def __init__(self, listeDonnee:list, nbCouche:int,tauxApp:float,valAtt:float):
        self.valAttendue=valAtt
        self.tauxApprentissage=tauxApp
        self.listeDonnee = listeDonnee.copy()
        self.listeCouche=[]
        self.coucheInitiale=CoucheInitiale(self.listeDonnee, nbCouche)
        for i in range(0,nbCouche-1):
            if(i==0):
                self.listeCouche.append(Couche(self.coucheInitiale, nbCouche-i-1))
            else:
                self.listeCouche.append(Couche(self.listeCouche[i-1], nbCouche-i))
        self.coucheFinale=CoucheFinale(self.listeCouche[nbCouche-2])


    def addEntier(self,val:float):
        self.listeDonnee.append(val)

    def removeEntier(self,val:float):
        self.listeDonnee.remove(val)
        
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
        self.coucheInitiale.initierCalcul()
        for x in self.listeCouche:
            x.initierCalcul()
        self.coucheFinale.initierCalcul()
        print("Résultat : "+str(self.coucheFinale.neurone.getValeur()))


    def initierCorrection(self):
        self.coucheFinale.propagationErreur(self.valAttendue)
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur()))

    def initierCorrection(self):
        self.coucheFinale.propagationErreur(self.valAttendue)
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur()))
        self.coucheFinale.propagationErreurCorrection(self.tauxApprentissage)