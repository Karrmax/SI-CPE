import tkinter as tk
from screens.LobbyScreen import LobbyScreen
from screens.LeaderboardScreen import LeaderboardScreen
from screens.GameScreen import GameScreen
from managers.LoadManager import LoadManager

class MainRoot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter Game")
        # self.root.attributes("-toolwindow", True)
        self.root.state('zoomed')
        # self.root.bind("<Configure>", resize)

    
        self.loadManager = LoadManager()
        self.loadManager.load_resources()

        self.screens = {}
        self.currentScreen = None
        self.init_screens()

    def init_screens(self):
        self.screens["lobby"] = LobbyScreen(self.root, self.switch_screen, self.loadManager)
        self.screens["leaderboard"] = LeaderboardScreen(self.root, self.switch_screen, self.loadManager)
        self.screens["game"] = GameScreen(self.root, self.switch_screen, self.loadManager)

        self.switch_screen("lobby")

    def switch_screen(self, screen_name):
        if self.currentScreen:
            self.currentScreen.pack_forget()
        self.currentScreen = self.screens[screen_name]
        
        self.currentScreen.pack(fill=tk.BOTH, expand=True)
        if isinstance(self.currentScreen, GameScreen):
            self.currentScreen.start_game_loop()
            
        if isinstance(self.currentScreen, LeaderboardScreen):
            self.currentScreen.reload()
    def start(self):
        self.root.mainloop()

def resize(event):
    print("New size is: {}x{}".format(event.width, event.height))
        
        
        
    # def toggle_fullscreen(self, event=None):
    #     self.state = not self.state  # Just toggling the boolean
    #     self.root.attributes("-fullscreen", self.state)
    #     return "break"

    # def end_fullscreen(self, event=None):
    #     self.state = False
    #     self.root.attributes("-fullscreen", False)
    #     return "break"
