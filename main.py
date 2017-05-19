#!/usr/bin/env python
# coding=utf-8

# chargement de la configuration
from config import *
from packages.game.decision import ask_for_objective
from packages.game.game import Game
from packages.network.network import NetworkInterface

# ________________________________ imports des fonctions de plus haut niveau, qui seront appelées tour à tour

# ________________________________ exécution


net = NetworkInterface()

r = ""
game = None
next_input = net.receive()
while next_input != 'FIN':
    if game is None:
        game = Game(next_input)
    else:
        game.update(next_input)
    if len(game.currentDir) == 0:
        print("Searching")
        loots = game.board.update_weight(game.players[net.team_num])
        objective = ask_for_objective(game.board.board, loots)
        game.set_direction(*objective)
    nextdirection = game.next(net.team_num)
    print("Gonna move to : ", nextdirection)
    net.action(nextdirection)
    next_input = net.receive()
