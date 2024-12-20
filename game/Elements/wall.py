"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Ship
Description: Cette classe représente un mur dans le jeu. Elle hérite de la classe Element et gère les dégâts et les collisions des projectiles.
TODO: Ajouter des comportements spécifiques pour les murs, comme des animations, des interactions avec d'autres éléments ou des effets visuels.
Date de création: 2024-16-11
Date de modification: 2024-04-12
"""

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
        