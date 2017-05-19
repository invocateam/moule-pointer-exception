# coding=utf-8

# on rend accessible les variables globales définies ici

import sys
from os.path import abspath
path_of_here = abspath(__file__)
sys.path.append(path_of_here)

# ________________________________ définition des constantes

# générales
LIMIT_TIME = 1000
NOMBRE_DE_TOURS_LIMITE = 1500
PORT_SERVEUR = 1337
IP_SERVEUR = 'localhost'

# tuiles
DUNE = 'D'
SABLE = 'S'
FRITE = 'F'
BIERE = 'B'
INFRANCHISSABLE = 'X'

# directions
HAUT = 'N'
BAS = 'S'
DROITE = 'E'
GAUCHE = 'O'
PASSER_LE_TOUR = 'C'
