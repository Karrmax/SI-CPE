from divers.Vector import Vector, NULLVECTOR

class Element:
    def __init__(self, board, pos:Vector, size:Vector):
        self.board = board
        self.pos = pos ## en (x,y)
        self.size = size ## en (x,y)
        self.sprite = False
        
    def hasSprite(self):
        return self.sprite != False
    
    def update(self):
        pass
    
    def changeState(self, input):
        pass
    
    def hit(self, proj):
        pass
    
    def touched(e1, e2):
        return (e1.pointIn(e2.pos) or e1.pointIn(e2.pos + e2.size) or e1.pointIn(Vector(e2.pos.x + e2.size.x, e2.pos.y)) or e1.pointIn(Vector(e2.pos.x, e2.pos.y + e2.size.y)) or
                e2.pointIn(e1.pos) or e2.pointIn(e1.pos + e1.size) or e2.pointIn(Vector(e1.pos.x + e1.size.x, e1.pos.y)) or e2.pointIn(Vector(e1.pos.x, e1.pos.y + e1.size.y)))
      ### regarde si les deux objets rectangulaires sont l'un dans l'autre (se touchent)
      
    def pointIn(self, point):
        return (point.x >= self.pos.x and point.x <= self.pos.x + self.size.x) and (point.y >= self.pos.y and point.y <= self.pos.y + self.size.y)
        
        
    def outOfBoard(self):
        return ((self.pos.x < 0 or self.pos.x + self.size.x > self.board.width) or
                (self.pos.y < 0 or self.pos.y + self.size.y > self.board.height))
    
    def outOfBoardLarge(self):
        return ((self.pos.x + self.size.x < 0 or self.pos.x - self.size.x > self.board.width) or
            (self.pos.y + self.size.y < 0 or self.pos.y - self.size.y > self.board.height)) 
 