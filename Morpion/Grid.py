"""
Fichier: Grid.py
Description: Contient la classe Grid, qui représente la logique de la grille pour le jeu Morpion (Tic-Tac-Toe).
"""

class Grid:
    """
    Classe représentant la grille du jeu Morpion.
    """
    SIZE = 3  # La grille est de taille 3x3

    def __init__(self):
        """
        Initialise une grille vide.
        """
        self.grid = [[' ' for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def display(self):
        """
        Affiche la grille dans la console (utile pour les tests).
        """
        for row in self.grid:
            print(' | '.join(row))
            print('-' * 5)

    def set_move(self, row, col, token):
        """
        Place un jeton (X ou O) à la position spécifiée.

        Args:
            row (int): La ligne où insérer le jeton (0-2).
            col (int): La colonne où insérer le jeton (0-2).
            token (str): Le jeton du joueur ('X' ou 'O').

        Returns:
            bool: True si le coup est valide, False sinon.
        """
        if self.grid[row][col] == ' ':
            self.grid[row][col] = token
            return True
        return False

    def check_winner(self, token):
        """
        Vérifie si le joueur a gagné.

        Args:
            token (str): Le jeton du joueur ('X' ou 'O').

        Returns:
            bool: True si le joueur a gagné, False sinon.
        """
        # Vérifie les lignes
        for row in self.grid:
            if all(cell == token for cell in row):
                return True

        # Vérifie les colonnes
        for col in range(self.SIZE):
            if all(self.grid[row][col] == token for row in range(self.SIZE)):
                return True

        # Vérifie les diagonales
        if all(self.grid[i][i] == token for i in range(self.SIZE)):
            return True
        if all(self.grid[i][self.SIZE - 1 - i] == token for i in range(self.SIZE)):
            return True

        return False

    def is_full(self):
        """
        Vérifie si la grille est pleine.

        Returns:
            bool: True si la grille est pleine, False sinon.
        """
        return all(self.grid[row][col] != ' ' for row in range(self.SIZE) for col in range(self.SIZE))
