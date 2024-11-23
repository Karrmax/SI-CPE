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
        # tk.Button(self, text="Back to Lobby", command=self.goLobby).pack()
        
        # Création du canvas avec la largeur et la hauteur de l'écran, fond noir
        self.canvas = tk.Canvas(self, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
        self.canvas.pack()
        
        # Initialisation de la logique du jeu avec une cible de 60 FPS
        self.gameLogic = GameLogic(self, load_manager, target_fps=60)

        # Bind the Esc key to pause the game
        root.bind("<KeyRelease-Escape>", self.toggle_pause)

        self.paused = False
        self.pause_menu_buttons = []

    def goLobby(self):
        """
        Change l'écran pour le lobby et réinitialise la logique du jeu.
        """
        # Changer l'écran pour le lobby
        self.switch_callback("lobby")
        # Réinitialiser la logique du jeu
        self.gameLogic = GameLogic(self, self.load_manager, target_fps=60)
        
    def start_game_loop(self):
        """
        Démarre la boucle de jeu.
        """
        self.gameLogic.start()

    def toggle_pause(self, event=None):
        if self.paused:
            self.resume_game()
        else:
            self.pause_game()

    def pause_game(self):
        self.paused = True
        self.gameLogic.pause()

        # Griser l'arrière-plan
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="gray", stipple="gray50")

        # Afficher le texte "Paused"
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 - 200, text="Paused", font=("Arial", 36), fill="white")

              # Créer les boutons de pause
        resume_button = tk.Button(self.canvas, text="Resume", command=self.resume_game, bg="black", fg="white", font=("Arial", 24), padx=20, pady=10)
        resume_button_window = self.canvas.create_window(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, window=resume_button)
        self.pause_menu_buttons.append(resume_button_window)

        quit_button = tk.Button(self.canvas, text="Quit to Lobby", command=self.goLobby, bg="black", fg="white", font=("Arial", 24), padx=20, pady=10)
        quit_button_window = self.canvas.create_window(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 + 100, window=quit_button)
        self.pause_menu_buttons.append(quit_button_window)

    def resume_game(self):
        self.paused = False
        self.gameLogic.unPause()

        # Supprimer les boutons de pause
        for button in self.pause_menu_buttons:
            self.canvas.delete(button)
        self.pause_menu_buttons.clear()

        # Supprimer le rectangle gris et le texte "Paused"
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.load_manager.get_resource('background'), anchor="nw")
