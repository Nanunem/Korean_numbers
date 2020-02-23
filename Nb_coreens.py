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
                break
    with open("Dico_cor_pur","r") as fic_cor_pur :
        for line in fic_cor_pur:
            line=line.strip()
            line=line.split(":")
            if len(line)>1 :
                dico_cor_pur[line[0]]=line[1]
            else :
                break
    return dico_sino, dico_cor_pur

def construction_rep(number,type):
    #answer2 ne concerne que les nombres > 100 et le type "co" où deux écritures sont possibles
    if number < 11 :
        if type=="co" :
            answer1=ref_cor_pur[str(number)]
        elif type=="si" :
            answer1=ref_sino[str(number)]
    elif number > 10 and number < 101 and number % 10 == 0 :
        if type=="co" :
            answer1=ref_cor_pur[str(number)]
        elif type=="si":
            first_part=number//10
            answer1 = ref_sino[str(first_part)] + ref_sino["10"]
    elif number < 101 and number % 10 != 0 :
        if type=="co" :
            first_part=number//10*10
            second_part=number%10
            answer1=ref_cor_pur[str(first_part)]+ref_cor_pur[str(second_part)]
        elif type == "si":
            first_part = number // 10
            second_part = number % 10
            answer1 = ref_sino[str(first_part)]+ ref_sino["10"] + ref_sino[str(second_part)]
    elif number > 100 and number <1001:
        first_part = number // 100
        second_part = number % 100
        third_part = second_part // 10
        forth_part = second_part % 10
        if type=="si" :
            if forth_part==0 :
                if third_part==1 :
                    if first_part==1 :
                        answer1 = ref_sino["100"] + ref_sino["10"]
                    else :
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino["10"]
                else :
                    if first_part == 1:
                        answer1 = ref_sino["100"] + ref_sino[str(third_part)] + ref_sino["10"]
                    else:
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino[str(third_part)] + ref_sino["10"]
            else :
                if third_part==1 :
                    if first_part==1 :
                        answer1 = ref_sino["100"] + ref_sino["10"] + ref_sino[str(forth_part)]
                    else :
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino["10"] + ref_sino[str(forth_part)]
                else :
                    if first_part==1 :
                        answer1=ref_sino["100"] +ref_sino[str(third_part)]+ ref_sino["10"] + ref_sino[str(forth_part)]
                    else :
                        answer1=ref_sino[str(first_part)]+ ref_sino["100"] +ref_sino[str(third_part)]+ ref_sino["10"] + ref_sino[str(forth_part)]
        elif type == "co":
            print("Pour le système coréen et les nombres > 100, deux possibilités sont offertes :\n")
            print("- écrire le nombre dans le système sino\n")
            print("- s'approcher le plus possible du système coréen, donc en écrivant les milliers et les centaines dans le sytèmes sino et les dizaines et unités dans le système coréen\n")
            #première possibilité = strictement sino
            if forth_part==0 :
                if third_part==1 :
                    if first_part==1 :
                        answer1 = ref_sino["100"] + ref_sino["10"]
                    else :
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino["10"]
                else :
                    if first_part == 1:
                        answer1 = ref_sino["100"] + ref_sino[str(third_part)] + ref_sino["10"]
                    else:
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino[str(third_part)] + ref_sino["10"]
            else :
                if third_part==1 :
                    if first_part==1 :
                        answer1 = ref_sino["100"] + ref_sino["10"] + ref_sino[str(forth_part)]
                    else :
                        answer1 = ref_sino[str(first_part)] + ref_sino["100"] + ref_sino["10"] + ref_sino[str(forth_part)]
                else :
                    if first_part==1 :
                        answer1=ref_sino["100"] +ref_sino[str(third_part)]+ ref_sino["10"] + ref_sino[str(forth_part)]
                    else :
                        answer1=ref_sino[str(first_part)]+ ref_sino["100"] +ref_sino[str(third_part)]+ ref_sino["10"] + ref_sino[str(forth_part)]
            # deuxième possibilité = composite sino coréen
            if forth_part==0 :
                if third_part==1 :
                    if first_part==1 :
                        answer2 = ref_sino["100"] + ref_cor_pur["10"]
                    else :
                        answer2 = ref_sino[str(first_part)] + ref_sino["100"] + ref_cor_pur["10"]
                else :
                    if first_part==1 :
                        answer2 = ref_sino["100"] + ref_cor_pur[str(third_part*10)]
                    else :
                        answer2 = ref_sino[str(first_part)] + ref_sino["100"] + ref_cor_pur[str(third_part*10)]
            else :
                if third_part==1 :
                    if first_part==1 :
                        answer2 = ref_sino["100"] + ref_cor_pur["10"] + ref_cor_pur[str(forth_part)]
                    else :
                        answer2 = ref_sino[str(first_part)] + ref_sino["100"] + ref_cor_pur["10"] + ref_cor_pur[str(forth_part)]
                else :
                    if first_part==1 :
                        answer2=ref_sino["100"] +ref_cor_pur[str(third_part*10)]+ ref_cor_pur[str(forth_part)]
                    else :
                        answer2=ref_sino[str(first_part)]+ ref_sino["100"] +ref_cor_pur[str(third_part*10)]+ ref_cor_pur[str(forth_part)]
    return answer1, answer2

##########################################################################################

print("##########################################################################\n")
print("############# PROGRAMME DE REVISIONS DES NOMBRES EN COREEN ###############\n")
print("##########################################################################\n")

print("Programme valable jusqu'à 10000")

ref_sino, ref_cor_pur = dico_nb()  #prise en compte des noms des nombres sino-coréens et coréens
test=construction_rep(120,"co")
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