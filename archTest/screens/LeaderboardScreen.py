import tkinter as tk

class LeaderboardScreen(tk.Frame):
    def __init__(self, root, switch_callback):
        super().__init__(root)
        self.switch_callback = switch_callback

        tk.Label(self, text="Leaderboard Screen", font=("Arial", 24)).pack(pady=20)
        tk.Button(self, text="Back to Lobby", command=lambda: self.switch_callback("lobby")).pack(pady=10)
