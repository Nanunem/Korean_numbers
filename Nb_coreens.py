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

def unites(number, type):
    if type == "co":
        ans1 = ref_cor_pur[str(number)]
    elif type == "si":
        ans1 = ref_sino[str(number)]
    return ans1

def dizaines(number, type) :
    if number > 10 and number < 101 and number % 10 == 0 :
        if type=="co" :
            ans1=ref_cor_pur[str(number)]
        elif type=="si":
            first_part=number//10
            ans1 = ref_sino[str(first_part)] + ref_sino["10"]
    elif number < 101 and number % 10 != 0 :
        if type=="co" :
            first_part=number//10*10
            second_part=number%10
            ans1=ref_cor_pur[str(first_part)]+ref_cor_pur[str(second_part)]
        elif type == "si":
            first_part = number // 10
            second_part = number % 10
            ans1 = ref_sino[str(first_part)]+ ref_sino["10"] + ref_sino[str(second_part)]
    return ans1

def centaines(number, type) :
    first_part = number // 100
    second_part = number % 100
    if type == "si":
        if second_part < 10 and second_part > 0 :
            diz = unites(second_part, "si")
        elif second_part==0 :
            diz=""
        else :
            diz=dizaines(second_part,"si")
        if first_part == 1:
            ans1 = ref_sino["100"] + diz
        else:
            ans1 = ref_sino[str(first_part)] + ref_sino["100"] + diz
        ans2=0
    elif type == "co":
        # première possibilité = sino uniquement
        if second_part < 10 and second_part > 0 :
            diz = unites(second_part, "si")
        elif second_part==0 :
            diz=""
        else :
            diz=dizaines(second_part,"si")
        if first_part == 1:
            ans1 = ref_sino["100"] + diz
        else:
            ans1 = ref_sino[str(first_part)] + ref_sino["100"] + diz
        # deuxième possibilité = composite sino coréen
        if second_part < 10 and second_part > 0 :
            diz = unites(second_part, "co")
        elif second_part==0 :
            diz=""
        else :
            diz=dizaines(second_part,"co")
        if first_part == 1:
            ans2 = ref_sino["100"] + diz
        else:
            ans2 = ref_sino[str(first_part)] + ref_sino["100"] + diz
    return ans1, ans2

def milliers(number, type) :
    first_part = number // 1000
    second_part = number % 1000
    if type == "si":
        cen1,cen2=centaines(second_part,"si")
        if first_part == 1:
            answer1 = ref_sino["1000"] + cen1
        else:
            answer1 = ref_sino[str(first_part)] + ref_sino["1000"] + cen1
        answer2 = 0
    elif type == "co":
        # première possibilité = sino uniquement
        cen1,cen2=centaines(second_part,"si")
        if first_part == 1:
            answer1 = ref_sino["1000"] + cen1
        else:
            answer1 = ref_sino[str(first_part)] + ref_sino["1000"] + cen1
        # deuxième possibilité = composite sino coréen
        cen1,cen2=centaines(second_part,"co")
        if first_part == 1:
            answer2 = ref_sino["1000"] + cen2
        else:
            answer2 = ref_sino[str(first_part)] + ref_sino["1000"] + cen2
    return answer1, answer2

def construction_rep(number,type):
    #answer2 ne concerne que les nombres > 100 et le type "co" où deux écritures sont possibles
    if number < 11 :
        answer1=unites(number,type)
        answer2=0
    elif number > 10 and number < 101 :
        answer1=dizaines(number,type)
        answer2=0
    elif number > 100 and number <1001:
        answer1, answer2 = centaines(number, type)
    elif number > 1000 and number <10001:
        answer1, answer2 = milliers(number, type)
    return answer1, answer2

##########################################################################################

print("##########################################################################\n")
print("############# PROGRAMME DE REVISIONS DES NOMBRES EN COREEN ###############\n")
print("##########################################################################\n")

print("Programme valable jusqu'à 10000")

ref_sino, ref_cor_pur = dico_nb()  #prise en compte des noms des nombres sino-coréens et coréens

"""test, test2= construction_rep(6400, "co")
print(test)"""

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

nb_rep_justes=0

if niveau == "s" :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 100)
        reponse1,reponse2=construction_rep(nombre,sino)
        rep_utilisateur=input("Comment écrire "+str(nombre)+" en coréen? ")
        if rep_utilisateur==reponse1 :
            print("Bravo")
            nb_rep_justes+=1
        else :
            print("Réponse fausse. "+str(nombre)+" s'écrit "+ reponse1)
else :
    for i in range(1,int(nombre_a_reviser)+1):
        nombre=r.randint(0, 10000)
        print(nombre)
        reponse1, reponse2 = construction_rep(nombre, sino)
        if nombre > 100 and sino=="co":
            rep_utilisateur1 = input("Comment écrire " + str(nombre) + " en système purement sino? ")
            if rep_utilisateur1==reponse1 :
                print("Bravo")
                nb_rep_justes+=1
            else :
                print("Réponse fausse. "+str(nombre)+" s'écrit "+ reponse1)
            rep_utilisateur2 = input("Comment écrire " + str(nombre) + " en système sino et coréen? ")
            if rep_utilisateur2==reponse2 :
                print("Bravo")
                nb_rep_justes+=1
            else :
                print("Réponse fausse. "+str(nombre)+" s'écrit "+ reponse2)
        else :
            rep_utilisateur = input("Comment écrire " + str(nombre) + " en coréen? ")
            if rep_utilisateur == reponse1:
                print("Bravo")
                nb_rep_justes += 1
            else:
                print("Réponse fausse. " + str(nombre) + " s'écrit " + reponse1)

print(str(nb_rep_justes)+" réponses justes sur "+ str(nombre_a_reviser))


print("Fin du programme de révisions")