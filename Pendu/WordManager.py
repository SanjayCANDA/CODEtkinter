"""
Fichier: WordManager.py
Description: Contient la classe WordManager, qui gère les mots pour le jeu du pendu.
"""

import random

class WordManager:
    """
    Classe pour gérer les mots du jeu du pendu.
    """
    def __init__(self, word_list=None):
        """
        Initialise le gestionnaire de mots.

        Args:
            word_list (list[str], optionnel): Liste des mots disponibles. 
            Si None, une liste par défaut est utilisée.
        """
        self.word_list = word_list or ["python", "pendu", "ordinateur", "programmation", "interface"]

    def choose_word(self):
        """
        Sélectionne un mot aléatoire dans la liste.

        Returns:
            str: Le mot sélectionné.
        """
        return random.choice(self.word_list)
