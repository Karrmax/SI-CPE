# SI-CPE

SPACE INVADERS  [ 3ETI ]
GRIVOT PELISSON Jules & DZIOPA Raphael

Table des Matières 

1. Présentation
2. Bibliographie
3. Structure
4. Cheatcodes
5. Details
    4.1 Database JSON
    4.2 Fonctions des Vecteurs
    4.3 Elements du jeux
    4.4 Managers
    4.5 Screens avec tkinter

________________________________________________________________________________________________
////////////////////////////////////////////////////////////////////////////////////////////////
PRESENTATION:

Space Invader. Le Jeux du groupe de GRIVOT PELISSON Jules et DZIOPA Raphael.

D'après les cours de CS-DEV avec les notion de python, tkinter, les classes dans python, et des ajouts de JSON.
________________________________________________________________________________________________
////////////////////////////////////////////////////////////////////////////////////////////////
BIBLIOGRAPHIE:

Alien2 image: https://www.artstation.com/artwork/zA3B9m
Alien3 image: https://www.pngfind.com/mpng/hJRJhhJ_spaceship-8-bit-heart-png-transparent-png/ 

Univers bakcground images: https://www.behance.net/gallery/27427543/The-universe 
Sci-fi wall image: https://i.pinimg.com/originals/9c/ca/7b/9cca7b50b65883b87df42b7347a31fda.gif 
________________________________________________________________________________________________
////////////////////////////////////////////////////////////////////////////////////////////////
STRUCTURE:

6 Dossiers:

    - database  [dossier]
        - score.json  [Fichier JSON]
        > Sauvgarde des nom, score de chaque joueur
    - divers    [dossier]
        - Vector.py [Fichier PYTHON]
        > Class de vecteurs 2D et plusieurs fonctions de traitement vectorielle.
    - game [dossier]
        > Multiple fichiers
        > Classes pour chaque element avec leurs fonctions.
    - managers [dossier]
        > Multiple fichiers
        > Classes pour gerer des action repetitives.
    - ressources    [dossier]
        > Images pour chaque object à être affiché
    - screens   [dossier]
        > Multiple fichiers
        > Graphismes à travers tkinter

main.py [Fichier PYTHON]
    - !!! Run pour lancer le jeux. !!!
    - Contiens la loop pour lancer le jeux avec ses 3 écrans d'affichage.
________________________________________________________________________________________________
////////////////////////////////////////////////////////////////////////////////////////////////
CHEAT CODES:

dead == tue tout enemi et skip le stage (niveau actuel)
help == gagner un HP
ez == avance au niveau 27 
________________________________________________________________________________________________
////////////////////////////////////////////////////////////////////////////////////////////////
DETAILS:

_____________
Database JSON
^^^^^^^^^^^^^

On utilise une database JSON pour stocker les données de chaque utilisateur à la fin de leur partie.
Le JSON ici permet de modifier un fichier directement avec un fonction de python pour enregistrer les scores et qu'ils soient gardées même si le jeux ne tourne pas.

______________________
Fonctions des Vecteurs
^^^^^^^^^^^^^^^^^^^^^^

On à crée une class VECTEUR, pour traiter toute information pour des vecteurs.
Etant dans un milieu en 2D (selon x,y), il y a plus demande pour modifier ces vecteurs à travers le jeux.

________________
Elements du jeux
^^^^^^^^^^^^^^^^

On utilise

________
Managers
^^^^^^^^

On utilise

____________________
Screens avec tkinter
^^^^^^^^^^^^^^^^^^^^

Ces fichiers "screens" effectuent l'affichage de la fenêtre tkinter.
