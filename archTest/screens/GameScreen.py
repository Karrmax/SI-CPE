import tkinter as tk
from game.GameLogic import GameLogic

class GameScreen(tk.Frame):
    """
    Classe représentant l'écran de jeu.
    
    Attributs:
        switch_callback (function): Fonction de rappel pour changer d'écran.
        load_manager (LoadManager): Gestionnaire de chargement.
        canvas (tk.Canvas): Canvas pour afficher le jeu.
        gameLogic (GameLogic): Logique du jeu.
    """
    def __init__(self, root, switch_callback, load_manager):
        """
        Initialise l'écran de jeu.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switch_callback (function): Fonction de rappel pour changer d'écran.
            load_manager (LoadManager): Gestionnaire de chargement.
        """
        super().__init__(root)
        self.switch_callback = switch_callback
        self.load_manager = load_manager
        
        # Bouton pour retourner au lobby
        tk.Button(self, text="Back to Lobby", command=lambda: self.goLobby()).pack()
        self.gameLogic = None
        # Création du canvas avec la largeur et la hauteur de l'écran, fond noir
        self.canvas = tk.Canvas(self, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
        self.canvas.pack()
        
        # Initialisation de la logique du jeu avec une cible de 60 FPS
        self.gameLogic = GameLogic(self, load_manager, target_fps=60)


    def goLobby(self):
        """
        Change l'écran pour le lobby et réinitialise la logique du jeu.
        """
        # self.gameLogic = None
        self.canvas.pack_forget()
        
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg="black")
        self.canvas.pack()
        self.gameLogic = GameLogic(self, self.load_manager, target_fps=60)
        
        
        # Changer l'écran pour le lobby
        self.switch_callback("lobby")
        # Réinitialiser la logique du jeu
        # self.gameLogic.reset()

        
    def start_game_loop(self):
        """
        Démarre la boucle de jeu.
        """
        self.gameLogic.start()
