# coding=utf-8

# on rend accessible les variables globales définies ici

import sys
from os.path import abspath
path_of_here = abspath(__file__)
sys.path.append(path_of_here)

# ________________________________ définition des constantes

# générales
LIMIT_TIME = 1000
TURN_LIMIT = 1500
SERVER_PORT = 1337
SERVER_IP = 'localhost'

# tuiles
DUNE = 'D'
SABLE = 'S'
FRITE = 'F'
BIERE = 'B'
INFRANCHISSABLE = 'X'

# directions
UP = 'N'
DOWN = 'S'
RIGHT = 'E'
LEFT = 'O'
IDLE = 'C'
