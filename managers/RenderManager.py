from tkinter import NW
from PIL import ImageTk
from managers.LoadManager import LoadManager
 
class RenderManager:
    def __init__(self, canvas, background_images):
        self.canvas = canvas
        self.background_image = background_images[1]
        self.background_images = background_images

    def render(self, entities, board, stage):
        
        if stage >= len(self.background_images):
            stage = len(self.background_images) - 1
        self.background_image = self.background_images[stage]
        
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        # délimitation de la zone de jeu
        self.canvas.create_line(0,board.allayZone,board.width,board.allayZone, fill="white", width=1)
        
        for entity in entities:
            if entity.hasSprite():
 
                self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.sprite, anchor="nw")
                
                #################   SHOW HIT BOX   ##############
                # self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + entity.size.x , entity.pos.y + entity.size.y, outline='red')
            else :
                print("has not sprite")
                self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + 20, entity.pos.y + 20, fill="white")
        
    def renderInfos(self, points, stage, HP):
        info_text = f"HP: {HP} \nPoints: {points} \nStage: {stage}"
        self.canvas.create_text(10, 10, text=info_text, anchor="nw", font=("Arial", 16), fill="white")
        
    def __del__(self):
        del self.canvas