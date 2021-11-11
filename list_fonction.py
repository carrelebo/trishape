#list des praincipales fonctions utiliser pour compacter le code à un très grand niveau ! :)
from math import *

def unityfon():
    global unitychoice
    unity = str(input("Quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))
    unitychoice = unity

def let1fon():
    global letchoice1
    let1 = str(input("Donne moi la lettre du 1er point du triangle (en majuscule) : "))
    letchoice1 = let1

def let2fon():
    global letchoice2
    let2 = str(input("Donne moi la lettre du 2ème point du triangle (en majuscule) : "))
    letchoice2 = let2

def let3fon():
    global letchoice3
    let3 = str(input("Donne moi la lettre du 3ème point du triangle (en majuscule) : "))
    letchoice3 = let3

def mseg1fon():
    global m_segchoice1
    try:
        m_seg1 = float(input("Combien mesure le segment [" + str(letchoice1) + str(letchoice2) + "] ? : "))
        m_segchoice1 = m_seg1
    except ValueError:
        print("Veuillez entrer un nombre !")
        mseg1fon()

def mseg2fon():
    try:
        global m_segchoice2
        m_seg2 = float(input("Combien mesure le segment [" + str(letchoice1) + str(letchoice3) + "] ? : "))
        m_segchoice2 = m_seg2
    except ValueError:
        print("Veuillez entrer un nombre !")
        mseg2fon()

def mseg3fon():
    try:
        global m_segchoice3
        m_seg3 = float(input("Combien mesure le segment [" + str(letchoice2) + str(letchoice3) + "] ? : "))
        m_segchoice3 = m_seg3
    except ValueError:
        print("Veuillez entrer un nombre !")
        mseg3fon()

def special_perimetre():
    sigma_allm = float(m_segchoice1) + float(m_segchoice2) + float(m_segchoice3)
    
    print("Le trangle " + str(letchoice1) + str(letchoice2) + str(letchoice3) + " qui a pour segements [" + str(letchoice1) + str(letchoice2) + "]" +"[" + str(letchoice1)
     + str(letchoice3) + "]" +"[" + str(letchoice2) + str(letchoice3) + "] " + "à un périmètre de " + str(sigma_allm) + str(unitychoice) + " :)")

def special_pythagore():
    if m_segchoice1 == sqrt(m_segchoice2**2 + m_segchoice3**2):
        print("d'après le théorème de pythagore, le triangle est rectangle")
    if m_segchoice2 == sqrt(m_segchoice1**2 + m_segchoice3**2):
        print("d'après le théorème de pythagore, le triangle est rectangle")
    if m_segchoice3 == sqrt(m_segchoice2**2 + m_segchoice1**2):
        print("d'après le théorème de pythagore, le triangle est rectangle")
    else:
        print("d'après le théorème de pythagore, le triangle n'est pas rectangle")

def perimetre():
    unityfon()

    let1fon()
    let2fon()
    let3fon()

    mseg1fon()
    mseg2fon()
    mseg3fon()

    special_perimetre()

def pythagore():
    unityfon()

    let1fon()
    let2fon()
    let3fon()

    mseg1fon()
    mseg2fon()
    mseg3fon()

    special_pythagore()