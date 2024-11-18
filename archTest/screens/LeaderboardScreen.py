import tkinter as tk
from managers.scoreManager import ScoreManager

class LeaderboardScreen(tk.Frame):
    def __init__(self, root, switch_callback):
        super().__init__(root)
        self.switch_callback = switch_callback

        data = ScoreManager.get_score()
        sorted_list = sorted(data, key=lambda d:(list(d.values())[1], list(d.values())[2]))[::-1]
        keyless_list = [list(d.values()) for d in sorted_list]
        print_list = keyless_list[0:5]       #Max 5 profiles
 
        tk.Label(self, text="Leaderboard top 5 players", font=("Arial", 24)).pack(pady=20)
        
        table = tk.Frame(self)
        table.grid(row=0, column=0, padx=10, pady=10)
        table.grid_columnconfigure(0, weight=1)
        
        labeluser = tk.Label(frame, text="Username")
        labeluser.grid(row=0, column=0, padx=5)

        labelscore = tk.Label(frame, text="Score")
        labelscore.grid(row=0, column=1, padx=5)

        labelstage = tk.Label(frame, text="Stage")
        labelstage.grid(row=0, column=2, padx=5)
        
        """
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        """

        for i,val in enumerate(print_list):
            val = tk.Label(frame, text=val, font=("Arial", 12)).pack(side=tk.BOTTOM, pady=20)
            
        
        tk.Button(self, text="Back to Lobby", command=lambda: self.switch_callback("lobby")).pack(pady=10)
