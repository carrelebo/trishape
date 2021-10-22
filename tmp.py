#coe temporaire, là où sont parfois construit les fonctions
import math
import time
import os

def perimetre():
    unity = str(input("Quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))

    print("")

    let1 = str(input("Donne moi la lettre du premier point du triangle (en majuscule) : "))
    let2 = str(input("Donne moi la lettre du deuxième point du triangle (en majuscule) : "))
    let3 = str(input("Donne moi la lettre du troisième point du triangle (en majuscule) : "))

    print("")

    m_seg1 = input("Combien mesure le segment [" + str(let1) + str(let2) + "] (juste le nombre) ? : ")
    m_seg2 = input("Combien mesure le segment [" + str(let1) + str(let3) + "] (juste le nombre) ? : ")
    m_seg3 = input("Combien mesure le segment [" + str(let2) + str(let3) + "] (juste le nombre) ? : ")

    sigma_allm = float(m_seg1) + float(m_seg2) + float(m_seg3)

    print("")

    print("Le trangle " + str(let1) + str(let2) + str(let3) + " qui a pour segements [" + str(let1) + str(let2) + "]" +"[" + str(let1)
     + str(let3) + "]" +"[" + str(let2) + str(let3) + "] " + "à un périmètre de " + str(sigma_allm) + str(unity) + " :)")

    print("")

perimetre()