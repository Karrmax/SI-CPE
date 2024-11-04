"""
SPACE INVADERS

"""

class Element:
    def __init__(self, pos, size):
        self.pos = pos ## en (x,y)
        self.size = size ## en (x,y)
        
    def touched(e1, e2):
        return not((e2.pos.x > e1.pos.x + e1.size.x - 1) or (e1.pos.x > e2.pos.x + e2.size.x - 1) and 
                   (e2.pos.y > e1.pos.y + e1.size.y - 1) or (e1.pos.y > e2.pos.y + e2.size.y - 1))
        
        ### regarde si les deux objets rectangulaires sont l'un dans l'autre (se touchent)
        
        
class ship(Element): # herite de ELEMENT pour gerer les collisions simplement
    def __init__(self, hp, position, size, weapon, speed = (0,0), sprite = 0) -> None:
        super.__init__(position, size)
        self.HPMax = hp
        self.HP = hp
        
        self.speed = speed
        self.MAXspeed = (4,4)
        
        self.weapon = weapon
        
        self.sprite = sprite

    def hit(self, projectile):
        self.hp -= projectile.dmg
    
    def shoot(self):
        self.weapon.shoot()

    def move(self):
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        

class weapon:
    def __init__(self, dmg, sprite = 0) -> None:
        self.projectiles = []
        self.dmg = dmg
        self.sprite = sprite

    def shoot(self):
        proj = Projectile()
        self.projectiles.append(proj)

class Projectile(Element):
    def __init__(self, position, size, speed, dmg, sprite = 0) -> None:
        super.__init__(position, size)
        self.speed = speed
        self.dmg = dmg
        self.sprite = sprite




