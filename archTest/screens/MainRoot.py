import tkinter as tk
from screens.LobbyScreen import LobbyScreen
from screens.LeaderboardScreen import LeaderboardScreen
from screens.GameScreen import GameScreen
from managers.LoadManager import LoadManager

class MainRoot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter Game")
        self.root.geometry("800x600")

        self.loadManager = LoadManager()
        self.loadManager.load_resources()

        self.screens = {}
        self.currentScreen = None

        self.init_screens()

    def init_screens(self):
        self.screens["lobby"] = LobbyScreen(self.root, self.switch_screen)
        self.screens["leaderboard"] = LeaderboardScreen(self.root, self.switch_screen)
        self.screens["game"] = GameScreen(self.root, self.switch_screen, self.loadManager)

        self.switch_screen("lobby")

    def switch_screen(self, screen_name):
        if self.currentScreen:
            self.currentScreen.pack_forget()
        self.currentScreen = self.screens[screen_name]
        self.currentScreen.pack(fill=tk.BOTH, expand=True)

    def start(self):
        self.root.mainloop()
