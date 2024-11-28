from game.Elements.Element import Element

class Wall(Element):
    def __init__(self, board, position, size, sprite, HP = 5) -> None:
        super().__init__(board, position, size)
        self.HP = HP
        self.sprite = sprite
        
    def update(self):
        pass
    
    def hit(self, projectile):
        self.HP -= projectile.dmg
        projectile.destroy()
        
        if not self.isAlive():
            self.destroy()
        
    def isAlive(self):
        return self.HP > 0
    
    def destroy(self):
        if self in self.board.walls:
            self.board.walls.remove(self)
        