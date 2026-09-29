"""
Pour interagir avec le joueur dans la console (version 1 de 2.Version console)
Il n'est utilise que si l'utilisateur veut jouer en mode console
Auteur: Nemo CHARPENTIER
29/09/2026
"""
import Pendu_Lib

def demander_lettre():                                      #Recupere la lettre du joueur
    lettre = input ("Donnez une lettre : ").lower()
    if len(lettre) > 1:
        print("Erreur une seule lettre")
        lettre = lettre[0]
    return lettre

def jouer_partie(liste_mots):
    mot = Pendu_Lib.choisir_mots(liste_mots)
    lettres_donnees = [mot[0]]
    chance = 8
    while chance > 0 and not Pendu_Lib.mot_trouve(mot, lettres_donnees):
        print("Mot : ", Pendu_Lib.prepare_mots(mot, lettres_donnees))
        print("Chance restantes: ", chance )
        lettre  = demander_lettre()

        if lettre in mot:
           lettres_donnees.append(lettre)
           print("Lettre trouve")
        else:
            chance = chance -1
            print("Mauvaise lettre")
    if chance >0:
           print("Gagner le mot etait ", mot)
    else: 
           print("Perdu le mot etait ", mot)

liste_mots = Pendu_Lib.lire_mots()
jouer_partie(liste_mots)
