#liste des principales variables à utiliser pour le développement des modules

#demander les unitées :

unity = str(input("Quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))

#demander les lettres des triangles:

let1 = str(input("Donne moi la lettre du premier point du triangle (en majuscule) : "))
let2 = str(input("Donne moi la lettre du deuxième point du triangle (en majuscule) : "))
let3 = str(input("Donne moi la lettre du troisième point du triangle (en majuscule) : "))

#demander les mesures des segments du triangle:
m_seg1 = float(input("Combien mesure le segment [" + str(let1) + str(let2) + "] ? : "))
m_seg2 = float(input("Combien mesure le segment [" + str(let1) + str(let3) + "] ? : "))
m_seg3 = float(input("Combien mesure le segment [" + str(let2) + str(let3) + "] ? : "))

#pour la fonction perimètre
sigma_allm = m_seg1 + m_seg2 + m_seg3
