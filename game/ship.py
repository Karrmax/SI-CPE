"""
SPACE INVADERS

"""
from divers.Vector import Vector, NULLVECTOR
import time
import random

class Element:
    def __init__(self, board, pos:Vector, size:Vector):
        self.board = board
        self.pos = pos ## en (x,y)
        self.size = size ## en (x,y)
        self.sprite = False
        
    def hasSprite(self):
        return self.sprite != False
    
    def update(self):
        pass
    
    def changeState(self, input):
        pass
    
    def hit(self, proj):
        pass
    
    def touched(e1, e2):
        return (e1.pointIn(e2.pos) or e1.pointIn(e2.pos + e2.size) or e1.pointIn(Vector(e2.pos.x + e2.size.x, e2.pos.y)) or e1.pointIn(Vector(e2.pos.x, e2.pos.y + e2.size.y)) or
                e2.pointIn(e1.pos) or e2.pointIn(e1.pos + e1.size) or e2.pointIn(Vector(e1.pos.x + e1.size.x, e1.pos.y)) or e2.pointIn(Vector(e1.pos.x, e1.pos.y + e1.size.y)))
      ### regarde si les deux objets rectangulaires sont l'un dans l'autre (se touchent)
      
    def pointIn(self, point):
        return (point.x >= self.pos.x and point.x <= self.pos.x + self.size.x) and (point.y >= self.pos.y and point.y <= self.pos.y + self.size.y)
        
        
    def outOfBoard(self):
        return ((self.pos.x < 0 or self.pos.x + self.size.x > self.board.width) or
                (self.pos.y < 0 or self.pos.y + self.size.y > self.board.height))
    
    def outOfBoardLarge(self):
        return ((self.pos.x + self.size.x < 0 or self.pos.x - self.size.x > self.board.width) or
            (self.pos.y + self.size.y < 0 or self.pos.y - self.size.y > self.board.height)) 
    
        

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
        s = self.weapon.shoot(self)
            
    def update(self):
        self.move()
        
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
        
        
class Ship(Character): 
    def __init__(self, board, hp, position, size, weapon, sprite = False, speed = NULLVECTOR) -> None:
        super().__init__(board,hp, position, size, weapon, sprite, speed)
        
        
    def changeState(self, input):
        self.speed.x = 0
        self.speed.y = 0
        
        if ('d' in input) or ('D' in input) or ('Right' in input):
            self.speed.x += self.MAXspeed[0]
            
        if ('q' in input) or ('Q' in input) or ('Left' in input):
            self.speed.x -= self.MAXspeed[0]
            
        if ('z' in input) or ('Z' in input) or ('Up' in input):
            self.speed.y -= self.MAXspeed[1]
            
        if ('s' in input) or ('S' in input) or ('Down' in input):
            self.speed.y += self.MAXspeed[1]
            
            
        if 'space' in input:
            self.shoot()
            
    def move(self):
        if not ((self.pos.x + self.speed.x + self.size.x>= self.board.width - 15) or (self.pos.x + self.speed.x <= 15)) :    
            self.pos.x += self.speed.x
        if not ((self.pos.y + self.speed.y + self.size.y >= self.board.height - 15) or (self.pos.y + self.speed.y <= self.board.allayZone)) :       
            self.pos.y += self.speed.y  
            
    def isAlive(self):
        return self.HP > 0
        
        
        

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
        
        
class CoolDown():
    def __init__(self, CD):
        self.CD = CD
        self.lastTime = time.time()
        
        ## will time and enable the action only when lastTime = time 
        
    def isEnable(self):
        return (time.time() - self.lastTime) >= self.CD
    
    def set(self):
        self.lastTime = time.time()
        
    def reset(self):
        self.lastTime = time.time(0)
        