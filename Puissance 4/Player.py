"""
Fichier: Player.py
Description: Contient la classe Player, qui représente un joueur du Puissance 4.
"""

class Player:
    """
    Classe représentant un joueur dans le jeu Puissance 4.
    """
    def __init__(self, name, token):
        """
        Initialise un joueur avec un nom et un jeton.

        Args:
            name (str): Le nom du joueur.
            token (str): Le jeton du joueur ('X' ou 'O').
        """
        self.name = name
        self.token = token
