import tkinter as tk
from tkinter import ttk
  
LARGEFONT = "Verdana"

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Welcome to", font = (LARGEFONT,15))
        label = ttk.Label(self, text ="SPACE INVADERS the Game !", font = (LARGEFONT,25))
        label.grid(row = 1, column = 1, padx = 10, pady = 10) 
  
        button1 = ttk.Button(self, text ="Play",
        command = lambda : controller.show_frame(1))
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="Menu",
        command = lambda : controller.show_frame(2))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="QUIT", 
                             command = lambda : controller.destroy())
        button3.grid(row = 5, column = 2, padx = 10, pady = 10) 