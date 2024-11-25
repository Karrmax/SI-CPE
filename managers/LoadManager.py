from PIL import Image, ImageTk

class LoadManager:
    def __init__(self):
        self.resources = {}
        self.enemyRessources = {}

    def load_resources(self):
        # loading images, sounds, etc...
        print("Loading resources...")
        self.resources["ship"] = ImageTk.PhotoImage(Image.open("ressources/images/pngegg.png").resize((60, 60)))
        self.resources["fire"] = ImageTk.PhotoImage(Image.open("ressources/images/fire.png").resize((10, 58)))
        self.resources['background'] = ImageTk.PhotoImage(Image.open("ressources/images/background.jpg"))
        self.resources["wall"] = ImageTk.PhotoImage(Image.open("ressources/images/sci-fiwall8bit.png").resize((150, 42)))
        
        self.enemyRessources["enemy1"] = ImageTk.PhotoImage(Image.open("ressources/images/alien1.png").resize((40, 40)))
        self.enemyRessources["enemy2"] = ImageTk.PhotoImage(Image.open("ressources/images/alien2.png").resize((40, 40)))
        self.enemyRessources["enemy3full"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3_FULL.png").resize((40, 40)))
        self.enemyRessources["enemy3mid"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3MID.png").resize((40, 40)))
        self.enemyRessources["enemy3low"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3LOW.png").resize((40, 40)))
        self.enemyRessources["fireDown"] = ImageTk.PhotoImage(Image.open("ressources/images/fireDown.png").resize((10, 58)))
        
        print("Resources loaded.")
        
    def get_resource(self, name):
        return self.resources.get(name, None)
    
    def __del__(self):
        del self.resources
