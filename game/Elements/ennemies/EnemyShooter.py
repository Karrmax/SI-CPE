"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: EnemyShooter
Description: Cette classe représente un ennemi tireur dans le jeu. Elle hérite de la classe Enemy et gère les sprites, les points de vie et les attaques de l'ennemi tireur.
TODO: Ajouter des comportements spécifiques pour l'ennemi tireur, comme des tirs en rafale ou des mouvements d'esquive.
"""

from game.Elements.Enemy import Enemy
from divers.Vector import NULLVECTOR

class EnemyShooter(Enemy):
    """
    Classe représentant un ennemi tireur.
    
    Attributs:
        board (Board): Le plateau de jeu.
        position (Vector): La position initiale de l'ennemi.
        size (Vector): La taille de l'ennemi.
        weapon (Weapon): L'arme de l'ennemi.
        speed (Vector): La vitesse de l'ennemi.
        shootProbability (float): La probabilité de tir de l'ennemi.
        points (int): Les points attribués pour avoir vaincu l'ennemi.
        sprite (Image): Le sprite de l'ennemi.
    """
    def __init__(self, board, position, size, weapon, speed=NULLVECTOR, shootProbability=0, points=30) -> None:
        """
        Initialise un ennemi tireur avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            position (Vector): La position initiale de l'ennemi.
            size (Vector): La taille de l'ennemi.
            weapon (Weapon): L'arme de l'ennemi.
            speed (Vector, optional): La vitesse de l'ennemi. Par défaut, NULLVECTOR.
            shootProbability (float, optional): La probabilité de tir de l'ennemi. Par défaut, 0.
            points (int, optional): Les points attribués pour avoir vaincu l'ennemi. Par défaut, 30.
        """
        sprite = board.load_manager.enemyRessources['enemy2']
        super().__init__(board, 1, position, size, weapon, sprite, speed, shootProbability, points)