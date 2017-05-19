#!/usr/bin/env python
# coding=utf-8

# chargement de la configuration
from config import *
from packages.network.network import NetworkInterface

# ________________________________ imports des fonctions de plus haut niveau, qui seront appelées tour à tour




# ________________________________ exécution
from packages.game.game import Game
from packages.network.network import NetworkInterface

client = NetworkInterface()

r = ""
game = None
while r != "FIN":
    if(game == None):
      game = Game(net.receive())
    else:
      game.update(net.receive())
    game.board.update_board(game.players[net.team_num])
    r = client.action(IDLE)
    print("main", r)
    