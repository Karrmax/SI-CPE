"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Board
Description: Cette classe représente le plateau de jeu. Elle gère les dimensions du plateau, les ennemis, le vaisseau principal, les projectiles, les murs et les collisions.
TODO: Ajouter des comportements spécifiques pour le plateau de jeu, comme des niveaux différents, des obstacles dynamiques ou des effets visuels.
Date de création: 2024-20-11
Date de modification: 2024-04-12
"""

from game.Elements.Enemy import Enemy
from game.Elements.Element import Element
from game.Elements.Projectile import Projectile

class Board:
    """
    Classe représentant le plateau de jeu.
    
    Attributs:
        width (int): La largeur du plateau de jeu.
        height (int): La hauteur du plateau de jeu.
        ennemiesMatrix (list): La matrice des ennemis sur le plateau.
        mainShip (Element): Le vaisseau principal.
        fire (dict): Les projectiles tirés par les ennemis et le vaisseau principal.
        walls (list): Les murs sur le plateau.
        col (list): Les colonnes sur le plateau.
        load_manager (LoadManager): Le gestionnaire de chargement des ressources.
        points (int): Les points du joueur.
        allayZone (int): La zone d'allée sur le plateau.
    """
    def __init__(self, width, height, loadManager):
        """
        Initialise un plateau de jeu avec les dimensions données et le gestionnaire de chargement.
        
        Args:
            width (int): La largeur du plateau de jeu.
            height (int): La hauteur du plateau de jeu.
            loadManager (LoadManager): Le gestionnaire de chargement des ressources.
        """
        self.width = width
        self.height = height
        
        self.ennemiesMatrix = None
        self.mainShip = None
        self.fire = {'ennemy':[], 'mainShip':[]}
        self.walls = []
        
        self.col = []
        self.load_manager = loadManager
        self.points = 0
        
        self.allayZone = height - 175
    
    def isInAllayZone(self, element):
        """
        Vérifie si un élément est dans la zone d'allée.
        
        Args:
            element (Element): L'élément à vérifier.
        
        Returns:
            bool: True si l'élément est dans la zone d'allée, False sinon.
        """
        return element.pos.y > self.allayZone
    
    def getEntities(self):
        """
        Retourne la liste de toutes les entités sur le plateau.
        
        Returns:
            list: La liste de toutes les entités sur le plateau.
        """
        return self.getEnnemiesList() + self.fire['ennemy'] + self.fire['mainShip'] + [self.mainShip] + self.walls
    
    def getEnnemiesList(self):
        """
        Retourne la liste de tous les ennemis sur le plateau.
        
        Returns:
            list: La liste de tous les ennemis sur le plateau.
        """
        return [j for sub in self.ennemiesMatrix for j in sub]
    
    def remove(self, entity):
        """
        Supprime une entité du plateau.
        
        Args:
            entity (Element): L'entité à supprimer.
        """
        if isinstance(entity, Enemy):
            for i in self.ennemiesMatrix:
                for j in i:
                    if j == entity:
                        i.remove(j)
                        self.setAllShooterEnnemies()
                    
        if isinstance(entity, Projectile):
            if entity.fromMainShip:
                self.fire['ennemy'].remove(entity)
            else:
                self.fire['mainShip'].remove(entity)
        
    def manageCollisions(self):
        """
        Gère les collisions entre les entités sur le plateau.
        """
        col = []
        entities = self.getEntities()
        for i in range(len(entities) -1):
            for j in range(i + 1, len(entities)):
                if Element.touched(entities[i], entities[j]):
                    col.append([entities[i], entities[j]])
        self.col = col
        
    def colided(self, element):
        """
        Vérifie si un élément est en collision avec un autre élément.
        
        Args:
            element (Element): L'élément à vérifier.
        
        Returns:
            bool: True si l'élément est en collision, False sinon.
        """
        for i in self.col:
            if element in i:
                return True
            
    def colidedBy(self, element):
        """
        Retourne l'élément avec lequel l'élément donné est en collision.
        
        Args:
            element (Element): L'élément à vérifier.
        
        Returns:
            Element: L'élément avec lequel l'élément donné est en collision.
        """
        for i in self.col:
            if element in i:
                return i[((i.index(element))-1)**2]
            
    def reset(self):
        """
        Réinitialise le plateau de jeu.
        """
        self.ennemiesMatrix = None
        self.mainShip = None
        self.fire = {'ennemy':[], 'mainShip':[]}
        self.col = []
        
    def getAllLastsEnnemiesByColumn(self): 
        """
        Retourne les derniers ennemis de chaque colonne.
        """    
        matCol = self.matRowToMatColumn(self.ennemiesMatrix)
        for i in matCol:
            yield i[-1]
  
        
    def matRowToMatColumn(self, list_of_lists):
        """
        Transforms a list of lists into columns. Handles uneven row lengths.

        Args:
            list_of_lists: A 2D list where rows may have varying lengths.
        
        returns: 
            A list of lists representing columns.
        """
        columns = []
        max_length = max(len(row) for row in list_of_lists)  # Find the longest row
        for col_index in range(max_length):
            column = []
            for row in list_of_lists:
                if col_index < len(row):  # Check if the column exists in this row
                    column.append(row[col_index])
            columns.append(column)
        return columns
       
    def setAllShooterEnnemies(self): 
        for i in self.getAllLastsEnnemiesByColumn():
            i.canShoot = True
            
    def isGameFinished(self):
        """
        Vérifie si le jeu est terminé.
        
        Returns:
            bool: True si le jeu est terminé, False sinon.
        """
        return self.aliensTooDown() or not self.mainShip.isAlive()
        
    def aliensTooDown(self):
        """
        Vérifie si les aliens sont trop bas sur le plateau.
        
        Returns:
            bool: True si les aliens sont trop bas, False sinon.
        """
        return self.getDownestPointAliens().y > self.allayZone
    
    def getDownestAliens(self):
        """
        Retourne l'alien le plus bas sur le plateau.
        
        Returns:
            Enemy: L'alien le plus bas sur le plateau.
        """
        matCol = self.matRowToMatColumn(self.ennemiesMatrix)
        lengthMax = max([len(matCol[i]) for i in range(len(matCol))])
        
        for i in matCol:
            if len(i) == lengthMax:
                return i[-1]
            
    def getDownestPointAliens(self):
        """
        Retourne le point le plus bas de l'alien le plus bas sur le plateau.
        
        Returns:
            Vector: Le point le plus bas de l'alien le plus bas.
        """
        alien = self.getDownestAliens()
        return alien.pos + alien.size
    
    def noEnemies(self):
        """
        Vérifie s'il n'y a plus d'ennemis sur le plateau.
        
        Returns:
            bool: True s'il n'y a plus d'ennemis, False sinon.
        """
        for i in self.ennemiesMatrix:
            for j in i:
                if isinstance(j, Enemy):
                    return False
                
        return True