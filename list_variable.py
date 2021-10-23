#liste des principales variables utilisées pour le développement des modules et des fontions

#demander les unitées :

unity = str(input("Quelle unité de longeur utilisez-vous (cm, m, km ect...) ? : "))

#demander les lettres des triangles:

let1 = str(input("Donne moi la lettre du premier point du triangle (en majuscule) : "))
letchoice1 = let1
let2 = str(input("Donne moi la lettre du deuxième point du triangle (en majuscule) : "))
letchoice2 = let2
let3 = str(input("Donne moi la lettre du troisième point du triangle (en majuscule) : "))
letchoice1 = let3

#demander les mesures des segments du triangle:
m_seg1 = float(input("Combien mesure le segment [" + str(let1) + str(let2) + "] ? : "))
m_segchoice1 = m_seg1
m_seg2 = float(input("Combien mesure le segment [" + str(let1) + str(let3) + "] ? : "))
m_seg1 = float(input("Combien mesure le segment [" + str(let1) + str(let2) + "] ? : "))
m_segchoice2 = m_seg2
m_seg3 = float(input("Combien mesure le segment [" + str(let2) + str(let3) + "] ? : "))
m_seg1 = float(input("Combien mesure le segment [" + str(let1) + str(let2) + "] ? : "))
m_segchoice3 = m_seg3

#pour la fonction perimètre
sigma_allm = m_segchoice1 + m_segchoice2 + m_segchoice3
