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

def reponse(nombre) :
    dico_sino = {0:"영",
                    1:"일",
                    2:"이",
                    3:"삼",
                    4:"사",
                    5:"오",
                    6:"육",
                    7:"칠",
                    8:"발",
                    9:"구",
                    10:"십",
                    100:"백",
                    1000:"천",
                    10000:"만",
                    100000000:"억"}
    dico_cor_pur = {1:"하나",
                    2:"둘",
                    3:"셋",
                    4:"넷",
                    5:"다섯",
                    6:"여섯",
                    7:"일곱",
                    8:"여덟",
                    9:"아홉",
                    10:"열",
                    20:"스물",
                    30:"서른",
                    40:"마흔",
                    50:"쉰",
                    60:"예순",
                    70:"일흔",
                    80:"여든",
                    90:"아흔"}
    return rep

##########################################################################################

print("##########################################################################\n")
print("############# PROGRAMME DE REVISIONS DES NOMBRES EN COREEN ###############\n")
print("##########################################################################\n")
nombre_a_reviser=input("Combien de nombre à réviser aujourd'hui?  ")


if float(nombre_a_reviser)==0 :
    print("Fin du programme de révisions")
    sys.exit()
else :
    while nombre_a_reviser.isdigit()==False :
        print("Erreur, choisir un nombre entier et positif")
        nombre_a_reviser = input("Combien de nombre à réviser aujourd'hui?  ")

niveau=input("Niveau simple (\"s\") ou compliqué (\"c\")?  ")
while niveau != "C" and niveau != "c" and niveau != "s" and niveau != "S":
    print("Erreur dans le choix du niveau, s ou c seulement")
    niveau=input("Niveau simple (\"s\") ou compliqué (\"c\")?  ")

sino=input("Réviser nombres coréens (\"co\") ou sino-coréens (\"si\") ?")
while sino != "CO" and sino != "Co" and sino != "co" and sino != "SI" and sino != "Si" and sino != "si":
    print("Erreur dans le choix du type de nombre, co ou si seulement")
    sino = input("Réviser nombres coréens (\"co\") ou sino-coréens (\"si\") ?")

if niveau == "s" :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 100)
        print(nombre)
else :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 1000000)
        print(nombre)


#exercice = input ("La date du jour en coréen ?")
print("Fin du programme de révisions")