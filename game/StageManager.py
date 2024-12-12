"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: StageManager
Description: Cette classe gère les différents niveaux (stages) du jeu, y compris la génération des ennemis et des boss pour chaque niveau.
TODO: Ajouter des comportements spécifiques pour les niveaux, comme des animations de transition, des effets visuels ou des interactions avancées avec les él��ments du jeu.
Date de création: 2024-20-11
Date de modification: 2024-04-12
"""

from game.Elements.ennemies.EnemyClassic import EnemyClassic
from game.Elements.ennemies.EnemyShooter import EnemyShooter
from game.Elements.ennemies.EnemyBoss import EnemyBoss
from game.Elements.Weapon import Weapon
from divers.Vector import Vector
from game.Elements.wall import Wall

class StageManager:
    """
    Classe représentant le gestionnaire des niveaux.
    
    Attributs:
        board (Board): Le plateau de jeu.
        enemySprites (dict): Dictionnaire des sprites des ennemis.
        numStage (int): Le numéro du niveau actuel.
    """
    def __init__(self, board, enemySprites):
        """
        Initialise le gestionnaire des niveaux avec le plateau de jeu et les sprites des ennemis.
        
        Args:
            board (Board): Le plateau de jeu.
            enemySprites (dict): Dictionnaire des sprites des ennemis.
        """
        self.board = board
        self.enemySprites = enemySprites
        self.numStage = 1

    def generateStage(self):
        """
        Génère le niveau actuel en fonction du numéro de niveau.
        """
        self.removeALLExceptShip()
        matrix = [[None for _ in range(5)] for _ in range(3)]
        if self.numStage == 1:
            matrix = self.generateStage1(matrix)
        elif self.numStage == 2:
            matrix = self.generateStage2(matrix)
        elif self.numStage == 3:
            matrix = self.generateStage3(matrix)
        elif self.numStage == 4:
            matrix = self.generateStage4(matrix)
        else:
            matrix = self.generateClassicStage(matrix)
        if self.numStage != 1:
            self.board.walls.append(Wall(self.board, Vector(600 + 100, self.board.height * 4/5), Vector(150, 42), self.board.load_manager.resources['wall'])) 
        self.board.ennemiesMatrix = matrix

    def generateStage1(self, matrix):
        """
        Génère le premier niveau avec des ennemis classiques et des ennemis tireurs.
        
        Args:
            matrix (list): La matrice des ennemis.
        
        Returns:
            list: La matrice des ennemis mise à jour.
        """
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateStage2(self, matrix):
        """
        Génère le premier niveau avec des ennemis classiques et des ennemis tireurs.
        
        Args:
            matrix (list): La matrice des ennemis.
        
        Returns:
            list: La matrice des ennemis mise à jour.
        """
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateStage3(self, matrix):
        """
        Génère le deuxième niveau avec des ennemis classiques, des ennemis tireurs et un boss.
        
        Args:
            matrix (list): La matrice des ennemis.
        
        Returns:
            list: La matrice des ennemis mise à jour.
        """
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 and j == 2:
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateStage4(self, matrix):
        """
        Génère le troisième niveau avec des ennemis classiques, des ennemis tireurs et un boss.
        
        Args:
            matrix (list): La matrice des ennemis.
        
        Returns:
            list: La matrice des ennemis mise à jour.
        """
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 and j == 2 or i == 0 and j == 3 or i == 0 and j == 1:
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    
    def generateClassicStage(self, matrix):
        """
        Génère un niveau classique avec des ennemis classiques, des ennemis tireurs et un boss.
        
        Args:
            matrix (list): La matrice des ennemis.
        
        Returns:
            list: La matrice des ennemis mise à jour.
        """
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 :
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, self.calculateSpeed(), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.calculateSpeed(), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.calculateSpeed())
                matrix[i][j] = e
        return matrix
                
    def calculateProbability(self):
        """
        Calcule la probabilité de tir des ennemis.
        
        Returns:
            float: La probabilité de tir des ennemis.
        """
        return 0.005 + self.numStage * 0.007
    
    def calculateSpeed(self):
        """
        Calcule la vitesse des ennemis en fonction du niveau actuel.
        
        Returns:
            Vector: La vitesse des ennemis.
        """
        return Vector(self.numStage, 0)
    
    def removeALLExceptShip(self):
        """
        Supprime tous les ennemis et projectiles du plateau, sauf le vaisseau principal.
        """
        self.board.ennemiesMatrix = None
        self.fire = {'ennemie':[], 'mainship':[]}
        
    def manageEnemiesMoves(self):
        """
        Gère les mouvements des ennemis sur le plateau.
        """
        e = self.board.getEnnemiesList()
        for i in e:
            if i.outOfBoard():
                self.reversALLMovement(e)
                self.ALLgoDown(e)
                return
            
    def reversMovement(self, e):
        """
        Inverse la direction du mouvement d'un ennemi.
        
        Args:
            e (Enemy): L'ennemi dont la direction du mouvement doit être inversée.
        """
        e.speed = -e.speed
            
    def reversALLMovement(self, tab):
        """
        Inverse la direction du mouvement de tous les ennemis.
        
        Args:
            tab (list): La liste des ennemis.
        """
        for i in tab:
            self.reversMovement(i)
            
    def goDown(self, e):
        """
        Fait descendre un ennemi d'une ligne.
        
        Args:
            e (Enemy): L'ennemi à faire descendre.
        """
        e.pos.y += e.size.y
        
    def ALLgoDown(self, tab):
        """
        Fait descendre tous les ennemis d'une ligne.
        
        Args:
            tab (list): La liste des ennemis.
        """
        for i in tab:
            self.goDown(i)
            
    def isStageFinished(self):
        """
        Retourne si le niveau est finis ou non
        
        returns:
            bool: True si le niveau est terminé, False sinon.
        """
        return  self.board.getEnnemiesList() == []
    

    def nextStage(self):
        """
        Fait descendre tous les ennemis d'une ligne.

        """
        self.numStage += 1
        self.generateStage()
        
        
    def changeStates(self):
        """
        Passe au niveau suivant si le niveau actuel est terminé.
        

        """
        self.manageEnemiesMoves()
        if self.isStageFinished():
            self.nextStage()
            
    def reset(self):
        """
        Réinitialise le gestionnaire de stage.
        """
        self.numStage = 0
        self.generateStage()