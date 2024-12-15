"""
Fichier: Game.py
Description: Contient la classe Game, qui gère la logique principale et l'interface graphique.
"""

import tkinter as tk
from tkinter import messagebox
from Grid import Grid
from Player import Player

class Game:
    """
    Classe principale pour gérer la logique et l'interface graphique de Puissance 4.
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
        self.root.title("Puissance 4")
        self.grid = Grid()
        self.players = [player1, player2]
        self.current_player_index = 0

        self.buttons = []
        self.board = []

        self.setup_ui()

    def setup_ui(self):
        """
        Configure l'interface utilisateur pour le jeu.
        """
        # Boutons pour les colonnes
        frame = tk.Frame(self.root)
        frame.pack()
        for col in range(Grid.COLUMNS):
            btn = tk.Button(frame, text=f"↓ {col+1}", command=lambda c=col: self.play_turn(c))
            btn.grid(row=0, column=col)
            self.buttons.append(btn)

        # Grille de jeu
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        for row in range(Grid.ROWS):
            row_widgets = []
            for col in range(Grid.COLUMNS):
                lbl = tk.Label(self.board_frame, text=" ", width=4, height=2, borderwidth=2, relief="solid", font=("Arial", 16))
                lbl.grid(row=row, column=col)
                row_widgets.append(lbl)
            self.board.append(row_widgets)

    def play_turn(self, column):
        """
        Gère le tour du joueur actuel.

        Args:
            column (int): Colonne choisie par le joueur.
        """
        player = self.players[self.current_player_index]
        result = self.grid.drop_token(column, player.token)

        if result is None:
            messagebox.showwarning("Erreur", f"Colonne {column+1} pleine ou invalide !")
            return

        row, col = result
        self.board[row][col].config(text=player.token, fg="red" if player.token == 'X' else "blue")

        if self.grid.check_winner(player.token):
            self.end_game(f"{player.name} a gagné ! Félicitations !")
            return

        if self.grid.is_full():
            self.end_game("Match nul ! La grille est pleine.")
            return

        self.current_player_index = 1 - self.current_player_index

    def end_game(self, message):
        """
        Termine le jeu avec un message.

        Args:
            message (str): Message à afficher.
        """
        messagebox.showinfo("Fin du jeu", message)
        self.root.destroy()
