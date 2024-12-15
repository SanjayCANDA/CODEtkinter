"""
Fichier: Grid.py
Description: Contient la classe Grid, qui représente la logique de la grille pour Puissance 4.
"""

class Grid:
    """
    Classe représentant la grille logique du jeu Puissance 4.
    """
    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        """
        Initialise une grille vide.
        """
        self.grid = [[' ' for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

    def drop_token(self, column, token):
        """
        Insère un jeton dans une colonne donnée si possible.

        Args:
            column (int): La colonne où insérer le jeton (0-indexé).
            token (str): Le jeton du joueur ('X' ou 'O').

        Returns:
            tuple: (row, column) si l'insertion est réussie, None sinon.
        """
        if column < 0 or column >= self.COLUMNS or self.grid[0][column] != ' ':
            return None

        for row in reversed(range(self.ROWS)):
            if self.grid[row][column] == ' ':
                self.grid[row][column] = token
                return (row, column)
        return None

    def check_winner(self, token):
        """
        Vérifie si un joueur a gagné.

        Args:
            token (str): Le jeton du joueur à vérifier ('X' ou 'O').

        Returns:
            bool: True si le joueur a gagné, False sinon.
        """
        # Vérifie les lignes
        for row in self.grid:
            for col in range(self.COLUMNS - 3):
                if all(cell == token for cell in row[col:col + 4]):
                    return True

        # Vérifie les colonnes
        for col in range(self.COLUMNS):
            for row in range(self.ROWS - 3):
                if all(self.grid[row + i][col] == token for i in range(4)):
                    return True

        # Vérifie les diagonales montantes
        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if all(self.grid[row + i][col + i] == token for i in range(4)):
                    return True

        # Vérifie les diagonales descendantes
        for row in range(3, self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.grid[row - i][col + i] == token for i in range(4)):
                    return True

        return False

    def is_full(self):
        """
        Vérifie si la grille est pleine.

        Returns:
            bool: True si la grille est pleine, False sinon.
        """
        return all(self.grid[0][col] != ' ' for col in range(self.COLUMNS))

