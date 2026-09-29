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

        if lettre in lettres_donnees:
           print("Lettre deja donnee")
        elif lettre in mot:
            lettres_donnees.append(lettre)
            print("Lettre trouvee")
        else:
             lettres_donnees.append(lettre)
             chance = chance - 1
             print("Mauvaise lettre")

    if chance >0:
           print("Gagner le mot etait ", mot)
    else: 
           print("Perdu le mot etait ", mot)
    return chance
def demande_rejouer():
     reponse = input("voulez vous rejouer ? o/n :").lower()
     while reponse != "o" and reponse != "n":
          reponse = input("repondez par o ou n :").lower()
     return reponse

liste_mots = Pendu_Lib.lire_mots()
meilleur_score = 0
rejouer = "o"

while rejouer == "o":
     score = jouer_partie(liste_mots)
     if score > meilleur_score:
          meilleur_score = score
     print("votre score :", score)
     print("meilleur score:", meilleur_score)
     rejouer = demande_rejouer()
     print("au revoir")
