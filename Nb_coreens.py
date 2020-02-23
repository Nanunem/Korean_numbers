#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import random as r


def dico_nb():
    dico_sino = {}
    dico_cor_pur = {}
    with open("Dico_sino", "r") as fic_sino:
        for line in fic_sino:
            line = line.strip()
            line = line.split(":")
            if len(line) > 1:
                dico_sino[line[0]] = line[1]
            else:
                break
    with open("Dico_cor_pur", "r") as fic_cor_pur:
        for line in fic_cor_pur:
            line = line.strip()
            line = line.split(":")
            if len(line) > 1:
                dico_cor_pur[line[0]] = line[1]
            else:
                break
    return dico_sino, dico_cor_pur


def units(number, type):
    if type == "ko":
        ans1 = ref_cor_pur[str(number)]
    elif type == "si":
        ans1 = ref_sino[str(number)]
    return ans1


def tens(number, type):
    if number > 9 and number < 101 and number % 10 == 0:
        if type == "ko":
            ans1 = ref_cor_pur[str(number)]
        elif type == "si":
            if number == 10 :
                ans1 = ref_sino["10"]
            else :
                first_part = number // 10
                ans1 = ref_sino[str(first_part)] + ref_sino["10"]
    elif number < 101 and number % 10 != 0:
        if type == "ko":
            first_part = number // 10 * 10
            second_part = number % 10
            ans1 = ref_cor_pur[str(first_part)] + ref_cor_pur[str(second_part)]
        elif type == "si":
            first_part = number // 10
            second_part = number % 10
            ans1 = ref_sino[str(first_part)] + ref_sino["10"] + ref_sino[str(second_part)]
    return ans1


def hundreds(number, type):
    first_part = number // 100
    second_part = number % 100
    if type == "si":
        if second_part < 10 and second_part > 0:
            diz = units(second_part, "si")
        elif second_part == 0:
            diz = ""
        else:
            diz = tens(second_part, "si")
        if first_part == 1:
            ans1 = ref_sino["100"] + diz
        else:
            ans1 = ref_sino[str(first_part)] + ref_sino["100"] + diz
        ans2 = 0
    elif type == "ko":
        # first option = only using sino numbers
        if second_part < 10 and second_part > 0:
            diz = units(second_part, "si")
        elif second_part == 0:
            diz = ""
        else:
            diz = tens(second_part, "si")
        if first_part == 1:
            ans1 = ref_sino["100"] + diz
        else:
            ans1 = ref_sino[str(first_part)] + ref_sino["100"] + diz
        # second option = sino korean mix
        if second_part < 10 and second_part > 0:
            diz = units(second_part, "ko")
        elif second_part == 0:
            diz = ""
        else:
            diz = tens(second_part, "ko")
        if first_part == 1:
            ans2 = ref_sino["100"] + diz
        else:
            ans2 = ref_sino[str(first_part)] + ref_sino["100"] + diz
    return ans1, ans2


def thousands(number, type):
    first_part = number // 1000
    second_part = number % 1000
    if type == "si":
        hun1, hun2 = hundreds(second_part, "si")
        if first_part == 1:
            answer1 = ref_sino["1000"] + hun1
        else:
            answer1 = ref_sino[str(first_part)] + ref_sino["1000"] + hun1
        answer2 = 0
    elif type == "ko":
        # first option = only using sino numbers
        hun1, hun2 = hundreds(second_part, "si")
        if first_part == 1:
            answer1 = ref_sino["1000"] + hun1
        else:
            answer1 = ref_sino[str(first_part)] + ref_sino["1000"] + hun1
        # second option = sino korean mix
        hun1, hun2 = hundreds(second_part, "ko")
        if first_part == 1:
            answer2 = ref_sino["1000"] + hun2
        else:
            answer2 = ref_sino[str(first_part)] + ref_sino["1000"] + hun2
    return answer1, answer2


def building_answer(number, type):
    # answer2 only used for numbers above 100 and for the choice "ko"
    if number < 11:
        answer1 = units(number, type)
        answer2 = 0
    elif number > 10 and number < 101:
        answer1 = tens(number, type)
        answer2 = 0
    elif number > 100 and number < 1001:
        answer1, answer2 = hundreds(number, type)
    elif number > 1000 and number < 10001:
        answer1, answer2 = thousands(number, type)
    return answer1, answer2


##########################################################################################

print("##########################################################################\n")
print("############# REVIEW KOREAN NUMBERS UP TO 100000 ###############\n")
print("##########################################################################\n")

print("Version up to 10000 numbers")

ref_sino, ref_cor_pur = dico_nb()  # dictionaries to build the answers

number_to_review = input("How any numbers do you want to review?  ")

if float(number_to_review) == 0:
    print("End of the review session")
    sys.exit()
else:
    while number_to_review.isdigit() == False:
        print("Error, please write a positive integer")
        number_to_review = input("How any numbers do you want to review?  ")

level = input("Simple (\"s\") or complicated (\"c\") session?  ")  # complicated being numbers above 100
while level != "C" and level != "c" and level != "s" and level != "S":
    print("Error, s ou c are the only answers accepted")
    level = input("Simple (\"s\") or complicated (\"c\") session?  ")

sino = input("Review korean numbers (\"ko\") or sino-korean (\"si\") ?")
while sino != "KO" and sino != "Ko" and sino != "ko" and sino != "SI" and sino != "Si" and sino != "si":
    print("Error in the type of review to perform, \"ko\" or \"si\" only")
    sino = input("Review korean numbers (\"ko\") or sino-korean (\"si\") ?")

if sino=="KO" or "Ko" :
    sino=="ko"
elif sino=="SI" or "Si" :
    sino=="si"

right_answers = 0

if level == "s":
    for i in range(1, int(number_to_review) + 1):
        number = r.randint(0, 100)
        answer1, answer2 = building_answer(number, sino)
        user_answer = input("How would you write " + str(number) + " in Korean? ")
        if user_answer == answer1:
            print("Bravo")
            right_answers += 1
        else:
            print("Wrong answer. " + str(number) + " should be written " + answer1)
else:
    for i in range(1, int(number_to_review) + 1):
        number = r.randint(0, 10000)
        print(number)
        answer1, answer2 = building_answer(number, sino)
        if number > 100 and sino == "co":
            rep_utilisateur1 = input("How would you write " + str(number) + " using only a sino form? ")
            if rep_utilisateur1 == answer1:
                print("Bravo")
                right_answers += 1
            else:
                print("Wrong answer. " + str(number) + " should be written " + answer1)
            rep_utilisateur2 = input("How would you write " + str(number) + " using a mix of sino and korean numbers? ")
            if rep_utilisateur2 == answer2:
                print("Bravo")
                right_answers += 1
            else:
                print("Wrong answer. " + str(number) + " should be written " + answer2)
        else:
            user_answer = input("How would you write " + str(number) + " in Korean? ")
            if user_answer == answer1:
                print("Bravo")
                right_answers += 1
            else:
                    print("Wrong answer. " + str(number) + " should be written " + answer1)

print(str(right_answers) + " correct answers out of " + str(number_to_review))

print("End of the review session")
