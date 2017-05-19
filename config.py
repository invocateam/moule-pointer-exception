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
RESPONSE_SIZE = 999999
TEAM_NAME = "Invocateam"

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

# exploration de la map
MAX_WEIGHT = 100

# constantes de pondération (choix avec score)
MOY_VAL_MOULE = 55
BONUS_BIERE = MOY_VAL_MOULE / 5
BONUS_MOULE = MOY_VAL_MOULE / -5
