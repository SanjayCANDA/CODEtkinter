"""
Fichier: Game.py
Description: Contient la classe Game, qui gère la logique principale et l'interface graphique pour le jeu Morpion.
"""

import tkinter as tk
from tkinter import messagebox
from Grid import Grid
from Player import Player

class Game:
    """
    Classe principale pour gérer la logique et l'interface graphique du jeu Morpion.
    """
    def __init__(self, root, player1, player2):
        """
        Initialise le jeu avec deux joueurs et une interface graphique.

        Args:
            root (Tk): Fenêtre principale Tkinter.
            player1 (Player): Le premier joueur.
            player2 (Player): Le second joueur.
        """
        self.root = root
        self.root.title("Jeu Morpion")
        self.grid = Grid()
        self.players = [player1, player2]
        self.current_player_index = 0

        self.buttons = []
        self.setup_ui()

    def setup_ui(self):
        """
        Configure l'interface utilisateur pour le jeu.
        """
        # Création des boutons pour chaque case de la grille
        for row in range(Grid.SIZE):
            row_buttons = []
            for col in range(Grid.SIZE):
                btn = tk.Button(self.root, text=" ", width=10, height=3, font=("Arial", 20),
                                command=lambda r=row, c=col: self.play_turn(r, c))
                btn.grid(row=row, column=col)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def play_turn(self, row, col):
        """
        Gère le tour du joueur actuel.

        Args:
            row (int): La ligne où le joueur souhaite jouer.
            col (int): La colonne où le joueur souhaite jouer.
        """
        player = self.players[self.current_player_index]
        
        # Si la case est déjà occupée, ne rien faire
        if self.grid.set_move(row, col, player.token):
            self.buttons[row][col].config(text=player.token, state="disabled")
            
            if self.grid.check_winner(player.token):
                self.end_game(f"Félicitations {player.name}, vous avez gagné !")
                return
            
            if self.grid.is_full():
                self.end_game("Match nul ! La grille est pleine.")
                return

            # Change de joueur
            self.current_player_index = 1 - self.current_player_index

    def end_game(self, message):
        """
        Termine le jeu avec un message.

        Args:
            message (str): Message à afficher.
        """
        messagebox.showinfo("Fin du jeu", message)
        self.root.quit()