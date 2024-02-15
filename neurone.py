from math import exp

class Neurone:
    def __init__(self,liste:dict):
        self.listeEntree = liste.copy()

    def calculSigmoide(self,paramSigmoide:float):
        somme=0
        for i in self.listeEntree:
            somme=somme+(i.getValeur()*self.listeEntree[i])
        self.valeur = 1/(1+exp(-(somme*paramSigmoide)))
    
    def getValeur(self):
        return self.valeur
    
    def addEntree(self,val,poid:float):
        if type(val) == Neurone :
            self.listeEntree[val]=poid
        else:
            raise Exception("Erreur : Mauvais type")

    def removeEntree(self,index):
        if type(index)==Neurone :
            del self.listeEntree[index]
        else:
            raise Exception("Erreur : Mauvais type")
        
    def afficherListe(self) :
        itNeu=0
        for x in self.listeEntree:
            itNeu=itNeu+1
            print("Neurone Prec : "+str(itNeu)+" - Poids "+str(self.listeEntree[x]))
    
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
        for neurPrec in self.listeEntree:
            self.listeEntree[neurPrec]=self.listeEntree[neurPrec]+coeffApp*neurPrec.getValeur()*self.getErreur()
            self.listeEntree[neurPrec]=round(self.listeEntree[neurPrec], 2)