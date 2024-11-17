from game.ship import Element

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []
        self.col = []
        
    def remove(self, entity):
        self.entities.remove(entity)
        
    def newEntity(self, entity):
        self.entities.append(entity)
        
    def manageCollisions(self):
        col = []
        for i in range(len(self.entities) -1):
            for j in range(i + 1, len(self.entities)):
                if Element.touched(self.entities[i],  self.entities[j]):
                    col.append([self.entities[i],  self.entities[j]])
        self.col = col
        
    def colided(self, element):
        for i in self.col:
            if element in i:
                return True
            
    def colidedBy(self, element):
        for i in self.col:
            if element in i:
                return i[((i.index(element))-1)**2]
                
            
    