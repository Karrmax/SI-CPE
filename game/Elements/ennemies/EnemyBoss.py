from game.Elements.Enemy import Enemy
from divers.Vector import NULLVECTOR

class EnemyBoss(Enemy):
    def __init__(self, board, position, size, weapon, speed = NULLVECTOR, shootProbability = 0, points = 60) -> None:
        
        sprites = [ board.load_manager.enemyRessources['enemy3full'], board.load_manager.enemyRessources['enemy3mid'], board.load_manager.enemyRessources['enemy3low']]
        super().__init__(board,3, position, size, weapon, sprites[0], speed, shootProbability, points)
        self.sprites = sprites
        self.curSprite = 0
        
    def hit(self, projectile):
        if projectile.fromMainShip:
            self.HP -= projectile.dmg
            self.nextSprite()
            if self.HP <= 0:
                self.board.points += self.points
            projectile.destroy() 
    
    def nextSprite(self):
        self.curSprite += 1
        if self.curSprite >= len(self.sprites):
            self.destroy()
        else:
            self.sprite = self.sprites[self.curSprite]