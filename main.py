
import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT = "Verdana"
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
  
        allFrames = [StartPage, Jeu, Menu]
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in allFrames:
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Welcome to", font = (LARGEFONT,15))
        label = ttk.Label(self, text ="SPACE INVADERS the Game !", font = (LARGEFONT,25))
        label.grid(row = 1, column = 1, padx = 10, pady = 10) 
  
        button1 = ttk.Button(self, text ="Play",
        command = lambda : controller.show_frame(Jeu))
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="Menu",
        command = lambda : controller.show_frame(Menu))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="QUIT", 
                             command = lambda : controller.destroy)
        button3.grid(row = 5, column = 2, padx = 10, pady = 10)
  
          
  
class Jeu(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Play", font = (LARGEFONT,15))
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text ="Menu",
        command = lambda : controller.show_frame(Menu))
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="QUIT", 
                             command = lambda : controller.destroy)
        button3.grid(row = 5, column = 2, padx = 10, pady = 10)
  
class Menu(tk.Frame): 
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Menu", font = (LARGEFONT,15))
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text ="Play",
        command = lambda : controller.show_frame(Jeu))
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="QUIT", 
                             command = lambda : controller.destroy)
        button3.grid(row = 5, column = 2, padx = 10, pady = 10)

# Driver Code
app = tkinterApp()
app.mainloop()
