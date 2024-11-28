"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Projectile
Description: Cette classe représente un projectile dans le jeu. Elle hérite de la classe Element et gère les déplacements, les dégâts et les collisions des projectiles.
TODO: Ajouter des comportements spécifiques pour les projectiles, comme des effets visuels, des types de projectiles différents ou des interactions spéciales avec d'autres éléments.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

from game.Elements.Element import Element

class Projectile(Element):
    """
    Classe représentant un projectile.
    
    Attributs:
        board (Board): Le plateau de jeu.
        speed (int): La vitesse du projectile.
        dmg (int): Les dégâts infligés par le projectile.
        sprite (Image): Le sprite du projectile.
        fromMainShip (bool): Indique si le projectile provient du vaisseau principal.
    """
    def __init__(self, board, position, size, speed, dmg, sprite=False, fromMainShip=False) -> None:
        """
        Initialise un projectile avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            position (Vector): La position initiale du projectile.
            size (Vector): La taille du projectile.
            speed (int): La vitesse du projectile.
            dmg (int): Les dégâts infligés par le projectile.
            sprite (Image, optional): Le sprite du projectile. Par défaut, False.
            fromMainShip (bool, optional): Indique si le projectile provient du vaisseau principal. Par défaut, False.
        """
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
        """
        Déplace le projectile en fonction de sa vitesse et de son origine.
        """
        if self.fromMainShip:
            self.pos.y -= self.speed 
        else:
            self.pos.y += self.speed
        
    def update(self):
        """
        Met à jour l'état du projectile, en vérifiant les collisions et en déplaçant le projectile.
        """
        if self.board.colided(self):
            elementTouched = self.board.colidedBy(self)
            elementTouched.hit(self)
    
        self.move()
        if self.outOfBoardLarge():
            self.destroy()
    
    def destroy(self):
        """
        Détruit le projectile en le retirant du plateau de jeu.
        """
        self.board.remove(self)