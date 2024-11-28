"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: ScoreManager
Description: Cette classe gère les scores des joueurs, y compris la récupération et l'ajout de scores au leaderboard.
TODO: Ajouter des fonctionnalités spécifiques pour la gestion des scores, comme la suppression de scores, la mise à jour de scores existants ou l'intégration avec une base de données en ligne.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

import json

class ScoreManager:
    """
    Classe représentant le gestionnaire des scores.
    
    Attributs:
        filename (str): Le nom du fichier JSON contenant les scores.
    """
    def __init__(self) -> None:
        """
        Initialise le gestionnaire des scores avec le nom du fichier JSON.
        """
        self.filename = 'database/score.json'

    def getAllData(self):
        """
        Récupère toutes les données du fichier JSON.
        
        Returns:
            dict: Les données JSON sous forme de dictionnaire.
        """
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        return json_data
        
    def get_score(self):
        """
        Récupère le leaderboard des scores.
        
        Returns:
            list: La liste des scores du leaderboard.
        """
        json_data = self.getAllData()
        return json_data['leaderboard']
    
    def addScore(self, name, score, stage):
        """
        Ajoute un nouveau score au leaderboard.
        
        Args:
            name (str): Le nom du joueur.
            score (int): Le score du joueur.
            stage (int): Le niveau atteint par le joueur.
        """
        new_data = {"name": name,
                    "score": score,
                    "stage": stage}
        
        json_data = self.getAllData()
        json_data["leaderboard"].append(new_data)
        with open(self.filename, 'w') as file:
            json.dump(json_data, file, indent=4)  # convert back to json.