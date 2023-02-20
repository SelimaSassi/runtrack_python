# -*- coding: utf-8 -*-
"""
Runtrack_Jour_4

Date : 17/02/2023
Auteur : Selima Sassi
"""

import re
import numpy as np


#%% Job 0

print ('Job 0')
print ()

def factorielle (n) :
    
    assert (n>=0 and type(n)==int) , "Vous devez entrer un entier positif"
    
    if n==0 :
        return (1)
    else :
        return (n*factorielle(n-1))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 0.1

print ('Job 0.1')
print ()

n = input ("Veuillez entrer un nombre entier : ") 

def xn (x , n) :
    
    assert (n>=0) , "Cette fonction est a utiliser avec des nombres positifs"
    
    if n == 0 :
        return (1)
    
    elif n > 0 :
        return (x*xn(x,n-1))

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 03

print ('Job 03')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 08

print ('Job 08')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()


#%% Job 15

print ('Job 15')
print ()

#

print ()
print ('-----------------------------------------------------------------------')
print ()
































