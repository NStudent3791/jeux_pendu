"""
Fichier pour le fonctionnement de base du jeu du pendu et 
independant de l'affichage pour pouvoir etre reutiliser dans la version tkinter
Auteur: Nemo CHARPENTIER
29/09/2026
"""
import random


def lire_mots():                                        #Cree une liste de mots de MOTS.txt qui ont 5lettres ou plus 
    liste_mots = []
    fich = open("MOTS.txt", 'r')
    for ligne in fich:
        mot = ligne.strip()                             #Enleve un caractere inivisble "\n"
        if len(mot) >= 5:
            liste_mots.append(mot)
    fich.close()
    return liste_mots

def choisir_mots(liste_mot):                            #Choisi le mots aleatoirement
    numero = random.randint(0, len(liste_mot) - 1)
    mot = liste_mot[numero]
    return mot

def prepare_mots(mot, lettres_donnees):                 #Contruire l'affichage avec _ 
    texte = ""
    for lettre in mot:
        if lettre in lettres_donnees:
           texte = texte + lettre + " "
        else:
          texte = texte + "_ "
    return texte

def mot_trouve(mot, lettres_donnees):
    trouve = True
    for lettre in mot:
        if lettre not in lettres_donnees:
            trouve = False
    return trouve