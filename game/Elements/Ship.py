from game.Elements.Character import Character
from divers.Vector import NULLVECTOR

class Ship(Character): 
    def __init__(self, board, hp, position, size, weapon, sprite = False, speed = NULLVECTOR) -> None:
        super().__init__(board,hp, position, size, weapon, sprite, speed)
        
        
    def changeState(self, input):
        self.speed.x = 0
        self.speed.y = 0
        
        if ('d' in input) or ('D' in input) or ('Right' in input):
            self.speed.x += self.MAXspeed[0]
            
        if ('q' in input) or ('Q' in input) or ('Left' in input):
            self.speed.x -= self.MAXspeed[0]
            
        if ('z' in input) or ('Z' in input) or ('Up' in input):
            self.speed.y -= self.MAXspeed[1]
            
        if ('s' in input) or ('S' in input) or ('Down' in input):
            self.speed.y += self.MAXspeed[1]
            
            
        if 'space' in input:
            self.shoot()
            
    def move(self):
        if self.canMoveHorizontaly() and not ((self.pos.x + self.speed.x + self.size.x>= self.board.width - 15) or (self.pos.x + self.speed.x <= 15)) :    
            self.pos.x += self.speed.x
        if self.canMoveVerticaly() and not ((self.pos.y + self.speed.y + self.size.y >= self.board.height - 15) or (self.pos.y + self.speed.y <= self.board.allayZone)) :       
            self.pos.y += self.speed.y  
            
    def isAlive(self):
        return self.HP > 0
    
    def canMoveHorizontaly(self):
        newPos = self.pos + self.speed
        newPos.y -= self.speed.y
        nextShip = Ship(self.board, self.HP, newPos, self.size, self.weapon, self.sprite, self.speed)
        for i in self.board.walls:
            if nextShip.touched(i):
                return False
        return True
    
    def canMoveVerticaly(self):
        newPos = self.pos + self.speed
        newPos.x -= self.speed.x
        # newPos
        nextShip = Ship(self.board, self.HP, newPos, self.size, self.weapon, self.sprite, self.speed)
        for i in self.board.walls:
            if nextShip.touched(i):
                return False
        return True