# -*- coding: utf-8 -*-
"""
Runtrack_Jour_1

Date : 15/02/2023
Auteur : Selima Sassi
"""


#%% Job 11

print ('Job 11')

prenom = input ('Veuillez entrer votre prenom : ')
print ()
print ('Hello ' , prenom , ' !')

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 13

print ('Job 13')

L = []
for i in range (5) : 
    nb = input ('Veuillez entrer un nombre : ')
    L.append(nb)

L.sort()

print ()
print ("La liste des nombres tries par ordre croissant est : ")
print (L)

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 17

print ('Job 17')
print ()

for i in range (1,101) :
    if ( (i%3 == 0) and (i%5 != 0) ):
        print (i , ': Fizz')
    elif ( (i%3 != 0) and (i%5 == 0) ):
        print (i , ': Buzz')
    elif ( (i%3 == 0) and (i%5 == 0) ):
        print (i , ': FizzBuzz')
    else : 
        print (i)
        
print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 19

print ('Job 19')

def draw_rectangle (width, height) :
    assert width > 0 , 'La longueur doit etre un nombre strictement positif'
    assert height > 0 , 'La largeur doit etre un nombre strictement positif'
    
    for i in range (height) :
        L = '|'
        for k in range (width-1) :
            if ( (i == 0) or (i == (height-1)) ) : 
                L += '-'
            else : 
                L += ' '
        L += '|'
        print (L)

width = input ('Veuillez entrer la largeur (width) du rectangle : ')
height = input ('Veuillez entrer la hauteur (height) du rectangle : ')

draw_rectangle(int(width), int(height))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 23

print ('Job 23')

def draw_triangle (height) :
    assert height > 0 , 'La hauteur doit etre un nombre strictement positif'

    esp_avant = height - 1
    esp_dedans = 0

    for i in range (height) :
        L = ''
        
        for k1 in range (esp_avant) : 
            L += ' '
            
        L += '/'
        
        if esp_dedans == height-1 :
            for k2 in range (esp_dedans*2) : 
                L += '_'
        else :
            for k2 in range (esp_dedans*2) : 
                L += ' '
        
        L += '\\'
        
        esp_avant -= 1
        esp_dedans +=1

        print (L)

height = input ('Veuillez entrer la hauteur (height) du triangle : ')

draw_triangle(int(height))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 29

print ('Job 29')
print ()

def arrondi_LS (nb):
    ent = ( nb // 5 )
    multiple_5 = (ent + 1) * 5
    
    if (multiple_5 - nb) < 3 :
        return (multiple_5)
    else : 
        return (nb)

def arrondi_notes_LS (Liste):
    nb_notes = len(Liste)
    
    Liste_arrondi = []
    for i in range (nb_notes) :
        Liste_arrondi.append(arrondi_LS(Liste[i]))
    
    return (Liste_arrondi)

notes = [80,81,82,83,84,85,86,87,88,89,90]
arr = arrondi_notes_LS(notes)
print ('Pour les notes : ' )
print ( notes )
print ("On obtient l'arrondi : ")
print ( arr )

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 31

print ('Job 31')

from unidecode import unidecode # permet d'enlever les accents

Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mot = input ('Veuillez entrer un seul mot, sans espace ni aucun autre caractère que les 26 lettres de l’alphabet : ')

mot_modif = unidecode(mot) 
mot_modif = mot_modif.replace (' ' , '')

mot_final = ''
for i in range (len(mot_modif)) : 
    if mot_modif[i] in Alphabet :
        mot_final += mot_modif[i]

Liste_lettres = list(mot)

def plus_loin_proche (mot) :
    n = len(mot)
    i = n-1
    
    mot_plus_loin_proche = ''
    
    while mot[i-1] >= mot[i] : # on s'arrete quand i-1 < i 
        i -= 1
    
    mot_plus_loin_proche = mot[:i-1]
    
    reste_mot = mot[i-1:]
    liste_ord = list(reste_mot)
    liste_ord.sort()
    
    k = liste_ord.index(mot[i-1])
    mot_plus_loin_proche += liste_ord[k+1]
    liste_ord.remove(liste_ord[k+1])
    reste_mot_ord = ''.join(liste_ord)
    
    mot_plus_loin_proche += reste_mot_ord
    
    return (mot_plus_loin_proche)

print (mot_final)
print (plus_loin_proche(mot_final))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%%






