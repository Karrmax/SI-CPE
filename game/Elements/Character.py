"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Character
Description: Cette classe représente un personnage dans le jeu. Elle hérite de la classe Element et gère les déplacements, les points de vie, les armes et les collisions du personnage.
TODO: Ajouter des comportements spécifiques pour le personnage, comme des animations, des compétences spéciales ou des améliorations d'armes.
Date de création: 2024-16-11
Date de modification: 2024-04-12
"""

from game.Elements.Element import Element
from divers.Vector import Vector

class Character(Element):
    """
    Classe représentant un personnage.
    
    Attributs:
        board (Board): Le plateau de jeu.
        HPMax (int): Les points de vie maximum du personnage.
        HP (int): Les points de vie actuels du personnage.
        speed (Vector): La vitesse du personnage.
        MAXspeed (tuple): La vitesse maximale du personnage.
        weapon (Weapon): L'arme du personnage.
        sprite (Image): Le sprite du personnage.
    """
    def __init__(self, board, hp, position, size, weapon, sprite=0, speed=Vector(0, 0)) -> None:
        """
        Initialise un personnage avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            hp (int): Les points de vie du personnage.
            position (Vector): La position initiale du personnage.
            size (Vector): La taille du personnage.
            weapon (Weapon): L'arme du personnage.
            sprite (Image, optional): Le sprite du personnage. Par défaut, 0.
            speed (Vector, optional): La vitesse du personnage. Par défaut, Vector(0, 0).
        """
        super().__init__(board, position, size)
        
        self.HPMax = hp
        self.HP = hp
        
        self.speed = Vector(speed.x, speed.y)
        self.MAXspeed = (4, 4)
        
        self.weapon = weapon
        
        self.sprite = sprite  
    
    def move(self):
        """
        Déplace le personnage en fonction de sa vitesse, en vérifiant les limites du plateau de jeu.
        """
        if not ((self.pos.x + self.speed.x + self.size.x >= self.board.width) or (self.pos.x + self.speed.x <= 0)):
            self.pos.x += self.speed.x
        if not ((self.pos.y + self.speed.y + self.size.y >= self.board.height) or (self.pos.y + self.speed.y <= 0)):
            self.pos.y += self.speed.y 
            
    def hit(self, projectile):
        """
        Gère l'impact d'un projectile sur le personnage.
        
        Args:
            projectile (Projectile): Le projectile qui touche le personnage.
        """
        self.HP -= projectile.dmg
        projectile.destroy()
        
    def shoot(self):
        """
        Fait tirer le personnage avec son arme.
        """
        self.weapon.shoot(self)
            
    def update(self):
        """
        Met à jour l'état du personnage, en déplaçant le personnage.
        """
        self.move()