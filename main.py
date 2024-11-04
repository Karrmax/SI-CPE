"""
SPACE INVADERS

"""
from tkinter import Tk, Label, Button, StringVar, Entry, Frame

class render:
    def __init__(self) -> None:
        """TKinter initialisation"""
        tk = Tk()
        tk.title("SI-CPE")
        tk.geometry('700x500')

        """Frame TOP"""
        FrameTOP = Frame(tk).pack(side='top')

        #Label de titre
        labelHello = Label(FrameTOP, text="Space Invaders the game !", fg='black', font=("Arial",20)).pack(side='top')
        """Frame MIDDLE"""
        FrameMIDDLE = Frame(tk, bd=5).pack()

        """Frame BOTTOM"""
        FrameBOTTOM = Frame(tk).pack(side='bottom')
        #Boutton quit
        buttonQuit = Button(FrameBOTTOM, text="QUIT", fg='red', command=tk.destroy).pack(side='bottom')
        
        """NOTHING AFTER THIS LINE"""
        tk.mainloop()

if __name__ == "__main__":
    render()

