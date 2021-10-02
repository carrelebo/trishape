import math
import time

print("""
Bievenue sur l'application console tripshape,

l'application qui utilise le théorème de pythagore

(ne prend seulement en compte les variable entière "int")

""")

def pythagore():

    let1 = str(input("domme moi la lettre du premier segment : "))
    let2 = str(input("donne moi la lettre du deuxième segment : "))
    let3 = str(input("donne moi la lettre du dernier segment : "))

    triangle = let1, let2, let3

    print("""
    
    """)
#seg1 = str(input("donne moi le nom du premier segment : "))
#seg2 = str(input("sonne moi le nom du deucième segment : "))
#seg3 = str(input("donne moi le nom du troisème segment : "))
    
#triseg = seg1, seg2, seg3
    
    m_seg1 = int(input("combien mesure le segment [" + str(let1) + str(let2) + "] ? : "))
    m_seg2 = int(input("combien mesure le segment [" + str(let1) + str(let3) + "] ? : "))
    m_seg3 = int(input("combien mesure le segment [" + str(let2) + str(let3) + "] ? : "))

    allm = m_seg1, m_seg2, m_seg3
    add_allm = m_seg1 + m_seg2 + m_seg3

    print("le trangle" + str(let1) + str(let2) + str(let3) + "qui a pour segement [" + str(let1) + str(let2) + "]" + "[" + str(let1) + str(let3) + "]" + "[" + str(let2) + str(let3) + "]" + "à un périmètre de " + str(add_allm) + " :)")

pythagore()