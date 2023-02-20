# -*- coding: utf-8 -*-
"""
Runtrack_Jour_2

Date : 16/02/2023
Auteur : Selima Sassi
"""

"""
15/02 - s
- Job 2 (Classe Client / Classe Bibliotheque)
- modif dans la fonction listerOeuvre
- pb fonction acheterLivre

16/02
- Modif Auteur.listerOeuvre => remplacement return par print (car fonction d'affichage)
- Modif acheterLivre / inventaire / louer / rendreLivre => on doit rentrer le NOM du livre et non un OBJET livre
    (il a fallu faire les boucles => creer methode dans livre pour faciliter ?)
"""

#%% Job 0 - Classe Personne

class Personne :
    
    
    def __init__ (self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    
        
    def SePresenter(self):
        print ('Nom    : ' + self.nom + '\n' + 'Prenom : ' + self.prenom )
        
        
    def get_nom(self):
        return (self.nom)
        
    def get_prenom(self):
        return (self.prenom)
        
    
    def set_nom(self,nouveau_nom):
        self.nom = nouveau_nom
           
    def set_prenom(self,nouveau_prenom):
        self.prenom = nouveau_prenom
        

#%% Job 1 - Classe Auteur / Classe Livre

class Auteur (Personne) :
    
    def __init__ (self , nom , prenom , *oeuvres):
        self.oeuvres = oeuvres
        Personne.__init__(self, nom , prenom)
    
    # Autre solution :
    # def __init__ (self , nom , prenom):
    #     self.oeuvres = []
    #     Personne.__init__(self, nom , prenom)
    
    def listerOeuvre (self) :
        if len(self.oeuvres) > 0 :
            print ("La liste des oeuvres de" , self.prenom , self.nom , "est : ")
            for livre in self.oeuvres:
                print("   - \"" , livre.titre , "\" ")
        else : 
            print (self.prenom , self.nom , "n'a pas d'oeuvres enregistrees")
        print ()
    
    def ecrireUnLivre (self , titre) :
        nouvelle_oeuvre = Livre ( titre , self )
        self.oeuvres += (nouvelle_oeuvre , )

# -----------------------------------------------------------------------------

class Livre :
    
    def __init__ (self,titre,auteur):
        self.titre = titre
        self.auteur = auteur
    
    def __str__ (self) :
        return ( "Le titre du livre est \" %s \" " % (self.titre) )
        

#%% Job 2 - Classe Client / Classe Bibliotheque

class Client (Personne) :
    
    def __init__ (self , nom , prenom , *collection):
        self.collection = collection
        Personne.__init__(self, nom , prenom)

    def inventaire (self) : 
        print ()
        
        if len(self.collection) > 0 :
            print (self.prenom , self.nom , "a emprunte les livres : ")
            for livre in self.collection:
                print("   - \" " , livre , " \" ")
        
        else : 
            print (self.prenom , self.nom , "n'a emprunte aucun livre")
        
        print ()

# -----------------------------------------------------------------------------

class Bibliotheque :
    
    # def __init__ (self , nom: str , catalogue: dict) -> Bibliotheque :
    def __init__ (self , nom , catalogue ) :   
        # assert (type(catalogue) == dict , "la variable catalogue doit etre du type dictionnaire")
        self.nom = nom
        self.catalogue = catalogue
        
    def acheterLivre (self , auteur , nom_livre , quantite) :
        # on verifie que le nom du livre est dans le catalogue de l'auteur 
        for i in range (len (auteur.oeuvres)) :
            if nom_livre == auteur.oeuvres[i].titre : 
                
                qte = 0
                j = 0
                livre = None
                
                # on verifie si le nom du livre est dans la collection de la bibliotheque
                while j < (len((self.catalogue).keys())) :
                    if nom_livre == list((self.catalogue).keys())[j].titre :
                        livre = list((self.catalogue).keys())[j]
                        qte += (self.catalogue)[list((self.catalogue).keys())[j]]
                        j = (len((self.catalogue).keys())) 
                    j += 1
                    
                if livre == None : 
                    livre = Livre(nom_livre,auteur)
                (self.catalogue).update({livre : quantite + qte})

    def inventaire (self) : 
        print ()
        print ('Nom de la bibliotheque : ' , self.nom)
        print ()
        print ('Vous trouverez : ')
        for livre, qte in (self.catalogue).items():
            print('   - ' , qte , " exemplaires du livre \" " , livre.titre , " \" ")
        print ()

    def louer (self , client , nom_livre) :
        
        j = 0
        livre = None
        
        # on verifie si le nom du livre est dans la collection de la bibliotheque
        while j < (len((self.catalogue).keys())) :
            if nom_livre == list((self.catalogue).keys())[j].titre :
                livre = list((self.catalogue).keys())[j]
                j = (len((self.catalogue).keys())) 
            j += 1
        
        if ((livre != None) and ( (self.catalogue)[livre] > 0 )) : 
            client.collection += (nom_livre , )
            (self.catalogue)[livre] -= 1

    def rendreLivres (self , client):
        for nom_livre in client.collection :
            j = 0
            livre = None
            
            # on verifie si le nom du livre est dans la collection de la bibliotheque
            while j < (len((self.catalogue).keys())) :
                if nom_livre == list((self.catalogue).keys())[j].titre :
                    livre = list((self.catalogue).keys())[j]
                    j = (len((self.catalogue).keys())) 
                j += 1
                
            if livre != None :
                qte = (self.catalogue)[livre]
            else :
                qte = 0
                
            (self.catalogue).update({livre : (qte + 1)})
        
        client.collection = ()
        

#%% Tests

print ("On cree des auteurs : ")
aut1 = Auteur('nom1' , 'prenom1')
aut2 = Auteur('nom2' , 'prenom2')
aut3 = Auteur('nom3' , 'prenom3')

print ("On affiche la liste de leurs oeuvres : ")
aut1.listerOeuvre()
aut2.listerOeuvre()
aut3.listerOeuvre()

print ()
print ("On ajoute a ces listes des livres (de classe Livre) : ")

aut1.ecrireUnLivre('A1_titre1')
aut1.ecrireUnLivre('A1_titre2')
aut1.ecrireUnLivre('A1_titre3')
aut1.ecrireUnLivre('A1_titre4')
aut1.ecrireUnLivre('A1_titre5')
aut1.listerOeuvre()
print ()

aut2.ecrireUnLivre('A2_ttr1')
aut2.ecrireUnLivre('A2_ttr2')
aut2.ecrireUnLivre('A2_ttr3')
aut2.ecrireUnLivre('A2_ttr4')
aut2.listerOeuvre()
print ()
# print (aut2.oeuvres[1].titre)

aut3.ecrireUnLivre('A3_t1')
aut3.ecrireUnLivre('A3_t2')
aut3.ecrireUnLivre('A3_t3')
aut3.ecrireUnLivre('A3_t4')
aut3.ecrireUnLivre('A3_t5')
aut3.ecrireUnLivre('A3_t6')
aut3.listerOeuvre()
print ()

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

clt1 = Client('nom1','prenom1')
clt2 = Client('nom2','prenom2')
clt3 = Client('nom3','prenom3')
clt4 = Client('nom4','prenom4')

clt1.inventaire()
clt2.inventaire()
clt3.inventaire()
clt4.inventaire()

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

A1_livre1 = aut1.oeuvres[0]
A1_livre2 = aut1.oeuvres[1]
A1_livre3 = aut1.oeuvres[2]

A2_livre1 = aut2.oeuvres[0]
A2_livre2 = aut2.oeuvres[1]
A2_livre3 = aut2.oeuvres[2]

A3_livre1 = aut3.oeuvres[0]
A3_livre2 = aut3.oeuvres[1]
A3_livre3 = aut3.oeuvres[2]

bib1 = Bibliotheque('bibli_1' , {A1_livre1 : 10 , A2_livre1 : 20 , A3_livre1 : 30})
bib2 = Bibliotheque('bibli_2' , {A1_livre2 : 40 , A2_livre2 : 50 , A3_livre2 : 60})
bib3 = Bibliotheque('bibli_3' , {A1_livre3 : 70 , A2_livre3 : 80 , A3_livre3 : 90})
bib4 = Bibliotheque('bibli_4' , {A1_livre1 : 110 , A2_livre2 : 120 , A3_livre3 : 130})

bib1.inventaire()
bib2.inventaire()
bib3.inventaire()
bib4.inventaire()
# bib4.catalogue

bib1.acheterLivre(aut1, "A1_titre1", 20) # actualise la quantite de livre A1_livre1
bib1.inventaire()

bib1.acheterLivre(aut1, "A2_ttr2", 20) # ne doit rien ajouter car pas bon auteur
bib1.inventaire()

bib1.acheterLivre(aut2, "A2_ttr2", 20) # ajoute le livre A2_livre2
bib1.inventaire()
# bib1.catalogue

# ----------------------------------------------------------------------------

bib1.louer(clt1 , "A1_titre1") # Ajoute A1_titre1 a la collection de clt1
bib1.louer(clt1 , "A1_titre2") # livre non present dans la bibliotheque
bib1.louer(clt1 , "A2_ttr2") # Ajoute A2_titre2 a la collection de clt1

clt1.inventaire()
bib1.inventaire()

# ----------------------------------------------------------------------------

bib1.rendreLivres(clt1)

clt1.inventaire()
bib1.inventaire()


#%%





