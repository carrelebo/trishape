import math
import time

print("""
Bievenue sur l'application console tripshape-flushed,
l'application qui est faites pour faire des calculs avec des triangles
(ne prend seulement en compte les variable entière "int")

""")

def perimetre():

    unity = str(input("quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))

    print("")

    let1 = str(input("domme moi la lettre du premier point du triangle (en majuscule) : "))
    let2 = str(input("donne moi la lettre du deuxième point du triangle (en majuscule) : "))
    let3 = str(input("donne moi la lettre du troisième point du triangle (en majuscule) : "))

    print("""
    """)
    
    m_seg1 = input("combien mesure le segment [" + str(let1) + str(let2) + "] ? : ")
    if m_seg1 != int:
        print ("veuillez entré un nombre entier et non une lettre ou autres caractère")

    m_seg2 = int(input("combien mesure le segment [" + str(let1) + str(let3) + "] ? : "))

    m_seg3 = int(input("combien mesure le segment [" + str(let2) + str(let3) + "] ? : "))

    add_allm = m_seg1 + m_seg2 + m_seg3

    print("")
    print("le trangle " + str(let1) + str(let2) + str(let3) + " qui a pour segements [" + str(let1) + str(let2) + "]" + "[" + str(let1) + str(let3) + "]" + "[" + str(let2) + str(let3) + "] " + "à un périmètre de " + str(add_allm) + str(unity) + " :)")

    print("")

perimetre()

def screenon():
    time.sleep(5)
    screenon()

screenon()