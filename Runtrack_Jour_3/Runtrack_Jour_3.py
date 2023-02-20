# -*- coding: utf-8 -*-
"""
Runtrack_Jour_3

Date : 19/02/2023
Auteur : Selima Sassi
"""

import re
import numpy as np


#%% Job 0

print ('Job 0')

# On demande a l'utilisateur ce qu'il veut ecrire dans le fichier et on stocke sa reponse
content = input ("Merci de renseigner une chaine de caracteres : ")


# On ouvre le fichier et on remplace son contenu si le fichier existe, sinon on le cree 
f = open("output.txt" , "w") # On ouvre le fichier en mode "ecriture"
f.write(content) # On ecrit la chaine entree par l'utilisateur
f.close() # On ferme le fichier

print ("La chaine de caracteres a ete inseree dans le fichier output.txt")

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 0.1

print ('Job 0.1')
print ()

f = open("output.txt" , "r") # On ouvre le fichier en mode "lecture"
content = f.read() # On lit le contenu du fichier et on le stocke
f.close() # On ferme le fichier

# Affichage du contenu
if len(content) == 0 : # Cas ou le fichier est vide
    print ("Le fichier est vide")
else : # Cas ou le fichier contient des informations 
    print ("Contenu du fichier output.txt : ")
    print ()
    print (content)

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 01 - domains.xml

print ('Job 01 - domains.xml')
print ()

f = open("domains.xml" , "r") # On ouvre le fichier en mode "lecture"
content_domains = f.read() # On lit le contenu du fichier et on le stocke
f.close() # On ferme le fichier

resultat = re.findall( r"\.[a-z]{2,4}[/|<|\n]" , content_domains )
print ("Nombre de domaines trouves : {} ".format(len(resultat)))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 01 - data.txt

print ('Job 01 - data.txt')
print ()

f_data = open("data.txt" , "r")
content_data = f_data.read()
f_data.close()

resultat_mots = re.findall( r"\w+" , content_data )
resultat_mots = list(filter(None , resultat_mots)) # Supprime les chaines vides

print ("Nombre de mots trouves : {} ".format(len(resultat_mots)))
print ("Les 10 premiers mots sont : ")
for i in range (10) :
    print ("   - "+resultat_mots[i])

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 02

print ('Job 02')

nb_lettres = input ("Veuillez renseigner un nombre entier : ")
print ()

resultat_nb_mots_1taille = []
for i in range (len(resultat_mots)) :
    if (len(resultat_mots[i]) == int(nb_lettres)) :
        resultat_nb_mots_1taille.append(resultat_mots[i])
        
print ("Nombre de mots de "+str(nb_lettres)+" lettres trouves : {} ".format(len(resultat_nb_mots_1taille)))
print ("Les 10 premiers mots sont : ")
for i in range (10) :
    print ("   - "+resultat_nb_mots_1taille[i])

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% ---Job 03

print ('Job 03')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% --Job 05

print ('Job 05')
print ()

resultat_nb_mots_ttes_tailles = {}

res = resultat_mots.copy()

for j in range (1, 31) :
    compte = 0
    for i in range (len(res)) :
        if (len(res[i]) == j) :
            compte += 1
        
    resultat_nb_mots_ttes_tailles.update({j: compte})

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% --Job 08

print ('Job 08')
print ()

resultat_lettres_debut = {}

res = resultat_mots.copy()

Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for j in range (len(Alphabet)) :
    compte = 0
    for i in range (len(res)) :
        if ((res[i])[0].lower() == Alphabet[j]) :
            compte += 1
            res.remove(res[i])
    resultat_lettres_debut.update({j: compte})

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% --Job 13

print ('Job 13')
print ()

liste_nb_occur_lettre_suiv = []

for lettre in Alphabet:
    liste = np.zeros(26)
    for mot in resultat_mots :
        for i in range(len(mot)) :
            if mot[i] == lettre :
                
                for j in range(len(Alphabet)) :
                    if (i+1 < len(mot)) and (mot[i+1] == Alphabet[j]) :
                        liste[j] += 1
    
    liste_nb_occur_lettre_suiv.append(liste)

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% ---Job 21

print ('Job 21')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% ---Job 34

print ('Job 34')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% ---Job 55

print ('Job 55')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()

#%%
















