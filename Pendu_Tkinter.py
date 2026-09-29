""""
Interface graphique
Auteur: Nemo CHARPENTIER
29/09/2026
"""

import Pendu_Lib
from tkinter import Tk, Label, Button, Entry , Canvas, PhotoImage


Fenetre = Tk()
Fenetre.title("Jeu du pendu")

labelHello = Label(Fenetre, text = "Jeu du pendu", fg= 'blue')
labelHello.pack()

buttonQuitt = Button (Fenetre, text="QUITTER", fg = 'red', command = Fenetre.destroy)
buttonQuitt.pack()

Largeur = 480
Hauteur = 320
Canevas= Canvas(Fenetre, width = Largeur, height =Hauteur, bg = 'white')
Canevas.pack(padx= 5, pady = 5)
image_pendu = PhotoImage(file = "image/bonhomme1.gif")

Canevas.create_image(Largeur /2, Hauteur /2, image = image_pendu)

Fenetre.mainloop()