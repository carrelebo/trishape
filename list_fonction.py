#list des praincipales fonction

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