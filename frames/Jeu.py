import tkinter as tk
from tkinter import ttk,Canvas
import time

LARGEFONT = "Verdana"

class Jeu(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Play", font = (LARGEFONT,15))
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        canva = Canvas(self)
        canva.grid(row = 2, column = 1, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Menu",
        command = lambda : controller.show_frame(2))
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="QUIT", 
                             command = lambda : controller.destroy())
        button3.grid(row = 5, column = 2, padx = 10, pady = 10)
        
        self.gameLoop()
        
        
    def updatewindow(self, fps=60):
        time.sleep(1/fps)
        self.update()
        
    def gameLoop(self):
        while True:
            
            self.updatewindow()
        
        
        
        
  