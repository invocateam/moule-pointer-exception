# coding=utf-8

# on rend accessible les variables globales définies ici

import sys
from os.path import abspath
path_of_here = abspath(__file__)
sys.path.append(path_of_here)

# ________________________________ définition des constantes

LIMIT_TIME = '1000'
DUNE = 'D'
SABLE = 'S'
FRITE = 'F'
BIERE = 'B'
INFRANCHISSABLE = 'X'
HAUT = 'N'
BAS = 'S'
DROITE = 'E'
GAUCHE = 'O'
PASSER_LE_TOUR = 'C'
