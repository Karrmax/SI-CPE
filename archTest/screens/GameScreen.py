import tkinter as tk
from game.GameLogic import GameLogic

class GameScreen(tk.Frame):
    def __init__(self, root, switch_callback, load_manager):
        super().__init__(root)
        self.switch_callback = switch_callback
        self.load_manager = load_manager
        
        tk.Button(self, text="Back to Lobby", command=lambda: self.switch_callback("lobby")).pack()
        
        
        self.canvas = tk.Canvas(self, width=800, height=500, bg="black")
        self.canvas.pack()
        
        self.gameLogic = GameLogic(self, load_manager, target_fps = 60)


        self.start_game_loop()

    def start_game_loop(self):
        self.gameLogic.start()
