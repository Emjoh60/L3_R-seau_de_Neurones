from math import exp

class Neurone:
    
    # Constructeur
    def __init__(self,liste:dict):
        self.listeEntree = liste.copy() # On affecte un tableau associatif dont l'index correspond à une entrée du neurone et la valeur correspond au poids

    # Méthode pour calcuer la sortie du neurone
    def calculSigmoide(self,paramSigmoide:float):
        somme=0
        # On fait la somme de toute les entrées multipliées par leur poids
        for i in self.listeEntree:
            somme=somme+(i.getValeur()*self.listeEntree[i])
        self.valeur = 1/(1+exp(-(somme*paramSigmoide)))
    
    # Méthode de retour d'une valeur
    def getValeur(self):
        return self.valeur
    
    # Méthode de rajout d'une valeur d'entrée
    def addEntree(self,val,poid:float):
        if type(val) == Neurone :
            self.listeEntree[val]=poid
        else:
            raise Exception("Erreur : Mauvais type")

    # Méthode de suppression d'une valeur d'entrée
    def removeEntree(self,index):
        if type(index)==Neurone :
            del self.listeEntree[index]
        else:
            raise Exception("Erreur : Mauvais type")
        
    # Méthode pour afficher les entrées du neurone
    def afficherListe(self) :
        itNeu=0
        for x in self.listeEntree:
            itNeu=itNeu+1
            print("         Neurone Prec : "+str(itNeu)+" - Poids "+str(self.listeEntree[x]))
    
    # Méthode pour calculer l'erreur selon une valeur attendue (sutout utilisé pour le neurone de sortie)
    def calculErreurAttendue(self,valAttendue:float):
        self.erreur=valAttendue-self.valeur
    
    # Méthode pour calculer l'erreur du neurone    
    def calculErreur(self,listeSuivante:list,paramSigmoide:float): # On passe au neurone une liste contenant tous ses successeurs puisque un neurone n'a pas accès directement 
        somErrPoids=0
        # On fait la somme des erreurs de sortie multipliées par les poids
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        self.erreur=paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids

    # Méthode pour calculer l'erreur du neurone Batch
    def calculErreurBatch(self,listeSuivante:list,paramSigmoide:float): # On passe au neurone une liste contenant tous ses successeurs puisque un neurone n'a pas accès directement
        somErrPoids=0
        # On fait la somme des erreurs de sortie multipliées par les poids
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        # Si l'erreur n'a pas été déjà calculée on lui affecte sa valeur afin de ne pas avoir de problème à l'execution
        if not(self.erreur in locals()):
            self.erreur=(self.erreur+paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids)
        self.erreur=(self.erreur+paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids)/2 # On fait la moyenne des erreurs

    # Méthode pour récupérer l'erreur 
    def getErreur(self):
        return self.erreur

    # Méthode pour corriger tous les poids d'entrée de ce neurone selon le coeff d'apprentissage
    def correctionPoids(self,coeffApp):
        for neurPrec in self.listeEntree:
            self.listeEntree[neurPrec]=self.listeEntree[neurPrec]+coeffApp*neurPrec.getValeur()*self.getErreur()