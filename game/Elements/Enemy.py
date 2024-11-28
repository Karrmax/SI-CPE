"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Enemy
Description: Cette classe représente un ennemi dans le jeu. Elle hérite de la classe Character et gère les points de vie, les attaques et les comportements des ennemis.
TODO: Ajouter des comportements spécifiques pour les ennemis, comme des mouvements aléatoires, des attaques spéciales ou des interactions avec d'autres éléments.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

from game.Elements.Character import Character
from divers.Vector import NULLVECTOR
import random   

class Enemy(Character):
    """
    Classe représentant un ennemi.
    
    Attributs:
        board (Board): Le plateau de jeu.
        points (int): Les points attribués pour avoir vaincu l'ennemi.
        canShoot (bool): Indique si l'ennemi peut tirer.
        shootProbability (float): La probabilité de tir de l'ennemi.
    """
    def __init__(self, board, hp, position, size, weapon, sprite=False, speed=NULLVECTOR, shootProbability=0, points=10) -> None:
        """
        Initialise un ennemi avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            hp (int): Les points de vie de l'ennemi.
            position (Vector): La position initiale de l'ennemi.
            size (Vector): La taille de l'ennemi.
            weapon (Weapon): L'arme de l'ennemi.
            sprite (Image, optional): Le sprite de l'ennemi. Par défaut, False.
            speed (Vector, optional): La vitesse de l'ennemi. Par défaut, NULLVECTOR.
            shootProbability (float, optional): La probabilité de tir de l'ennemi. Par défaut, 0.
            points (int, optional): Les points attribués pour avoir vaincu l'ennemi. Par défaut, 10.
        """
        super().__init__(board, hp, position, size, weapon, sprite, speed)
        self.points = points
        self.canShoot = False
        self.shootProbability = shootProbability
        
    def applyProba(self):
        """
        Retourne True ou False aléatoirement en fonction de la probabilité de tir de l'ennemi.
        
        Returns:
            bool: True si l'ennemi tire, False sinon.
        """
        return random.random() < self.shootProbability
    
    def hit(self, projectile):
        """
        Gère l'impact d'un projectile sur l'ennemi.
        
        Args:
            projectile (Projectile): Le projectile qui touche l'ennemi.
        """
        if projectile.fromMainShip:
            self.HP -= projectile.dmg  
            self.board.points += self.points
            projectile.destroy()
    
    def changeState(self, input):
        """
        Change l'état de l'ennemi en fonction des entrées.
        
        Args:
            input: Les entrées pour changer l'état de l'ennemi.
        """
        pass
    
    def update(self):
        """
        Met à jour l'état de l'ennemi.
        """
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