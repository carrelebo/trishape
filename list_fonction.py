#list des praincipales fonctions utiliser pour compacter le code à un très grand niveau ! :)

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
    m_seg1 = float(input("Combien mesure le segment [" + str(letchoice1) + str(letchoice2) + "] ? : "))
    m_segchoice1 = m_seg1

def mseg2fon():
    global m_segchoice2
    m_seg2 = float(input("Combien mesure le segment [" + str(letchoice1) + str(letchoice3) + "] ? : "))
    m_segchoice2 = m_seg2

def mseg3fon():
    global m_segchoice3
    m_seg3 = float(input("Combien mesure le segment [" + str(letchoice2) + str(letchoice3) + "] ? : "))
    m_segchoice3 = m_seg3

def special_perimetre():
    sigma_allm = m_segchoice1 + m_segchoice2 + m_segchoice3
    
    print("Le trangle " + str(letchoice1) + str(letchoice2) + str(letchoice3) + " qui a pour segements [" + str(letchoice1) + str(letchoice2) + "]" +"[" + str(letchoice1)
     + str(letchoice3) + "]" +"[" + str(letchoice2) + str(letchoice3) + "] " + "à un périmètre de " + str(sigma_allm) + str(unitychoice) + " :)")

def perimetrecomp():
    unityfon()

    let1fon()
    let2fon()
    let3fon()

    mseg1fon()
    mseg2fon()
    mseg3fon()

    special_perimetre()    


def perimetre():
    unity = str(input("Quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))

    print("")

    let1 = str(input("Donne moi la lettre du premier point du triangle (en majuscule) : "))
    let2 = str(input("Donne moi la lettre du deuxième point du triangle (en majuscule) : "))
    let3 = str(input("Donne moi la lettre du troisième point du triangle (en majuscule) : "))

    print("")

    m_seg1 = float(input("Combien mesure le segment [" + str(let1) + str(let2) + "] (juste le nombre) ? : "))
    m_seg2 = float(input("Combien mesure le segment [" + str(let1) + str(let3) + "] (juste le nombre) ? : "))
    m_seg3 = float(input("Combien mesure le segment [" + str(let2) + str(let3) + "] (juste le nombre) ? : "))

    sigma_allm = m_seg1 + m_seg2 + m_seg3

    print("")

    print("Le trangle " + str(let1) + str(let2) + str(let3) + " qui a pour segements [" + str(let1) + str(let2) + "]" +"[" + str(let1)
     + str(let3) + "]" +"[" + str(let2) + str(let3) + "] " + "à un périmètre de " + str(sigma_allm) + str(unity) + " :)")

    print("")