import tkinter as tk

class LobbyScreen(tk.Frame):
    def __init__(self, root, switch_callback):
        super().__init__(root)
        self.switch_callback = switch_callback

        tk.Label(self, text="Lobby Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Start Game", command=lambda: self.switch_callback("game")).pack(pady=10)
        tk.Button(self, text="Leaderboard", command=lambda: self.switch_callback("leaderboard")).pack(pady=10)
