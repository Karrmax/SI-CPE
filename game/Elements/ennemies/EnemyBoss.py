"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: EnemyBoss
Description: Cette classe représente un boss ennemi dans le jeu. Elle hérite de la classe Enemy et gère les sprites, les points de vie et les attaques du boss.
TODO: Ajouter des comportements spécifiques pour le boss, comme des attaques spéciales ou des mouvements complexes.
"""

from game.Elements.Enemy import Enemy
from divers.Vector import NULLVECTOR

class EnemyBoss(Enemy):
    """
    Classe représentant un boss ennemi.
    
    Attributs:
        board (Board): Le plateau de jeu.
        position (Vector): La position initiale du boss.
        size (Vector): La taille du boss.
        weapon (Weapon): L'arme du boss.
        speed (Vector): La vitesse du boss.
        shootProbability (float): La probabilité de tir du boss.
        points (int): Les points attribués pour avoir vaincu le boss.
        sprites (list): Liste des sprites du boss.
        curSprite (int): Index du sprite actuel.
    """
    def __init__(self, board, position, size, weapon, speed=NULLVECTOR, shootProbability=0, points=60) -> None:
        """
        Initialise un boss ennemi avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            position (Vector): La position initiale du boss.
            size (Vector): La taille du boss.
            weapon (Weapon): L'arme du boss.
            speed (Vector, optional): La vitesse du boss. Par défaut, NULLVECTOR.
            shootProbability (float, optional): La probabilité de tir du boss. Par défaut, 0.
            points (int, optional): Les points attribués pour avoir vaincu le boss. Par défaut, 60.
        """
        sprites = [board.load_manager.enemyRessources['enemy3full'], board.load_manager.enemyRessources['enemy3mid'], board.load_manager.enemyRessources['enemy3low']]
        super().__init__(board, 3, position, size, weapon, sprites[0], speed, shootProbability, points)
        self.sprites = sprites
        self.curSprite = 0
        
    def hit(self, projectile):
        """
        Gère l'impact d'un projectile sur le boss.
        
        Args:
            projectile (Projectile): Le projectile qui touche le boss.
        """
        if projectile.fromMainShip:
            self.HP -= projectile.dmg
            self.nextSprite()
            if self.HP <= 0:
                self.board.points += self.points
            projectile.destroy() 
    
    def nextSprite(self):
        """
        Passe au sprite suivant du boss. Détruit le boss si tous les sprites ont été utilisés.
        """
        self.curSprite += 1
        if self.curSprite >= len(self.sprites):
            self.destroy()
        else:
            self.sprite = self.sprites[self.curSprite]