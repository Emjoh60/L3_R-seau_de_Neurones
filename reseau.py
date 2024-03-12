from couche import Couche
from coucheFinale import CoucheFinale
from coucheInitiale import CoucheInitiale

class Reseau:
    
    # Constructeur
    def __init__(self, listeDonnee:list, nbCouche:int,tauxApp:float,valAtt:float,paramSigmoid:float,margeErreur:float):
        self.valAttendue=valAtt # Valeur attendue en sortie du réseau
        self.tauxApprentissage=tauxApp # Taux d'apprentissage
        self.paramSigmoide=paramSigmoid # Paramètre de la fonction Sigmoide (Pour accélérer l'apprentissage)
        self.margeErreur=margeErreur # Marge d'erreur acceptable (permettant de savoir s'il faut initier la correction ou pas)
        self.listeDonnee = listeDonnee.copy() # Liste d'entrée du réseau
        self.listeCouche=[] # Initialisation de la liste de couche en tant que liste vide
        self.coucheInitiale=CoucheInitiale(self.listeDonnee, nbCouche) # Initialisation de la couche initiale avec notre liste d'entrée
        
        # Création de notre ensemble de couche 
        for i in range(0,nbCouche-1):
            if(i==0):
                self.listeCouche.append(Couche(self.coucheInitiale, nbCouche-i-1))
            else:
                self.listeCouche.append(Couche(self.listeCouche[i-1], nbCouche-i))
        # Dans le cas où il n'y a que deux couches on lie la couche initiale et la couche finale
        if(nbCouche<2):
            self.coucheFinale=CoucheFinale(self.coucheInitiale)
        else:
            self.coucheFinale=CoucheFinale(self.listeCouche[nbCouche-2])

    # Méthode qui permet de modifier la liste de données
    def modifierListeDeDonnee(self, listeDonnee:list):
        self.listeDonnee = listeDonnee.copy()
        self.coucheInitiale.modifierListeValeur(self.listeDonnee) # Modification de la liste d'entrée dans la couche initiale

    # Fonction pour modifier le taux d'apprentissage
    def modifierTauxApp(self, tauxApp:float):
        self.tauxApprentissage = tauxApp

    # Fonction pour modifier la valeur attendue
    def modifierValAtt(self, valAtt:float):
        self.valAttendue = valAtt

    # Fonction pour modifier les paramètres de la Sigmoide
    def modifierParamSigmoide(self, paramSigmoide:float):
        self.paramSigmoide=paramSigmoide

    # Fonction pour modififer la marge d'erreur
    def modifierMargeErreur(self, margeErreur:float):
        self.margeErreur=margeErreur

    # Fonction pour retourner l'erreur
    def getErreur(self):
        return self.coucheFinale.neurone.getErreur()
    
    # Méthode pour afficher la liste d'entrée du réseau    
    def afficherListeDonnee(self) :
        itInt=0
        for x in self.listeDonnee :
            itInt=itInt+1
            print("Entrée "+str(itInt)+" : "+str(x))

    # Méthode pour afficher le réseau
    def afficherRéseau(self) :
        print("Affichage des entrées : ")
        self.afficherListeDonnee()
        print("Affichage de la couche initiale")
        self.coucheInitiale.afficherListe()
        it=0
        # Appel de la méthode affichage pour toute les couches
        for cou in self.listeCouche:
            print("Affichage de la couche "+str(it))
            cou.afficherListe()
            it=it+1
        print("Affichage de la couche final")
        self.coucheFinale.afficherListe()

    # Méthode pour initier le calcul dans notre réseau
    def initierCalcul(self):
        self.coucheInitiale.initierCalcul(self.paramSigmoide)
        for x in self.listeCouche:
            x.initierCalcul(self.paramSigmoide)
        self.coucheFinale.initierCalcul(self.paramSigmoide)
        print("Résultat du calcul : "+str(self.coucheFinale.neurone.getValeur()))

    # Méthode pour initier la correction dans notre réseau
    def initierCorrection(self):
        self.coucheFinale.propagationErreur(self.valAttendue,self.paramSigmoide) # Propagation de l'erreur selon la valeur attendue
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur())+" Marge : "+str(self.margeErreur)+"\n")
        # Si la valeur résultante est en dehors des bornes d'acceptation de la valeur attendue alors on initie la correction
        if(self.coucheFinale.neurone.getValeur()>(self.valAttendue+self.margeErreur) or self.coucheFinale.neurone.getValeur()<(self.valAttendue-self.margeErreur)):
            print("Correction\n")
            self.coucheFinale.propagationErreurCorrection(self.tauxApprentissage)

    # Méthode pour initier la correction Batch dans notre réseau
    def initierCorrectionBatch(self,correct:bool): # Propagation de l'erreur selon la valeur attendue
        self.coucheFinale.propagationErreur(self.valAttendue,self.paramSigmoide)
        print("Attente : "+str(self.valAttendue)+" Résultat : "+str(self.coucheFinale.neurone.getValeur())+" Marge : "+str(self.margeErreur)+"\n")
        if(correct):
            print("Correction\n")
            self.coucheFinale.propagationErreurCorrection(self.tauxApprentissage)