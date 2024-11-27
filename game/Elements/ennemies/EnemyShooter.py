from Elements.Enemy import Enemy
from divers.Vector import NULLVECTOR

class EnemyShooter(Enemy):
    def __init__(self, board, position, size, weapon, speed = NULLVECTOR, shootProbability = 0, points = 30) -> None:
        sprite = board.load_manager.enemyRessources['enemy2'] 
        super().__init__(board,1, position, size, weapon, sprite, speed, shootProbability, points)