from math import exp
class Neurone:
    def __init__(self,liste:dict):
        self.listeEntree = liste.copy()

    def calculSigmoide(self):
        somme=0
        for i in self.listeEntree:
            if type(i) == float:
                somme=somme+(i*self.listeEntree[i])
            elif type(i) == Neurone:
                somme=somme+(i.getValeur()*self.listeEntree[i])
        self.valeur = 1/(1+exp(-somme))
    
    def getValeur(self):
        return self.valeur
    
    def addEntree(self,val,poid:float):
        if type(val) == float or type(val) == Neurone :
            self.listeEntree[val]=poid
        else:
            raise Exception("Erreur : Mauvais type")

    def removeEntree(self,index):
        if type(index)==float or type(index)==Neurone :
            del self.listeEntree[index]
        else:
            raise Exception("Erreur : Mauvais type")
        
    def afficherListe(self) :
        itInt=0
        itNeu=0
        for x in self.listeEntree:
            if type(x) == float:
                itInt=itInt+1
                print("Entrée "+str(x)+" - Poids "+str(self.listeEntree[x]))
            elif type(x) == Neurone:
                itNeu=itNeu+1
                print("Neurone Prec : "+str(itNeu)+" - Poids "+str(self.listeEntree[x]))
    
    def calculErreurAttendue(self,valAttendue:float):
        self.erreur=valAttendue-self.valeur
        
    def calculErreur(self,listeSuivante:list):
        somErrPoids=0
        for neuSuivant in listeSuivante:
            e=neuSuivant.getErreur()
            w=neuSuivant.listeEntree[self]
            somErrPoids=somErrPoids+(e*w)
        self.erreur=self.valeur*(1-self.valeur)*somErrPoids

    def getErreur(self):
        return self.erreur

    def correctionPoids(self,coeffApp):
        for neurPrec in self.listeEntree:
            if type(neurPrec)==Neurone:
                self.listeEntree[neurPrec]=self.listeEntree[neurPrec]+coeffApp*neurPrec.getValeur()*self.getErreur()
            elif type(neurPrec)==float:
                self.listeEntree[neurPrec]=self.listeEntree[neurPrec]+coeffApp*neurPrec*self.getErreur()
