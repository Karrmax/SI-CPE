from game.Elements.Projectile import Projectile
from game.Elements.Ship import Ship
from divers.Vector import Vector
from divers.CoolDown import CoolDown

class Weapon:
    def __init__(self, dmg, sprite, CD = 0.6) -> None:
        # self.board = board
        self.projectiles = []
        self.dmg = dmg
        self.sprite = sprite
        
        self.projSize = Vector(10, 52)
        self.speed = 8
        self.coolDown = CoolDown(CD)

    def shoot(self, ship):
        if self.coolDown.isEnable():
            origin = (ship.pos + ship.size)
            origin.x -= ship.size.x/2 + self.projSize.x / 2
            
            if isinstance(ship, Ship):
                origin.y -= ship.size.y + self.projSize.y +1
            else:
                origin.y -= ship.size.y - self.projSize.y - 1
                # self.speed = -self.speed
            
            proj = Projectile(ship.board, origin, self.projSize, self.speed, self.dmg, self.sprite, isinstance(ship, Ship))
            self.projectiles.append(proj)
            self.coolDown.set()
            # return proj
        return False