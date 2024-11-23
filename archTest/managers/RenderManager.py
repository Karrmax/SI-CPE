from tkinter import NW
from PIL import ImageTk
 
class RenderManager:
    def __init__(self, canvas):
        self.canvas = canvas

    def render(self, entities):
        self.canvas.delete("all")
        for entity in entities:
            if entity.hasSprite():
                # self.canvas.images = []
                # Resize and render the sprite
                # resized_sprite = entity.sprite.resize((entity.size.x, entity.size.y))
                # tk_sprite = ImageTk.PhotoImage(resized_sprite)
                self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.sprite, anchor="nw")
                
                # Prevent garbage collection
                # self.canvas.images.append(tk_sprite)
                
                
                #################   SHOW HIT BOX   ##############
                self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + entity.size.x , entity.pos.y + entity.size.y, outline='red')
                

            else :
                print("has not sprite")
                self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + 20, entity.pos.y + 20, fill="white")

    def __del__(self):
        del self.canvas