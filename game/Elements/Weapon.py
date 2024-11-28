"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Weapon
Description: Cette classe représente une arme dans le jeu. Elle gère les projectiles, les dégâts, le sprite et le cooldown de l'arme.
TODO: Ajouter des comportements spécifiques pour les armes, comme des types de projectiles différents, des améliorations d'armes ou des effets visuels.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

from game.Elements.Projectile import Projectile
from game.Elements.Ship import Ship
from divers.Vector import Vector
from divers.CoolDown import CoolDown

class Weapon:
    """
    Classe représentant une arme.
    
    Attributs:
        dmg (int): Les dégâts infligés par l'arme.
        sprite (Image): Le sprite de l'arme.
        projSize (Vector): La taille des projectiles de l'arme.
        speed (int): La vitesse des projectiles de l'arme.
        coolDown (CoolDown): Le cooldown de l'arme.
        projectiles (list): Liste des projectiles tirés par l'arme.
    """
    def __init__(self, dmg, sprite, CD=0.6) -> None:
        """
        Initialise une arme avec les paramètres donnés.
        
        Args:
            dmg (int): Les dégâts infligés par l'arme.
            sprite (Image): Le sprite de l'arme.
            CD (float, optional): Le cooldown de l'arme. Par défaut, 0.6.
        """
        self.projectiles = []
        self.dmg = dmg
        self.sprite = sprite
        
        self.projSize = Vector(10, 52)
        self.speed = 8
        self.coolDown = CoolDown(CD)

    def shoot(self, ship):
        """
        Fait tirer l'arme depuis le vaisseau donné.
        
        Args:
            ship (Ship): Le vaisseau depuis lequel l'arme tire.
        
        Returns:
            bool: True si le tir est réussi, False sinon.
        """
        if self.coolDown.isEnable():
            origin = (ship.pos + ship.size)
            origin.x -= ship.size.x / 2 + self.projSize.x / 2
            
            if isinstance(ship, Ship):
                origin.y -= ship.size.y + self.projSize.y + 1
            else:
                origin.y -= ship.size.y - self.projSize.y - 1
            
            proj = Projectile(ship.board, origin, self.projSize, self.speed, self.dmg, self.sprite, isinstance(ship, Ship))
            self.projectiles.append(proj)
            self.coolDown.set()
            return True
        return False