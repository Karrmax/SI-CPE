"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: GameLogic
Description: Cette classe gère la logique du jeu, y compris les entrées utilisateur, le rendu, les mises à jour du jeu et la gestion des niveaux.
TODO: Ajouter des comportements spécifiques pour la logique du jeu, comme des animations de fin de niveau, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 2024-16-11
Date de modification: 2024-04-12
"""

from managers.InputManager import InputManager
from managers.RenderManager import RenderManager
from game.Elements.Ship import Ship
from game.Elements.wall import Wall
from divers.Vector import Vector
from game.Board import Board
from game.StageManager import StageManager as Stage
from game.Elements.Weapon import Weapon
import time

## TODO : 
## BUG la partie continue apres la fin du jeu

class GameLogic:
    """
    Classe représentant la logique du jeu.
    
    Attributs:
        canvas (tk.Canvas): Le canvas pour le rendu du jeu.
        callback_endSequence (function): Fonction de rappel pour la fin de la séquence de jeu.
        load_manager (LoadManager): Le gestionnaire de chargement des ressources.
        inputManager (InputManager): Le gestionnaire des entrées utilisateur.
        renderManager (RenderManager): Le gestionnaire du rendu.
        board (Board): Le plateau de jeu.
        stage_manager (StageManager): Le gestionnaire des niveaux.
        running (bool): Indique si le jeu est en cours d'exécution.
        points (int): Les points du joueur.
        target_fps (int): Le nombre d'images par seconde cible.
    """
    def __init__(self, screen, load_manager, callback_endSequence, target_fps=60):
        """
        Initialise la logique du jeu avec les paramètres donnés.
        
        Args:
            screen (tk.Frame): L'écran de jeu.
            load_manager (LoadManager): Le gestionnaire de chargement des ressources.
            callback_endSequence (function): Fonction de rappel pour la fin de la séquence de jeu.
            target_fps (int, optional): Le nombre d'images par seconde cible. Par défaut, 60.
        """
        self.canvas = screen.canvas
        self.callback_endSequence = callback_endSequence
        self.load_manager = load_manager
        self.inputManager = InputManager()
        
        load_manager.resizeAllBackgrounds(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())
        bgs = self.load_manager.getBackgrounds()
        
        self.renderManager = RenderManager(self.canvas, bgs)
        
        self.board = Board(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), self.load_manager)
        
        self.stage_manager = Stage(self.board, self.load_manager.enemyRessources)
        self.running = False

        self.points = 0
        
        self.target_fps = target_fps

        self.frame_time = 1 / self.target_fps

        # Bind input events
        self.bindAll(screen)
        screen.focus_set()
        
    def bindAll(self, screen):
        """
        Lie les événements d'entrée utilisateur au gestionnaire d'entrées.
        
        Args:
            screen (tk.Frame): L'écran de jeu.
        """
        screen.bind("<KeyPress>", self.inputManager.key_pressed)
        screen.bind("<KeyRelease>", self.inputManager.key_released)
    
    def start(self):
        """
        Démarre la boucle de jeu.
        """
        self.running = True
        
        # Ajout du vaisseau principal
        self.loadShip()
        self.loadWals()
        self.stage_manager.generateStage()
        self.game_loop()
        
    def stop(self):
        """
        Arrête la boucle de jeu.
        """
        self.running = False

    def game_loop(self):
        """
        Boucle principale du jeu.
        """
        start_time = time.time()

        if self.running:
            self.changeState()
            self.update()
            self.render()
            
            if not self.board.noEnemies() and self.board.isGameFinished():
                self.endSequence()

        elapsed_time = time.time() - start_time
        sleep_time = max(0, self.frame_time - elapsed_time)

        self.canvas.after(int(sleep_time * 1000), self.game_loop)

    def changeState(self):
        """
        Change l'état du jeu en fonction des entrées utilisateur.
        """
        inputs = self.inputManager.get_inputs()
        self.stage_manager.changeStates()
        for entity in self.board.getEntities():
            entity.changeState(inputs)
            
    def update(self):
        """
        Met à jour la logique du jeu.
        """
        self.board.manageCollisions()
        for entity in self.board.getEntities():
            entity.update()

    def render(self):
        """
        Rend l'état actuel du jeu.
        """
        self.renderManager.render(self.board.getEntities(), self.board, self.stage_manager.numStage)
        self.renderManager.renderInfos(self.board.points, self.stage_manager.numStage, self.board.mainShip.HP)
        
    def loadWals(self):
        """
        Charge les murs du jeu.
        """
        wallSprite = self.load_manager.get_resource('wall')
        for i in range(3):
            self.board.walls.append(Wall(self.board, Vector(i*self.canvas.winfo_reqwidth()/3 + self.canvas.winfo_reqwidth()/8, self.board.height * 4/5), Vector(150, 42), wallSprite))  
    
    def loadShip(self):
        """
        Charge le vaisseau principal.
        """
        weaponsprite = self.load_manager.get_resource('fire')
        mainWeapon = Weapon(1, weaponsprite)
        myMainSprite = self.load_manager.get_resource('ship')
        
        mainShip = Ship(self.board, 5, Vector(100, 100), Vector(60, 60), mainWeapon, myMainSprite)
        mainShip.pos.x = self.board.width/2
        mainShip.pos.y = self.board.height * 7/8
        
        self.board.mainShip = mainShip
    
    def reset(self):
        """
        Réinitialise le plateau de jeu et le gestionnaire de niveaux.
        """
        self.board.reset()
        self.stage_manager.reset()
        self.running = False
        
    def cheatCode(self, code):
        """
        Applique un code de triche.
        
        Args:
            code (str): Le code de triche à appliquer.
        """
        print(code)
        if(code == "dead"):
            self.stage_manager.nextStage()
        if(code == "help"):
            self.board.mainShip.HP += 1
            
        if(code == "ez"):
            self.stage_manager.numStage = 26
            self.stage_manager.nextStage()
            
        if(code == "300"):
            self.stage_manager.numStage = 4
            self.stage_manager.nextStage()
        
    def pause(self):
        """
        Met le jeu en pause.
        """
        self.running = False
        
    def unPause(self):
        """
        Reprend le jeu après une pause.
        """
        self.running = True
        
    def endSequence(self):
        """
        Termine la séquence de jeu et appelle la fonction de rappel de fin de séquence.
        """
        self.callback_endSequence(self.board.points)
        
    def get_points(self):
        """
        Retourne les points du joueur.
        
        Returns:
            int: Les points du joueur.
        """
        return self.board.points
    
    def get_stage(self):
        """
        Retourne le numéro du niveau actuel.
        
        Returns:
            int: Le numéro du niveau actuel.
        """
        return self.stage_manager.numStage
