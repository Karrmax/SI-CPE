"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Main
Description: Ce fichier contient le point d'entrée principal de l'application. Il initialise et démarre l'application.
TODO: Ajouter des fonctionnalités spécifiques pour le point d'entrée principal, comme la gestion des arguments de ligne de commande ou des configurations de démarrage.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

from screens.MainRoot import MainRoot

def main():
    """
    Point d'entrée principal de l'application.
    Initialise et démarre l'application.
    """
    app = MainRoot()
    app.start()

if __name__ == "__main__":
    main()