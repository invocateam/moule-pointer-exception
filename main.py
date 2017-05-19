#!/usr/bin/env python
# coding=utf-8

# chargement de la configuration
from config import *
from packages.network.network import NetworkInterface

# ________________________________ imports des fonctions de plus haut niveau, qui seront appelées tour à tour




# ________________________________ exécution


client = NetworkInterface()

r = ""

while r != "FIN":
    r = client.action(IDLE)
    print("main", r)
