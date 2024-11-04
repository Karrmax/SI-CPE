
import tkinter as tk
from tkinter import ttk
from frames.Startpage import StartPage
from frames.Jeu import Jeu
from frames.Menu import Menu

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        allFrames = [StartPage, Jeu, Menu]
        # initializing frames to an empty array
        self.frames = []  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in allFrames:
            frame = F(container, self)
            self.frames.append(frame)
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(0)
  
    # to display the current frame passed as parameter
    def show_frame(self, num):
        frame = self.frames[num]
        frame.tkraise()

# Driver Code
app = tkinterApp()
app.mainloop()
