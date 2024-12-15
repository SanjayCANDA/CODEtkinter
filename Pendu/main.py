"""
Fichier: main.py
Description: Fichier principal pour lancer le jeu du pendu avec une interface graphique.
"""

import tkinter as tk
from Player import Player
from Game import Game

if __name__ == "__main__":
    # Initialisation du joueur
    player_name = input("Entrez le nom du joueur : ")
    player = Player(player_name)

    # Création de la fenêtre Tkinter et démarrage du jeu
    root = tk.Tk()
    game = Game(root, player)
    root.mainloop()
