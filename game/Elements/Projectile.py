from game.Elements.Element import Element

class Projectile(Element):
    def __init__(self, board, position, size, speed, dmg, sprite = False, fromMainShip = False) -> None:
        super().__init__(board, position, size)
        self.speed = speed
        
        self.dmg = dmg
        self.sprite = sprite
        self.fromMainShip = fromMainShip
        
        if self.fromMainShip:
            self.board.fire['ennemy'].append(self)
        else:
            self.board.fire['mainShip'].append(self)
            
        
    def move(self):
        if self.fromMainShip:
            self.pos.y -= self.speed 
        else:
              self.pos.y += self.speed
        
    def update(self):
        if self.board.colided(self):
            elementTouched = self.board.colidedBy(self)
            elementTouched.hit(self)
    
        self.move()
        if self.outOfBoardLarge():
            self.destroy()
    
    def destroy(self):
        self.board.remove(self)