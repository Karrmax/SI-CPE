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

Planet background images: https://www.behance.net/gallery/27427543/The-universe 
Sci-fi wall image: https://i.pinimg.com/originals/9c/ca/7b/9cca7b50b65883b87df42b7347a31fda.gif 
Intro space image: https://www.freepik.com/premium-vector/generative-ai-galaxy-space-planets-stars-landscape-8bit-pixel-art-background-retrofuturistic-arcade-game-scene-with-starry-cosmos-sky-capturing-essence-cosmic-adventure-exploration_60119324.html 
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

Il existe plusieurs cheat codes qui ont été laissé dans cette version du jeux, qui provenait de debugging et qui sont laissé pour aider le joueur si il en a besoin. Les codes sont bien sûr caché et jamais révélé au joueur.

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

On utilise plusieurs managers pour gérer individuellement des aspects repetitifs à chaque frame.

- Input Manager:
    - Ce manager va vérifier a chaque frame si une presse du clavier à été detectée et ajoute la touche activé dans un contenant qui est transmit à la logique du game à traiter pour modifier le jeux.
- Load manager:
    - Celui-ci a pour role de charger avant le lancement du jeux, les assets, images necessaires pour l'affichage. Cela réduit la latence lors du jeux en décalent le temps de latence lors du chargement de l'application.
- Render manager:
    - Il s'occupe d'afficher à chaque frame les elements du jeux qui bougent. Tout les ennemis, murs, projectiles et le joueur. 
    - Il efface tout ces elements au début de chaque frame pour les réafficher apres dans leur nouvelle posisition.
- Score manager:
    - Il charge le fichier de score JSON, et prend le score final avec le nom et le stage pour l'ajouter au fichier JSON.
    - Il renvoie aussi les donnée pou rles afficher dans le Leaderboard.
____________________
Screens avec tkinter
^^^^^^^^^^^^^^^^^^^^

Ces fichiers "screens" effectuent l'affichage de la fenêtre tkinter.
