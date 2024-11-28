"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: MainRoot
Description: Cette classe représente la fenêtre principale de l'application et gère la navigation entre les différents écrans.
TODO: Ajouter des fonctionnalités spécifiques pour la fenêtre principale, comme des animations de transition, des effets visuels ou des interactions avancées avec les éléments de l'interface utilisateur.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

import tkinter as tk
from screens.LobbyScreen import LobbyScreen
from screens.LeaderboardScreen import LeaderboardScreen
from screens.GameScreen import GameScreen
from managers.LoadManager import LoadManager

class MainRoot:
    """
    Classe représentant la fenêtre principale de l'application.
    
    Attributs:
        root (tk.Tk): La fenêtre principale de l'application.
        loadManager (LoadManager): Le gestionnaire de chargement des ressources.
        screens (dict): Dictionnaire des écrans de l'application.
        currentScreen (tk.Frame): L'écran actuellement affiché.
    """
    def __init__(self):
        """
        Initialise la fenêtre principale de l'application.
        """
        self.root = tk.Tk()
        self.root.title("Tkinter Game")
        self.root.state('zoomed')

        self.loadManager = LoadManager()
        self.loadManager.load_resources()

        self.screens = {}
        self.currentScreen = None
        self.init_screens()

    def init_screens(self):
        """
        Initialise les écrans de l'application.
        """
        self.screens["lobby"] = LobbyScreen(self.root, self.switch_screen, self.loadManager)
        self.screens["leaderboard"] = LeaderboardScreen(self.root, self.switch_screen, self.loadManager)
        self.screens["game"] = GameScreen(self.root, self.switch_screen, self.loadManager)

        self.switch_screen("lobby")

    def switch_screen(self, screen_name):
        """
        Change l'écran actuellement affiché.
        
        Args:
            screen_name (str): Le nom de l'écran à afficher.
        """
        if self.currentScreen:
            self.currentScreen.pack_forget()
        self.currentScreen = self.screens[screen_name]
        
        self.currentScreen.pack(fill=tk.BOTH, expand=True)
        if isinstance(self.currentScreen, GameScreen):
            self.currentScreen.start_game_loop()
            
        if isinstance(self.currentScreen, LeaderboardScreen):
            self.currentScreen.reload()

    def start(self):
        """
        Démarre la boucle principale de l'application.
        """
        self.root.mainloop()

def resize(event):
    """
    Gère l'événement de redimensionnement de la fenêtre.
    
    Args:
        event (tk.Event): L'événement de redimensionnement.
    """
    print("New size is: {}x{}".format(event.width, event.height))
