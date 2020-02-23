#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from operator import itemgetter
import string
import os
import glob
import sys
from datetime import date
import re
import textwrap
import itertools
import shutil
from pathlib import Path
import random as r

def dico_nb() :
    dico_sino = {}
    dico_cor_pur ={}
    with open("Dico_sino","r") as fic_sino :
        for line in fic_sino:
            line=line.strip()
            line=line.split(":")
            if len(line)>1 :
                dico_sino[line[0]]=line[1]
            else :
                print("Erreur dans le dico \""+fic_sino.name+"\"")
                break
    with open("Dico_cor_pur","r") as fic_cor_pur :
        for line in fic_cor_pur:
            line=line.strip()
            line=line.split(":")
            if len(line)>1 :
                dico_cor_pur[line[0]]=line[1]
            else :
                print("Erreur dans le dico \""+fic_cor_pur.name+"\"")
                break
    return dico_sino, dico_cor_pur

##########################################################################################

print("##########################################################################\n")
print("############# PROGRAMME DE REVISIONS DES NOMBRES EN COREEN ###############\n")
print("##########################################################################\n")

ref_sino, ref_cor_pur = dico_nb()  #prise en compte des noms des nombres sino-coréens et coréens

nombre_a_reviser=input("Combien de nombre à réviser aujourd'hui?  ")

if float(nombre_a_reviser)==0 :
    print("Fin du programme de révisions")
    sys.exit()
else :
    while nombre_a_reviser.isdigit()==False :
        print("Erreur, choisir un nombre entier et positif")
        nombre_a_reviser = input("Combien de nombre à réviser aujourd'hui?  ")

niveau=input("Niveau simple (\"s\") ou compliqué (\"c\")?  ") #compliqué étant la révision des nombres > 100
while niveau != "C" and niveau != "c" and niveau != "s" and niveau != "S":
    print("Erreur dans le choix du niveau, s ou c seulement")
    niveau=input("Niveau simple (\"s\") ou compliqué (\"c\")?  ")

sino=input("Réviser nombres coréens (\"co\") ou sino-coréens (\"si\") ?") #choix de réviser les nombres sino-coréens ou coréens
while sino != "CO" and sino != "Co" and sino != "co" and sino != "SI" and sino != "Si" and sino != "si":
    print("Erreur dans le choix du type de nombre, co ou si seulement")
    sino = input("Réviser nombres coréens (\"co\") ou sino-coréens (\"si\") ?")

if niveau == "s" :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 100)
else :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 1000000)

#exercice = input ("La date du jour en coréen ?")
print("Fin du programme de révisions")