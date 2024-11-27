from game.Elements.Character import Character
from divers.Vector import NULLVECTOR
import random   

class Enemy(Character):
    def __init__(self, board, hp, position, size, weapon, sprite = False, speed = NULLVECTOR, shootProbability = 0, points = 10) -> None:
        super().__init__(board,hp, position, size, weapon, sprite, speed)
        self.points = points
        self.canShoot = False
        self.shootProbability = shootProbability
        
        
    # function that return true or false randomly by a probability self.probability    
    def applyProba(self):
        return random.random() < self.shootProbability
    
    def hit(self, projectile):
        if projectile.fromMainShip:
            self.HP -= projectile.dmg  
            # print('from main ship')
            self.board.points += self.points
            projectile.destroy()
    
    def changeState(self, input):
        pass
    
    def update(self):
        if self.HP <= 0:
            self.destroy()
        else:     
            self.move()
            if self.canShoot and self.applyProba():
                self.shoot()
            
    def move(self):
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y 
        
    def destroy(self):
        self.board.remove(self)