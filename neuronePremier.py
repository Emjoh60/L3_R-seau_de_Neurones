from math import exp
from neurone import Neurone

class NeuronePremier(Neurone):
    
    # Constructeur
    def __init__(self,liste):
        self.listeEntree  = [] # On initialise la liste d'entrée à vide parce qu'elle sera constitué dans la classe couche intinale
    
    # Méthode pour calcuer la sortie du neurone    
    def calculSigmoide(self,paramSigmoide:float):
        somme=0
        for x in range(len(self.listeEntree)):
            somme=somme+(self.listeEntree[x][0]*self.listeEntree[x][1])
        self.valeur = 1/(1+exp(-(somme*paramSigmoide)))
    
    # Méthode de retour d'une valeur
    def getValeur(self):
        return self.valeur
    
    # Méthode de rajout d'une valeur d'entrée 
    def addEntree(self,val:list,poid:float):
        self.listeEntree[len(self.listeEntree)+1][0]=val[0] # Affectation dans la case de l'entrée n la valeur passée en paramètre
        self.listeEntree[len(self.listeEntree)+1][1]=poid # Affectation dans la case de l'entrée n le poid passée en paramètre
    
    # Méthode de suppression d'une valeur d'entrée
    def removeEntree(self,index):
        del self.listeEntree[index]

    # Méthode pour afficher les entrées du neurone
    def afficherListe(self) :
        itInt=0
        for x in range(len(self.listeEntree)):
            itInt=itInt+1
            print("         Entrée "+str(x)+" Valeur : "+str(self.listeEntree[x][0])+" - Poids "+str(self.listeEntree[x][1]))
    
    # Méthode pour calculer l'erreur selon une valeur attendue (sutout utilisé pour le neurone de sortie)
    def calculErreurAttendue(self,valAttendue:float):
        self.erreur=valAttendue-self.valeur
    
    # Méthode pour calculer l'erreur du neurone    
    def calculErreur(self,listeSuivante:list,paramSigmoide:float):
        somErrPoids=0
        # On fait la somme des erreurs de sortie multipliées par les poids
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        self.erreur=paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids

    # Méthode pour calculer l'erreur du neurone Batch
    def calculErreurBatch(self,listeSuivante:list,paramSigmoide:float):
        somErrPoids=0
        # On fait la somme des erreurs de sortie multipliées par les poids
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        # Si l'erreur n'a pas été déjà calculée on lui affecte sa valeur afin de ne pas avoir de problème à l'execution
        if not(self.erreur in locals()):
            self.erreur=(self.erreur+paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids)
        self.erreur=(self.erreur+paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids)/2

    # Méthode pour récupérer l'erreur
    def getErreur(self):
        return self.erreur
    
    # Méthode pour corriger tous les poids d'entrée de ce neurone selon le coeff d'apprentissage
    def correctionPoids(self,coeffApp):
        for x in range(len(self.listeEntree)):
            self.listeEntree[x][1]=self.listeEntree[x][1]+coeffApp*self.listeEntree[x][0]*self.getErreur()
            self.listeEntree[x][1]=self.listeEntree[x][1], 2