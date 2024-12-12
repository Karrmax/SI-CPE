"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Ship
Description: Cette classe représente le vaisseau principal dans le jeu. Elle hérite de la classe Character et gère les déplacements, les dégâts et les collisions des projectiles.
TODO: ajouter différentes armes par défaut, des améliorations d'armes et des compétences spéciales pour le vaisseau principal.
Date de création: 2024-16-11
Date de modification: 2024-04-12
"""

from game.Elements.Character import Character
from game.Elements.Element import Element
from divers.Vector import NULLVECTOR

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
        if self.canMoveHorizontaly() and not ((self.pos.x + self.speed.x + self.size.x>= self.board.width - self.size.x/2) or (self.pos.x + self.speed.x <= self.size.x/2)) :    
            self.pos.x += self.speed.x
        if self.canMoveVerticaly() and not ((self.pos.y + self.speed.y + self.size.y >= self.board.height - self.size.y/2) or (self.pos.y + self.speed.y <= self.board.allayZone)) :       
            self.pos.y += self.speed.y  
            
    def isAlive(self):
        return self.HP > 0
    
    def canMoveHorizontaly(self):
        newPos = self.pos + self.speed
        newPos.y -= self.speed.y
        nextShip = Ship(self.board, self.HP, newPos, self.size, self.weapon, self.sprite, self.speed)
        for i in self.board.walls:
            if Element.touched(nextShip, i) and not Element.touched(self, i):
                return False
        return True
    
    def canMoveVerticaly(self):
        newPos = self.pos + self.speed
        newPos.x -= self.speed.x
        # newPos
        nextShip = Ship(self.board, self.HP, newPos, self.size, self.weapon, self.sprite, self.speed)
        for i in self.board.walls:
            if Element.touched(nextShip, i) and not Element.touched(self, i):
                return False
        return True