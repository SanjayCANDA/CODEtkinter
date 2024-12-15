"""
Fichier: Player.py
Description: Contient la classe Player, qui représente un joueur du jeu du pendu.
"""

class Player:
    """
    Classe représentant un joueur dans le jeu du pendu.
    """
    def __init__(self, name):
        """
        Initialise un joueur avec un nom.

        Args:
            name (str): Le nom du joueur.
        """
        self.name = name
        self.mistakes = 0
        self.max_mistakes = 6
        self.guessed_letters = set()

    def add_mistake(self):
        """
        Ajoute une erreur au compteur du joueur.
        """
        self.mistakes += 1

    def is_hanged(self):
        """
        Vérifie si le joueur a atteint le maximum d'erreurs.

        Returns:
            bool: True si le joueur a perdu, False sinon.
        """
        return self.mistakes >= self.max_mistakes
