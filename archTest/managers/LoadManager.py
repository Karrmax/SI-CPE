from PIL import Image, ImageTk

class LoadManager:
    def __init__(self):
        self.resources = {}

    def load_resources(self):
        # Simulate loading images, sounds, etc.
        print("Loading resources...")
        self.resources["ship"] = ImageTk.PhotoImage(Image.open("ressources/images/pngegg.png").resize((60, 60)))
        self.resources["fire"] = ImageTk.PhotoImage(Image.open("ressources/images/fire.png").resize((10, 58)))
        self.resources["enemy"] = ImageTk.PhotoImage(Image.open("ressources/images/enemy.png").resize((40, 40)))

    def get_resource(self, name):
        return self.resources.get(name, None)
