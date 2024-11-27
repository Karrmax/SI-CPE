from game.Elements.Element import Element
from divers.Vector import Vector

class Character(Element): # herite de ELEMENT pour gerer les collisions simplement
    def __init__(self, board, hp, position, size, weapon, sprite = 0, speed = Vector(0,0)) -> None:
        super().__init__(board, position, size)
        
        self.HPMax = hp
        self.HP = hp
        
        self.speed = Vector(speed.x, speed.y)
        self.MAXspeed = (4,4)
        
        self.weapon = weapon
        
        self.sprite = sprite  
        
    def move(self):
        if not ((self.pos.x + self.speed.x + self.size.x>= self.board.width) or (self.pos.x + self.speed.x <= 0)) :    
            self.pos.x += self.speed.x
        if not ((self.pos.y + self.speed.y + self.size.y >= self.board.height) or (self.pos.y + self.speed.y <= 0)) :       
            self.pos.y += self.speed.y 
            
    def hit(self, projectile):
        self.HP -= projectile.dmg
        projectile.destroy()
        
    def shoot(self):
        self.weapon.shoot(self)
            
    def update(self):
        self.move()