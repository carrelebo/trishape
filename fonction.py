#les lettres des points du triangle

def let1():
    let1 = str(input("Domme moi la lettre du premier point du triangle (en majuscule) : "))

def let2():
    let2 = str(input("Donne moi la lettre du deuxième point du triangle (en majuscule) : "))

def let3():
     let3 = str(input("Donne moi la lettre du troisième point du triangle (en majuscule) : "))

#les mesures des segments du triangle

def mseg1():
    m_seg1 = input("Combien mesure le segment [" + str(let1) + str(let2) + "] ? : ")
    if m_seg1 != int:
        print ("Veuillez entrer un nombre entier et non une lettre ou autres caractère")
        print("")
        mseg1()

def mseg2():
    m_seg2 = int(input("Combien mesure le segment [" + str(let1) + str(let3) + "] ? : "))
    if m_seg2 != int:
        print ("Veuillez entrer un nombre entier et non une lettre ou autres caractère")
        print("")
        mseg2()

def mseg3():
    m_seg3 = int(input("Combien mesure le segment [" + str(let2) + str(let3) + "] ? : "))
    if m_seg3 != int:
        print ("Veuillez entrer un nombre entier et non une lettre ou autres caractère")
        print("")
        mseg3()