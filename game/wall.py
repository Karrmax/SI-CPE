from game.ship import Element

class Wall(Element):
    def __init__(self, board, position, size, sprite) -> None:
        super().__init__(board, position, size)
        self.sprite = sprite
        
    def update(self):
        pass