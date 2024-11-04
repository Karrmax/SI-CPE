"""
SPACE INVADERS

"""


class ship:
    def __init__(self, hp:int, position, size,weapon, speed = (0,0), sprite = 0) -> None:
        """_summary_

        Args:
            hp (int): _description_
            position (_type_): _description_
            size (_type_): _description_
            weapon (_type_): _description_
            speed (tuple, optional): _description_. Defaults to (0,0).
            sprite (int, optional): _description_. Defaults to 0.
        """
class ship:
    def __init__(self, hp, position, size,weapon, speed = (0,0), sprite = 0) -> None:
        self.HPMax = hp
        self.HP = hp
        self.speed = speed
        self.MAXspeed = (4,4)
        self.pos = position
        self.size = size
        self.sprite = sprite
        self.weapon = weapon

    def hit(self, projectile):
        self.hp -= projectile.dmg
    
    def shoot(self):
        self.weapon.shoot()

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        

class weapon:
    def __init__(self, dmg, sprite = 0) -> None:
        self.projectile = []
        self.dmg = dmg
        self.sprite = sprite

    def shoot(self):
        proj = Projectile((0, 0), (0, 0), 15)
        self.projectile.append(proj)

class Projectile:
    def __init__(self, position, speed, dmg, sprite = 0) -> None:
        self.pos = position
        self.speed = speed
        self.dmg = dmg
        self.sprite = sprite




