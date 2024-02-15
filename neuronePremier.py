from math import exp
from neurone import Neurone

class NeuronePremier(Neurone):
    def __init__(self,liste):
        self.listeEntree  = []
        
    def calculSigmoide(self,paramSigmoide:float):
        somme=0
        for x in range(len(self.listeEntree)):
            somme=somme+(self.listeEntree[x][0]*self.listeEntree[x][1])
        self.valeur = 1/(1+exp(-(somme*paramSigmoide)))
    
    def getValeur(self):
        return self.valeur
    
    def addEntree(self,val:list,poid:float):
        self.listeEntree[len(self.listeEntree)+1][0]=val[0]
        self.listeEntree[len(self.listeEntree)+1][1]=poid

    def removeEntree(self,index):
        del self.listeEntree[index]

    def afficherListe(self) :
        itInt=0
        for x in range(len(self.listeEntree)):
            itInt=itInt+1
            print("Entrée "+str(x)+" Valeur : "+str(self.listeEntree[x][0])+" - Poids "+str(self.listeEntree[x][1]))
    
    def calculErreurAttendue(self,valAttendue:float):
        self.erreur=valAttendue-self.valeur
        
    def calculErreur(self,listeSuivante:list,paramSigmoide:float):
        somErrPoids=0
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        self.erreur=paramSigmoide*self.valeur*(1-self.valeur)*somErrPoids

    def getErreur(self):
        return self.erreur

    def correctionPoids(self,coeffApp):
        for x in range(len(self.listeEntree)):
            self.listeEntree[x][1]=self.listeEntree[x][1]+coeffApp*self.listeEntree[x][0]*self.getErreur()
            self.listeEntree[x][1]=round(self.listeEntree[x][1], 2)