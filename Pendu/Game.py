"""
Fichier: Game.py
Description: Contient la classe Game, qui gère la logique principale et l'interface graphique.
"""

import tkinter as tk
from tkinter import messagebox
from WordManager import WordManager
from Player import Player

class Game:
    """
    Classe principale pour gérer la logique et l'interface graphique du jeu du pendu.
    """
    def __init__(self, root, player):
        """
        Initialise le jeu du pendu avec un joueur et une interface graphique.

        Args:
            root (Tk): Fenêtre principale Tkinter.
            player (Player): Le joueur.
        """
        self.root = root
        self.player = player
        self.word_manager = WordManager()
        self.word_to_guess = self.word_manager.choose_word()
        self.hidden_word = ["_" for _ in self.word_to_guess]

        self.setup_ui()

    def setup_ui(self):
        """
        Configure l'interface utilisateur pour le jeu.
        """
        self.root.title("Jeu du Pendu")

        # Label pour afficher le mot à deviner
        self.word_label = tk.Label(self.root, text=" ".join(self.hidden_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        # Zone de saisie pour les lettres
        self.letter_entry = tk.Entry(self.root, font=("Arial", 14), justify="center", width=5)
        self.letter_entry.pack(pady=10)

        # Bouton pour valider une lettre
        self.submit_button = tk.Button(self.root, text="Essayer", command=self.guess_letter)
        self.submit_button.pack(pady=10)

        # Label pour afficher les lettres déjà devinées
        self.guessed_letters_label = tk.Label(self.root, text="Lettres devinées : ", font=("Arial", 12))
        self.guessed_letters_label.pack(pady=10)

        # Label pour afficher le nombre d'erreurs
        self.mistakes_label = tk.Label(self.root, text=f"Erreurs : {self.player.mistakes} / {self.player.max_mistakes}", font=("Arial", 12))
        self.mistakes_label.pack(pady=10)

    def guess_letter(self):
        """
        Gère la logique lorsqu'un joueur devine une lettre.
        """
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre valide.")
            return

        if letter in self.player.guessed_letters:
            messagebox.showinfo("Info", "Vous avez déjà essayé cette lettre.")
            return

        self.player.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            self.reveal_letter(letter)
        else:
            self.player.add_mistake()
            self.mistakes_label.config(text=f"Erreurs : {self.player.mistakes} / {self.player.max_mistakes}")

        self.guessed_letters_label.config(text=f"Lettres devinées : {', '.join(sorted(self.player.guessed_letters))}")

        if "_" not in self.hidden_word:
            self.end_game(f"Félicitations {self.player.name}, vous avez gagné !")
        elif self.player.is_hanged():
            self.end_game(f"Dommage {self.player.name}, vous avez perdu ! Le mot était : {self.word_to_guess}")

    def reveal_letter(self, letter):
        """
        Révèle les positions de la lettre dans le mot caché.

        Args:
            letter (str): La lettre devinée correctement.
        """
        for i, char in enumerate(self.word_to_guess):
            if char == letter:
                self.hidden_word[i] = letter

        self.word_label.config(text=" ".join(self.hidden_word))

    def end_game(self, message):
        """
        Termine le jeu avec un message.

        Args:
            message (str): Message à afficher.
        """
        messagebox.showinfo("Fin du jeu", message)
        self.root.quit()
