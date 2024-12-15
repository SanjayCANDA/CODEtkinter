"""
Fichier: main.py
Description: Fichier principal pour lancer le jeu Morpion avec une interface graphique.
"""

import tkinter as tk
from Player import Player
from Game import Game

if __name__ == "__main__":
    # Création des joueurs
    player1_name = input("Entrez le nom du joueur 1 : ")
    player2_name = input("Entrez le nom du joueur 2 : ")

    player1 = Player(player1_name, 'X')
    player2 = Player(player2_name, 'O')

    # Création de la fenêtre Tkinter et démarrage du jeu
    root = tk.Tk()
    game = Game(root, player1, player2)
    root.mainloop()
