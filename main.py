#!/usr/bin/env python
# coding=utf-8

# chargement de la configuration
from config import *

# ________________________________ imports des fonctions de plus haut niveau, qui seront appelées tour à tour




# ________________________________ exécution
from packages.game.game import Game
from packages.network.network import NetworkInterface

net = NetworkInterface()
game = Game(net.receive())
game.board.update_board(game.players[net.team_num])
