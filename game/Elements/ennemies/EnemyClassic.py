from game.Elements.Enemy import Enemy
from divers.Vector import NULLVECTOR

class EnemyClassic(Enemy):
    def __init__(self, board, position, size, weapon, speed = NULLVECTOR, shootProbability = 0, points = 10, ) -> None:
        sprite = board.load_manager.enemyRessources['enemy1']
        super().__init__(board, 1, position, size, weapon, sprite, speed, shootProbability, points)