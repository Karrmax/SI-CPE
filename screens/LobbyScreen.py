"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: LobbyScreen
Description: Cette classe représente l'écran du lobby. Elle permet de naviguer vers le jeu ou le tableau des scores.
TODO: Ajouter des fonctionnalités spécifiques pour l'écran du lobby, comme des animations, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

import tkinter as tk

class LobbyScreen(tk.Frame):
    """
    Classe représentant l'écran du lobby.
    
    Attributs:
        switch_callback (function): Fonction de rappel pour changer d'écran.
        loadManager (LoadManager): Gestionnaire de chargement des ressources.
        canvas (tk.Canvas): Canvas pour afficher le fond du lobby.
    """
    def __init__(self, root, switch_callback, loadManager):
        """
        Initialise l'écran du lobby.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switch_callback (function): Fonction de rappel pour changer d'écran.
            loadManager (LoadManager): Gestionnaire de chargement des ressources.
        """
        super().__init__(root)
        self.switch_callback = switch_callback
        self.loadManager = loadManager

        self.canvas = tk.Canvas(self, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)

        # Get the background image from LoadManager
        self.background_image = self.loadManager.getMainBG()
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Titre du lobby
        self.canvas.create_text(root.winfo_screenwidth() // 2, 100, text="SPACE INVADER", font=("Space Invaders", 36), fill="yellow")

        # Bouton pour démarrer le jeu
        start_button = tk.Button(self.canvas, text="Start Game", font=("Space Invaders", 24), fg="yellow", bg="black", command=lambda: self.switch_callback("game"))
        self.canvas.create_window(root.winfo_screenwidth() // 2, 200, window=start_button)

        # Bouton pour afficher le tableau des scores
        leaderboard_button = tk.Button(self.canvas, text="Leaderboard", font=("Space Invaders", 18), fg="yellow", bg="black", command=lambda: self.switch_callback("leaderboard"))
        self.canvas.create_window(root.winfo_screenwidth() // 2, 300, window=leaderboard_button)